# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_webex import DynamicTestWebex
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.udp_probe_mode_response import UdpProbeModeResponse
from typing import Optional, Set
from typing_extensions import Self

class DynamicBaseTestResult(BaseModel):
    """
    DynamicBaseTestResult
    """ # noqa: E501
    application: Optional[StrictStr] = Field(default=None, description="Which supported application to monitor, can be one of `webex`, `zoom`, `microsoft-teams`.")
    protocol: Optional[EndpointTestProtocol] = None
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    udp_probe_mode: Optional[UdpProbeModeResponse] = Field(default=None, alias="udpProbeMode")
    webex: Optional[DynamicTestWebex] = None
    __properties: ClassVar[List[str]] = ["application", "protocol", "tcpProbeMode", "udpProbeMode", "webex"]

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
        """Create an instance of DynamicBaseTestResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of webex
        if self.webex:
            _dict['webex'] = self.webex.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DynamicBaseTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "application": obj.get("application"),
            "protocol": obj.get("protocol"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "udpProbeMode": obj.get("udpProbeMode"),
            "webex": DynamicTestWebex.from_dict(obj["webex"]) if obj.get("webex") is not None else None
        })
        return _obj


