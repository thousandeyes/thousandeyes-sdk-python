# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from importlib.metadata import version

import thousandeyes_sdk.endpoint_instant_tests.models

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_instant_test import EndpointAgentToServerInstantTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_test import EndpointAgentToServerTest

from thousandeyes_sdk.core.api_client import ApiClient, RequestSerialized
from thousandeyes_sdk.core.api_response import ApiResponse
from thousandeyes_sdk.core.rest import RESTResponseType


class AgentToServerEndpointInstantScheduledTestsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        api_client.user_agent = "ThousandEyesSDK-Python/{0}".format(version("thousandeyes-sdk-endpoint-instant-tests"))
        self.api_client = api_client


    @validate_call
    def create_agent_to_server_scheduled_instant_test(
        self,
        endpoint_agent_to_server_instant_test: EndpointAgentToServerInstantTest,
        aid: Annotated[Optional[StrictStr], Field(description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> EndpointAgentToServerTest:
        """Run agent to server instant scheduled test

        Creates and runs a new endpoint agent to server instant scheduled test in ThousandEyes.

        :param endpoint_agent_to_server_instant_test: (required)
        :type endpoint_agent_to_server_instant_test: EndpointAgentToServerInstantTest
        :param aid: A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response.
        :type aid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_agent_to_server_scheduled_instant_test_serialize(
            endpoint_agent_to_server_instant_test=endpoint_agent_to_server_instant_test,
            aid=aid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "EndpointAgentToServerTest",
            '400': "ValidationError",
            '401': "UnauthorizedError",
            '403': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            models=thousandeyes_sdk.endpoint_instant_tests.models,
        ).data


    @validate_call
    def create_agent_to_server_scheduled_instant_test_with_http_info(
        self,
        endpoint_agent_to_server_instant_test: EndpointAgentToServerInstantTest,
        aid: Annotated[Optional[StrictStr], Field(description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[EndpointAgentToServerTest]:
        """Run agent to server instant scheduled test

        Creates and runs a new endpoint agent to server instant scheduled test in ThousandEyes.

        :param endpoint_agent_to_server_instant_test: (required)
        :type endpoint_agent_to_server_instant_test: EndpointAgentToServerInstantTest
        :param aid: A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response.
        :type aid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_agent_to_server_scheduled_instant_test_serialize(
            endpoint_agent_to_server_instant_test=endpoint_agent_to_server_instant_test,
            aid=aid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "EndpointAgentToServerTest",
            '400': "ValidationError",
            '401': "UnauthorizedError",
            '403': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            models=thousandeyes_sdk.endpoint_instant_tests.models,
        )


    @validate_call
    def create_agent_to_server_scheduled_instant_test_without_preload_content(
        self,
        endpoint_agent_to_server_instant_test: EndpointAgentToServerInstantTest,
        aid: Annotated[Optional[StrictStr], Field(description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Run agent to server instant scheduled test

        Creates and runs a new endpoint agent to server instant scheduled test in ThousandEyes.

        :param endpoint_agent_to_server_instant_test: (required)
        :type endpoint_agent_to_server_instant_test: EndpointAgentToServerInstantTest
        :param aid: A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response.
        :type aid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_agent_to_server_scheduled_instant_test_serialize(
            endpoint_agent_to_server_instant_test=endpoint_agent_to_server_instant_test,
            aid=aid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "EndpointAgentToServerTest",
            '400': "ValidationError",
            '401': "UnauthorizedError",
            '403': "Error",
            '429': "Error",
            '500': "Error",
            '502': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_agent_to_server_scheduled_instant_test_serialize(
        self,
        endpoint_agent_to_server_instant_test,
        aid,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if aid is not None:
            
            _query_params.append(('aid', aid))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if endpoint_agent_to_server_instant_test is not None:
            _body_params = endpoint_agent_to_server_instant_test


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/hal+json', 
                'application/json', 
                'application/problem+json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/endpoint/tests/scheduled-tests/agent-to-server/instant',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


