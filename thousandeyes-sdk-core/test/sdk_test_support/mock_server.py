# Copyright 2024 Cisco Systems, Inc. and its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
import re
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, Mapping, Optional
from urllib.parse import urlparse

from sdk_test_support.mock_server_types import OperationExpectation

OPERATION_ID_HEADER = "X-TE-Operation-Id"
ERROR_STATUS_HEADER = "X-TE-Error-Status"
AUTHORIZATION_HEADER = "Authorization"


def _normalize_scalar(value: Any) -> Any:
    if isinstance(value, str) and "T" in value:
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00")).isoformat().replace("+00:00", "Z")
        except ValueError:
            return value
    return value


def _normalize_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _normalize_json(value[key]) for key in sorted(value.keys())}
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    return _normalize_scalar(value)


def _json_body_matches(expected: Any, actual: Any) -> bool:
    if isinstance(expected, dict) and isinstance(actual, dict):
        for key in actual:
            if key not in expected:
                return False
            if not _json_body_matches(expected[key], actual[key]):
                return False
        return True
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return False
        return all(_json_body_matches(expected_item, actual_item)
                   for expected_item, actual_item in zip(expected, actual))
    return _normalize_json(expected) == _normalize_json(actual)


class MockApiServer:
    def __init__(self, manifest: Mapping[str, OperationExpectation], host: str = "127.0.0.1", port: int = 0):
        self._manifest = dict(manifest)
        self._host = host
        self._port = port
        self._server: Optional[ThreadingHTTPServer] = None
        self._thread: Optional[threading.Thread] = None

    @property
    def base_url(self) -> str:
        if self._server is None:
            raise RuntimeError("MockApiServer has not been started")
        return f"http://{self._host}:{self._server.server_port}"

    def start(self) -> None:
        if self._server is not None:
            return

        manifest = self._manifest
        handler = _build_handler(manifest)
        self._server = ThreadingHTTPServer((self._host, self._port), handler)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._server is None:
            return
        self._server.shutdown()
        self._server.server_close()
        if self._thread is not None:
            self._thread.join(timeout=5)
        self._server = None
        self._thread = None

    def __enter__(self) -> "MockApiServer":
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.stop()


def _build_handler(manifest: Mapping[str, OperationExpectation]):
    class MockApiRequestHandler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args) -> None:
            return

        def do_GET(self) -> None:
            self._handle_request("GET")

        def do_POST(self) -> None:
            self._handle_request("POST")

        def do_PUT(self) -> None:
            self._handle_request("PUT")

        def do_PATCH(self) -> None:
            self._handle_request("PATCH")

        def do_DELETE(self) -> None:
            self._handle_request("DELETE")

        def _handle_request(self, method: str) -> None:
            auth_error = _validate_authorization(self.headers.get(AUTHORIZATION_HEADER))
            if auth_error is not None:
                self._write_json(auth_error, 401)
                return

            operation_id = self.headers.get(OPERATION_ID_HEADER)
            if not operation_id:
                self._write_json({"detail": f"Missing required header {OPERATION_ID_HEADER}"}, 400)
                return

            expectation = manifest.get(operation_id)
            if expectation is None:
                self._write_json({"detail": f"Unknown operation id {operation_id}"}, 400)
                return

            if expectation.method.upper() != method.upper():
                self._write_json(
                    {"detail": f"Unexpected HTTP method {method} for operation {operation_id}"},
                    400,
                )
                return

            parsed = urlparse(self.path)
            if not _path_matches(expectation.path, parsed.path):
                self._write_json({"detail": "Path does not match operation expectation"}, 400)
                return

            error_status_header = self.headers.get(ERROR_STATUS_HEADER)
            if error_status_header:
                self._handle_error_response(expectation, error_status_header)
                return

            body_bytes = _read_body(self)
            if expectation.request_body_example is not None:
                if not body_bytes:
                    self._write_json({"detail": "Expected request body"}, 400)
                    return
                try:
                    request_json = json.loads(body_bytes.decode("utf-8"))
                except json.JSONDecodeError:
                    self._write_json({"detail": "Invalid JSON request body"}, 400)
                    return
                if not _json_body_matches(expectation.request_body_example, request_json):
                    self._write_json({"detail": "Request body does not match OAS example"}, 400)
                    return

            if expectation.success_body is None:
                self.send_response(expectation.success_status)
                self.end_headers()
                return

            self._write_json(
                expectation.success_body,
                expectation.success_status,
                expectation.success_content_type,
            )

        def _handle_error_response(self, expectation: OperationExpectation, error_status_header: str) -> None:
            error_response = expectation.error_responses.get(error_status_header)
            if error_response is None:
                self._write_json(
                    {"detail": f"No configured error response for status {error_status_header}"},
                    400,
                )
                return
            if error_response.body is None:
                self.send_response(error_response.status)
                self.end_headers()
                return
            self._write_json(error_response.body, error_response.status, error_response.content_type)

        def _write_json(self, body: Any, status: int, content_type: str = "application/json") -> None:
            payload = json.dumps(body).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    return MockApiRequestHandler


def _validate_authorization(value: Optional[str]) -> Optional[Dict[str, str]]:
    if value is None or not value.strip():
        return {"detail": f"Missing or empty required header {AUTHORIZATION_HEADER}"}
    return None


def _read_body(handler: BaseHTTPRequestHandler) -> bytes:
    length = handler.headers.get("Content-Length")
    if not length:
        return b""
    return handler.rfile.read(int(length))


def _path_matches(template: str, actual_path: str) -> bool:
    pattern = re.sub(r"\{[^/]+\}", r"[^/]+", template)
    pattern = f"^{pattern}$"
    return re.match(pattern, actual_path) is not None
