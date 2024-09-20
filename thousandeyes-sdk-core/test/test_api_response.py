import pytest
from pydantic import ValidationError
from thousandeyes_sdk.core.api_response import ApiResponse


def test_api_response_valid():
    response = ApiResponse(
        status_code=200,
        headers={"Content-Type": "application/json"},
        data={"key": "value"},
        raw_data=b'{"key": "value"}'
    )
    assert response.status_code == 200
    assert response.headers == {"Content-Type": "application/json"}
    assert response.data == {"key": "value"}
    assert response.raw_data == b'{"key": "value"}'


def test_api_response_missing_optional_headers():
    response = ApiResponse(
        status_code=200,
        data={"key": "value"},
        raw_data=b'{"key": "value"}'
    )
    assert response.status_code == 200
    assert response.headers is None
    assert response.data == {"key": "value"}
    assert response.raw_data == b'{"key": "value"}'


def test_api_response_invalid_status_code():
    with pytest.raises(ValidationError):
        ApiResponse(
            status_code="200",  # Invalid type
            headers={"Content-Type": "application/json"},
            data={"key": "value"},
            raw_data=b'{"key": "value"}'
        )


def test_api_response_invalid_raw_data():
    with pytest.raises(ValidationError):
        ApiResponse(
            status_code=200,
            headers={"Content-Type": "application/json"},
            data={"key": "value"},
            raw_data="raw data"  # Invalid type
        )
