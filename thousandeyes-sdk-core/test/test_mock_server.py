import json

import pytest

from sdk_test_support.mock_server import (
    AUTHORIZATION_HEADER,
    ERROR_STATUS_HEADER,
    OPERATION_ID_HEADER,
    MockApiServer,
)
from sdk_test_support.mock_server_types import ErrorResponseExpectation, OperationExpectation


@pytest.fixture
def manifest():
    return {
        "createAlertRule": OperationExpectation(
            operation_id="createAlertRule",
            method="POST",
            path="/alerts/rules",
            request_body_example={"ruleName": "Example"},
            success_status=201,
            success_body={"ruleId": "1"},
            error_responses={
                "400": ErrorResponseExpectation(
                    status=400,
                    body={"title": "Bad Request", "status": 400},
                )
            },
        ),
        "deleteAlertRule": OperationExpectation(
            operation_id="deleteAlertRule",
            method="DELETE",
            path="/alerts/rules/{ruleId}",
            path_param_examples={"ruleId": "127094"},
            success_status=204,
            success_body=None,
        ),
        "getAlertRule": OperationExpectation(
            operation_id="getAlertRule",
            method="GET",
            path="/alerts/rules/{ruleId}",
            path_param_examples={"ruleId": "127094"},
            success_status=200,
            success_body={"ruleId": "127094", "ruleName": "Example"},
        ),
    }


def _request(server: MockApiServer, *, method: str, path: str, headers=None, body=None):
    import urllib.request

    request_headers = {
        AUTHORIZATION_HEADER: "Bearer test-token",
        OPERATION_ID_HEADER: "createAlertRule",
    }
    if headers:
        request_headers.update(headers)

    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        request_headers["Content-Type"] = "application/json"

    request = urllib.request.Request(
        server.base_url + path,
        data=data,
        headers=request_headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(request) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read()


def test_mock_server_happy_path(manifest):
    with MockApiServer(manifest) as server:
        status, body = _request(
            server,
            method="POST",
            path="/alerts/rules",
            body={"ruleName": "Example"},
        )
        assert status == 201
        assert json.loads(body.decode("utf-8")) == {"ruleId": "1"}


def test_mock_server_rejects_missing_authorization(manifest):
    with MockApiServer(manifest) as server:
        status, _ = _request(
            server,
            method="POST",
            path="/alerts/rules",
            headers={AUTHORIZATION_HEADER: ""},
            body={"ruleName": "Example"},
        )
        assert status == 401


def test_mock_server_rejects_invalid_request_body(manifest):
    with MockApiServer(manifest) as server:
        status, _ = _request(
            server,
            method="POST",
            path="/alerts/rules",
            body={"ruleName": "Wrong"},
        )
        assert status == 400


def test_mock_server_error_path(manifest):
    with MockApiServer(manifest) as server:
        status, body = _request(
            server,
            method="POST",
            path="/alerts/rules",
            headers={ERROR_STATUS_HEADER: "400"},
            body={"unexpected": True},
        )
        assert status == 400
        assert json.loads(body.decode("utf-8"))["title"] == "Bad Request"


def test_mock_server_ignores_readonly_fields_in_expected_body(manifest):
    readonly_manifest = {
        **manifest,
        "createAlertRule": OperationExpectation(
            operation_id="createAlertRule",
            method="POST",
            path="/alerts/rules",
            request_body_example={"ruleName": "Example", "ruleId": "read-only"},
            success_status=201,
            success_body={"ruleId": "1"},
        ),
    }
    with MockApiServer(readonly_manifest) as server:
        status, body = _request(
            server,
            method="POST",
            path="/alerts/rules",
            body={"ruleName": "Example"},
        )
        assert status == 201
        assert json.loads(body.decode("utf-8")) == {"ruleId": "1"}


def test_mock_server_no_content_response(manifest):
    with MockApiServer(manifest) as server:
        import urllib.request

        request = urllib.request.Request(
            server.base_url + "/alerts/rules/127094",
            headers={
                AUTHORIZATION_HEADER: "Bearer test-token",
                OPERATION_ID_HEADER: "deleteAlertRule",
            },
            method="DELETE",
        )
        with urllib.request.urlopen(request) as response:
            assert response.status == 204
            assert response.read() == b""


def test_mock_server_matches_path_variable(manifest):
    with MockApiServer(manifest) as server:
        status, body = _request(
            server,
            method="GET",
            path="/alerts/rules/127094",
            headers={OPERATION_ID_HEADER: "getAlertRule"},
        )
        assert status == 200
        assert json.loads(body.decode("utf-8")) == {"ruleId": "127094", "ruleName": "Example"}


def test_mock_server_rejects_path_missing_path_variable(manifest):
    with MockApiServer(manifest) as server:
        status, body = _request(
            server,
            method="GET",
            path="/alerts/rules",
            headers={OPERATION_ID_HEADER: "getAlertRule"},
        )
        assert status == 400
        assert json.loads(body.decode("utf-8"))["detail"] == "Path does not match operation expectation"


def test_mock_server_accepts_equivalent_iso8601_datetime_formats(manifest):
    datetime_manifest = {
        **manifest,
        "createAlertRule": OperationExpectation(
            operation_id="createAlertRule",
            method="POST",
            path="/alerts/rules",
            request_body_example={
                "ruleName": "Example",
                "startDate": "2017-07-01T05:00:00Z",
            },
            success_status=201,
            success_body={"ruleId": "1"},
        ),
    }
    with MockApiServer(datetime_manifest) as server:
        status, body = _request(
            server,
            method="POST",
            path="/alerts/rules",
            body={
                "ruleName": "Example",
                "startDate": "2017-07-01T05:00:00+00:00",
            },
        )
        assert status == 201
        assert json.loads(body.decode("utf-8")) == {"ruleId": "1"}
