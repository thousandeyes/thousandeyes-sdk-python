import pytest

from thousandeyes_sdk.core.exceptions import (
    ApiException,
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    TooManyRequestsException,
    UnauthorizedException,
)


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (400, BadRequestException),
        (401, UnauthorizedException),
        (403, ForbiddenException),
        (404, NotFoundException),
        (429, TooManyRequestsException),
        (500, ServiceException),
        (503, ServiceException),
        (418, ApiException),
    ],
)
def test_exception_class_for_http_status(status, expected):
    assert ApiException.exception_class_for_http_status(status) is expected
