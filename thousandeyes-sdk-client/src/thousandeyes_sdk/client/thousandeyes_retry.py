import re
import time
import typing
from typing import Optional, Union

from urllib3 import BaseHTTPResponse
from urllib3.util.retry import RequestHistory, Retry


class ThousandEyesRetry(Retry):
    RATE_LIMIT_RESET_HEADERS = {
        "x-organization-rate-limit-reset",
        "x-instant-test-rate-limit-reset"
    }

    def __init__(
            self,
            total: Union[bool, int, None] = 10,
            connect: Optional[int] = None,
            read: Optional[int] = None,
            redirect: Union[bool, int, None] = None,
            status: Optional[int] = None,
            other: Optional[int] = None,
            allowed_methods: Optional[typing.Collection[str]] = Retry.DEFAULT_ALLOWED_METHODS,
            status_forcelist=None,
            backoff_factor: float = 0,
            backoff_max: float = Retry.DEFAULT_BACKOFF_MAX,
            raise_on_redirect: bool = False,
            raise_on_status: bool = False,
            history: Optional[tuple[RequestHistory, ...]] = None,
            respect_retry_after_header: bool = True,
            remove_headers_on_redirect: typing.Collection[
                str
            ] = Retry.DEFAULT_REMOVE_HEADERS_ON_REDIRECT,
            backoff_jitter: float = 0.0) -> None:
        super().__init__(total, connect, read, redirect, status, other, allowed_methods,
                         [429] if status_forcelist is None else status_forcelist,
                         backoff_factor, backoff_max, raise_on_redirect,
                         raise_on_status, history, respect_retry_after_header,
                         remove_headers_on_redirect, backoff_jitter)

    def get_retry_after(self, response: BaseHTTPResponse) -> Optional[float]:
        retry_after: Optional[float] = super().get_retry_after(response)

        if retry_after:
            return retry_after

        for header in self.RATE_LIMIT_RESET_HEADERS:
            value = self._parse_reset_header(response.headers.get(header))
            if value and (retry_after is None or value > retry_after):
                retry_after = value

        return retry_after

    @staticmethod
    def _parse_reset_header(value: Optional[str]) -> Optional[float]:
        if value is None or not re.match(r"^\s*[0-9]+\s*$", value):
            return None

        seconds: float = int(value) - time.time()
        return max(seconds, 0)
