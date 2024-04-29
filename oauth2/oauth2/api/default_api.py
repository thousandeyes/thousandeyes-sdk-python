# coding: utf-8

"""
    OAuth2 API

    This endpoint allows clients to trade their client credentials for an Access Token that can be used on subsequent calls to our API. Example of usage:    `   curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -d 'client_id=someId&scope=someScope&client_secret=someSecret&grant_type=client_credentials' 'https://api.thousandeyes.com/v7/oauth2/token'   `

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from oauth2.models.access_token import AccessToken

from oauth2.api_client import ApiClient, RequestSerialized
from oauth2.api_response import ApiResponse
from oauth2.rest import RESTResponseType


class DefaultApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def v7_oauth2_token_post(
        self,
        x_tenant_id: Annotated[Optional[StrictStr], Field(description="Tenant ID, only applicable if using the WanInsights Tenant flow")] = None,
        client_id: Annotated[Optional[StrictStr], Field(description="The Application ID.")] = None,
        client_secret: Annotated[Optional[StrictStr], Field(description="The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported.")] = None,
        grant_type: Annotated[Optional[StrictStr], Field(description="Must be set to `client_credentials`.")] = None,
        scope: Annotated[Optional[StrictStr], Field(description="Requested scope values for the new access token.")] = None,
        thousandeyes_bearer_token: Annotated[Optional[StrictStr], Field(description="The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user.")] = None,
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
    ) -> AccessToken:
        """Create and return access token.

        This endpoint uses the client credentials passed alongside the request to create a new access token and return it to the client.

        :param x_tenant_id: Tenant ID, only applicable if using the WanInsights Tenant flow
        :type x_tenant_id: str
        :param client_id: The Application ID.
        :type client_id: str
        :param client_secret: The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported.
        :type client_secret: str
        :param grant_type: Must be set to `client_credentials`.
        :type grant_type: str
        :param scope: Requested scope values for the new access token.
        :type scope: str
        :param thousandeyes_bearer_token: The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user.
        :type thousandeyes_bearer_token: str
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

        _param = self._v7_oauth2_token_post_serialize(
            x_tenant_id=x_tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            thousandeyes_bearer_token=thousandeyes_bearer_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AccessToken",
            '400': "ValidationError",
            '401': "UnauthorizedError",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def v7_oauth2_token_post_with_http_info(
        self,
        x_tenant_id: Annotated[Optional[StrictStr], Field(description="Tenant ID, only applicable if using the WanInsights Tenant flow")] = None,
        client_id: Annotated[Optional[StrictStr], Field(description="The Application ID.")] = None,
        client_secret: Annotated[Optional[StrictStr], Field(description="The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported.")] = None,
        grant_type: Annotated[Optional[StrictStr], Field(description="Must be set to `client_credentials`.")] = None,
        scope: Annotated[Optional[StrictStr], Field(description="Requested scope values for the new access token.")] = None,
        thousandeyes_bearer_token: Annotated[Optional[StrictStr], Field(description="The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user.")] = None,
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
    ) -> ApiResponse[AccessToken]:
        """Create and return access token.

        This endpoint uses the client credentials passed alongside the request to create a new access token and return it to the client.

        :param x_tenant_id: Tenant ID, only applicable if using the WanInsights Tenant flow
        :type x_tenant_id: str
        :param client_id: The Application ID.
        :type client_id: str
        :param client_secret: The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported.
        :type client_secret: str
        :param grant_type: Must be set to `client_credentials`.
        :type grant_type: str
        :param scope: Requested scope values for the new access token.
        :type scope: str
        :param thousandeyes_bearer_token: The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user.
        :type thousandeyes_bearer_token: str
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

        _param = self._v7_oauth2_token_post_serialize(
            x_tenant_id=x_tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            thousandeyes_bearer_token=thousandeyes_bearer_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AccessToken",
            '400': "ValidationError",
            '401': "UnauthorizedError",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def v7_oauth2_token_post_without_preload_content(
        self,
        x_tenant_id: Annotated[Optional[StrictStr], Field(description="Tenant ID, only applicable if using the WanInsights Tenant flow")] = None,
        client_id: Annotated[Optional[StrictStr], Field(description="The Application ID.")] = None,
        client_secret: Annotated[Optional[StrictStr], Field(description="The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported.")] = None,
        grant_type: Annotated[Optional[StrictStr], Field(description="Must be set to `client_credentials`.")] = None,
        scope: Annotated[Optional[StrictStr], Field(description="Requested scope values for the new access token.")] = None,
        thousandeyes_bearer_token: Annotated[Optional[StrictStr], Field(description="The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user.")] = None,
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
        """Create and return access token.

        This endpoint uses the client credentials passed alongside the request to create a new access token and return it to the client.

        :param x_tenant_id: Tenant ID, only applicable if using the WanInsights Tenant flow
        :type x_tenant_id: str
        :param client_id: The Application ID.
        :type client_id: str
        :param client_secret: The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported.
        :type client_secret: str
        :param grant_type: Must be set to `client_credentials`.
        :type grant_type: str
        :param scope: Requested scope values for the new access token.
        :type scope: str
        :param thousandeyes_bearer_token: The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user.
        :type thousandeyes_bearer_token: str
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

        _param = self._v7_oauth2_token_post_serialize(
            x_tenant_id=x_tenant_id,
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            thousandeyes_bearer_token=thousandeyes_bearer_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AccessToken",
            '400': "ValidationError",
            '401': "UnauthorizedError",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _v7_oauth2_token_post_serialize(
        self,
        x_tenant_id,
        client_id,
        client_secret,
        grant_type,
        scope,
        thousandeyes_bearer_token,
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
        # process the header parameters
        if x_tenant_id is not None:
            _header_params['x-tenant-id'] = x_tenant_id
        # process the form parameters
        if client_id is not None:
            _form_params.append(('client_id', client_id))
        if client_secret is not None:
            _form_params.append(('client_secret', client_secret))
        if grant_type is not None:
            _form_params.append(('grant_type', grant_type))
        if scope is not None:
            _form_params.append(('scope', scope))
        if thousandeyes_bearer_token is not None:
            _form_params.append(('thousandeyes_bearer_token', thousandeyes_bearer_token))
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
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
                        'application/x-www-form-urlencoded'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'application'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v7/oauth2/token',
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

