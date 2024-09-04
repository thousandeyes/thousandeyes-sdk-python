# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_auth_type import EndpointTestAuthType
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class EndpointHttpServerBaseTest(BaseModel):
    """
    EndpointHttpServerBaseTest
    """ # noqa: E501
    auth_type: Optional[EndpointTestAuthType] = Field(default=None, alias="authType")
    has_path_trace_in_session: Optional[StrictBool] = Field(default=None, description="Enables \"in session\" path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session.", alias="hasPathTraceInSession")
    http_time_limit: Optional[StrictInt] = Field(default=5000, description="Maximum amount of time in milliseconds the agents wait before a request times out.", alias="httpTimeLimit")
    protocol: Optional[EndpointTestProtocol] = None
    url: Optional[StrictStr] = Field(default=None, description="Test target URL. Optionally, you can specify a protocol (http or https). If no protocol is provided, the default `https` protocol is used.")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    verify_certificate: Optional[StrictBool] = Field(default=True, description="Flag indicating if a certificate should be verified.", alias="verifyCertificate")
    __properties: ClassVar[List[str]] = ["authType", "hasPathTraceInSession", "httpTimeLimit", "protocol", "url", "username", "sslVersionId", "tcpProbeMode", "verifyCertificate"]

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
        """Create an instance of EndpointHttpServerBaseTest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointHttpServerBaseTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authType": obj.get("authType"),
            "hasPathTraceInSession": obj.get("hasPathTraceInSession"),
            "httpTimeLimit": obj.get("httpTimeLimit") if obj.get("httpTimeLimit") is not None else 5000,
            "protocol": obj.get("protocol"),
            "url": obj.get("url"),
            "username": obj.get("username"),
            "sslVersionId": obj.get("sslVersionId"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "verifyCertificate": obj.get("verifyCertificate") if obj.get("verifyCertificate") is not None else True
        })
        return _obj


