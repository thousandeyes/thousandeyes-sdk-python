import pytest
import datetime
from unittest.mock import Mock, patch
from thousandeyes_sdk.core.api_client import ApiClient
from thousandeyes_sdk.core.configuration import Configuration
from thousandeyes_sdk.core import rest
from thousandeyes_sdk.core.exceptions import ApiException


@pytest.fixture
def api_client():
    config = Configuration()
    return ApiClient(configuration=config)


def test_api_client_initialization(api_client):
    assert api_client.configuration is not None
    assert isinstance(api_client.rest_client, rest.RESTClientObject)
    assert api_client.default_headers == {}


def test_set_default_header(api_client):
    api_client.set_default_header('X-Test-Header', 'test_value')
    assert api_client.default_headers['X-Test-Header'] == 'test_value'


def test_user_agent_property(api_client):
    api_client.user_agent = 'test-agent'
    assert api_client.user_agent == 'test-agent'


def test_get_default():
    default_client = ApiClient.get_default()
    assert isinstance(default_client, ApiClient)


def test_set_default():
    new_default = ApiClient()
    ApiClient.set_default(new_default)
    assert ApiClient.get_default() == new_default


def test_param_serialize(api_client):
    method, url, headers, _, __ = api_client.param_serialize(
        method='GET',
        resource_path='/test/{id}',
        path_params={'id': 1},
        query_params={'aid': '12'},
        header_params={'X-Test': 'test_value'}
    )
    assert method == 'GET'
    print(url + "3")
    assert url == api_client.configuration.host + '/test/1?aid=12'
    assert headers['X-Test'] == 'test_value'


@patch('thousandeyes_sdk.core.rest.RESTClientObject.request')
def test_call_api(mock_request, api_client):
    mock_response = Mock()
    mock_response.data = b'{"dummyKey": "someValue"}'
    mock_response.status = 200
    mock_request.return_value = mock_response

    response = api_client.call_api(
        method='GET',
        url='/tests',
        body=None,
        post_params=None,
        _request_timeout=None
    )
    assert response.data == b'{"dummyKey": "someValue"}'
    assert response.status == 200


@patch('thousandeyes_sdk.core.rest.RESTClientObject.request')
def test_call_api_exception(mock_request, api_client):
    mock_request.side_effect = ApiException(status=404, reason="Not Found")
    with pytest.raises(ApiException):
        api_client.call_api(
            method='GET',
            url='/tests',
            body=None,
            post_params=None,
            _request_timeout=None
        )


def test_response_deserialize(api_client):
    mock_response = Mock()
    mock_response.data = b'{"dummyKey": "someValue"}'
    mock_response.status = 200
    mock_response.getheader.return_value = 'application/json'
    mock_response.getheaders.return_value = {}

    response = api_client.response_deserialize(
        response_data=mock_response,
        response_types_map={'200': 'dict'},
        models={}
    )
    assert response.data == {"dummyKey": "someValue"}
    assert response.status_code == 200


def test_sanitize_for_serialization(api_client):
    data = {
        'str': 'value',
        'int': 1,
        'float': 1.1,
        'bool': True,
        'datetime': datetime.datetime(2023, 1, 1),
        'date': datetime.date(2023, 1, 1),
        'list': [1, 2, 3],
        'dict': {'key': 'value'}
    }
    sanitized = api_client.sanitize_for_serialization(data)
    assert sanitized['str'] == 'value'
    assert sanitized['int'] == 1
    assert sanitized['float'] == 1.1
    assert sanitized['bool'] is True
    assert sanitized['datetime'] == '2023-01-01T00:00:00'
    assert sanitized['date'] == '2023-01-01'
    assert sanitized['list'] == [1, 2, 3]
    assert sanitized['dict'] == {'key': 'value'}
