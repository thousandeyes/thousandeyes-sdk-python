# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API operations lets you create and run new instant tests. You will need to be an Account Admin.  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.instant_tests.models.api_client_authentication import ApiClientAuthentication
from thousandeyes_sdk.instant_tests.models.api_request_assertion import ApiRequestAssertion
from thousandeyes_sdk.instant_tests.models.api_request_auth_type import ApiRequestAuthType
from thousandeyes_sdk.instant_tests.models.api_request_header import ApiRequestHeader
from thousandeyes_sdk.instant_tests.models.api_request_method import ApiRequestMethod
from thousandeyes_sdk.instant_tests.models.api_request_variable import ApiRequestVariable
from typing import Optional, Set
from typing_extensions import Self

class ApiRequest(BaseModel):
    """
    ApiRequest
    """ # noqa: E501
    assertions: Optional[List[ApiRequestAssertion]] = Field(default=None, description="List of assertion objects.")
    auth_type: Optional[ApiRequestAuthType] = Field(default=None, alias="authType")
    bearer_token: Optional[StrictStr] = Field(default=None, description="The bearer token if `authType = bearer-token`.", alias="bearerToken")
    body: Optional[StrictStr] = Field(default=None, description="POST/PUT request body. Must be in JSON format.")
    client_authentication: Optional[ApiClientAuthentication] = Field(default=None, alias="clientAuthentication")
    client_id: Optional[StrictStr] = Field(default=None, description="The application ID used when `authType` is set to \"oauth2\".", alias="clientId")
    client_secret: Optional[StrictStr] = Field(default=None, description="The private client secret used when `authType` is set to \"oauth2\".", alias="clientSecret")
    collect_api_response: Optional[StrictBool] = Field(default=True, description="Set to `true` if API response body should be collected and saved. Set to `false` if API response body should not be saved.", alias="collectApiResponse")
    headers: Optional[List[ApiRequestHeader]] = Field(default=None, description="Array of API Request Header objects.")
    method: Optional[ApiRequestMethod] = None
    name: StrictStr = Field(description="API step name, must be unique.")
    password: Optional[StrictStr] = Field(default=None, description="The password if `authType = basic`.")
    scope: Optional[StrictStr] = Field(default=None, description="Application-specific scope values for the access token when `authType` is \"oauth2\".")
    token_url: Optional[StrictStr] = Field(default=None, description="The endpoint used to request the access token when `authType` is \"oauth2\".", alias="tokenUrl")
    url: StrictStr = Field(description="Request url. Supports variables in the format `{{variableName}}`.")
    username: Optional[StrictStr] = Field(default=None, description="The username if `authType = basic`.")
    variables: Optional[List[ApiRequestVariable]] = Field(default=None, description="Array of API post request variable objects.")
    verify_certificate: Optional[StrictBool] = Field(default=False, description="Ignore or acknowledge certificate errors. Set to false to ignore certificate errors.", alias="verifyCertificate")
    wait_time_ms: Optional[StrictInt] = Field(default=None, description="Post request delay before executing the next API requests, in milliseconds.", alias="waitTimeMs")
    __properties: ClassVar[List[str]] = ["assertions", "authType", "bearerToken", "body", "clientAuthentication", "clientId", "clientSecret", "collectApiResponse", "headers", "method", "name", "password", "scope", "tokenUrl", "url", "username", "variables", "verifyCertificate", "waitTimeMs"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return self.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in assertions (list)
        _items = []
        if self.assertions:
            for _item in self.assertions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assertions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in headers (list)
        _items = []
        if self.headers:
            for _item in self.headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['headers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variables (list)
        _items = []
        if self.variables:
            for _item in self.variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assertions": [ApiRequestAssertion.from_dict(_item) for _item in obj["assertions"]] if obj.get("assertions") is not None else None,
            "authType": obj.get("authType"),
            "bearerToken": obj.get("bearerToken"),
            "body": obj.get("body"),
            "clientAuthentication": obj.get("clientAuthentication"),
            "clientId": obj.get("clientId"),
            "clientSecret": obj.get("clientSecret"),
            "collectApiResponse": obj.get("collectApiResponse") if obj.get("collectApiResponse") is not None else True,
            "headers": [ApiRequestHeader.from_dict(_item) for _item in obj["headers"]] if obj.get("headers") is not None else None,
            "method": obj.get("method"),
            "name": obj.get("name"),
            "password": obj.get("password"),
            "scope": obj.get("scope"),
            "tokenUrl": obj.get("tokenUrl"),
            "url": obj.get("url"),
            "username": obj.get("username"),
            "variables": [ApiRequestVariable.from_dict(_item) for _item in obj["variables"]] if obj.get("variables") is not None else None,
            "verifyCertificate": obj.get("verifyCertificate") if obj.get("verifyCertificate") is not None else False,
            "waitTimeMs": obj.get("waitTimeMs")
        })
        return _obj


