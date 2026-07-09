import time
import pytest
from unittest.mock import Mock
from urllib3 import HTTPResponse
from thousandeyes_sdk.core.thousandeyes_retry import ThousandEyesRetry


def test_is_retry_on_429():
    retry = ThousandEyesRetry()
    assert retry.is_retry("GET", 429) is True


def test_is_retry_on_other_status():
    retry = ThousandEyesRetry(status_forcelist=[500])
    assert retry.is_retry("GET", 500) is True
    assert retry.is_retry("GET", 404) is False


def test_get_retry_after_with_custom_header():
    response = Mock(spec=HTTPResponse)
    response.headers = {
        "x-organization-rate-limit-reset": str(int(time.time()) + 100)}
    retry = ThousandEyesRetry()
    assert retry.get_retry_after(response) == pytest.approx(100, rel=1)


def test_get_retry_after_with_no_headers():
    response = Mock(spec=HTTPResponse)
    response.headers = {}
    retry = ThousandEyesRetry()
    assert retry.get_retry_after(response) is None


def test_parse_reset_header_valid():
    retry = ThousandEyesRetry()
    future_time = str(int(time.time()) + 100)
    assert retry._parse_reset_header(future_time) == pytest.approx(100, rel=1)


def test_parse_reset_header_invalid():
    retry = ThousandEyesRetry()
    assert retry._parse_reset_header("invalid") is None
    assert retry._parse_reset_header(None) is None
