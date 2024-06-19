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

import re
import time
from typing import Collection, Optional, Union

from urllib3 import BaseHTTPResponse
from urllib3.util.retry import RequestHistory, Retry


class ThousandEyesRetry(Retry):
    RATE_LIMIT_RESET_HEADERS = {
        "x-organization-rate-limit-reset",
        "x-instant-test-rate-limit-reset"
    }

    RESET_HEADER_PATTERN = re.compile(r"^\s*[0-9]+\s*$")
    HTTP_TOO_MANY_REQUESTS = 429

    def __init__(
            self,
            total: Union[bool, int, None] = 3,
            connect: Optional[int] = None,
            read: Optional[int] = None,
            redirect: Union[bool, int, None] = None,
            status: Optional[int] = 1,
            other: Optional[int] = None,
            allowed_methods: Optional[Collection[str]] = Retry.DEFAULT_ALLOWED_METHODS,
            status_forcelist=None,
            backoff_factor: float = 0,
            backoff_max: float = Retry.DEFAULT_BACKOFF_MAX,
            raise_on_redirect: bool = False,
            raise_on_status: bool = False,
            history: Optional[tuple[RequestHistory, ...]] = None,
            respect_retry_after_header: bool = True,
            remove_headers_on_redirect: Collection[str] = Retry.DEFAULT_REMOVE_HEADERS_ON_REDIRECT,
            backoff_jitter: float = 0.0) -> None:
        super().__init__(total, connect, read, redirect, status, other, allowed_methods,
                         status_forcelist, backoff_factor, backoff_max, raise_on_redirect,
                         raise_on_status, history, respect_retry_after_header,
                         remove_headers_on_redirect, backoff_jitter)

    def is_retry(self, method: str, status_code: int, has_retry_after: bool = False) -> bool:
        # Always retry on 429, regardless of method or status_forcelist
        return (status_code == self.HTTP_TOO_MANY_REQUESTS or
                super().is_retry(method, status_code, has_retry_after))

    def get_retry_after(self, response: BaseHTTPResponse) -> Optional[float]:
        retry_after: Optional[float] = super().get_retry_after(response)

        if retry_after:
            return retry_after

        for header in self.RATE_LIMIT_RESET_HEADERS:
            value = self._parse_reset_header(response.headers.get(header))
            if value and (retry_after is None or value > retry_after):
                retry_after = value

        return retry_after

    def _parse_reset_header(self, value: Optional[str]) -> Optional[float]:
        if value is None or not self.RESET_HEADER_PATTERN.match(value):
            return None

        seconds: float = int(value) - time.time()
        return max(seconds, 0)
