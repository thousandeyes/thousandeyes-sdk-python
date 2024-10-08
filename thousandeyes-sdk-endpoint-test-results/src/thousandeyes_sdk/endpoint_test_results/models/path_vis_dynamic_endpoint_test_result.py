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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.asn_details import AsnDetails
from thousandeyes_sdk.endpoint_test_results.models.dynamic_endpoint_test_webex import DynamicEndpointTestWebex
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_trace import EndpointPathTrace
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_result_protocol import EndpointTestResultProtocol
from thousandeyes_sdk.endpoint_test_results.models.network_profile import NetworkProfile
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from thousandeyes_sdk.endpoint_test_results.models.target_profile import TargetProfile
from thousandeyes_sdk.endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.udp_probe_mode_response import UdpProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.vpn_profile import VpnProfile
from typing import Optional, Set
from typing_extensions import Self

class PathVisDynamicEndpointTestResult(BaseModel):
    """
    PathVisDynamicEndpointTestResult
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint.")
    test_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint test.", alias="testId")
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint agent, from `/endpoint/agents` endpoint.", alias="agentId")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round.", alias="roundId")
    server_ip: Optional[StrictStr] = Field(default=None, description="IP address of target server.", alias="serverIp")
    network_profile: Optional[NetworkProfile] = Field(default=None, alias="networkProfile")
    system_metrics: Optional[SystemMetrics] = Field(default=None, alias="systemMetrics")
    original_target_profile: Optional[TargetProfile] = Field(default=None, alias="originalTargetProfile")
    vpn_profile: Optional[VpnProfile] = Field(default=None, alias="vpnProfile")
    asn_details: Optional[AsnDetails] = Field(default=None, alias="asnDetails")
    server: Optional[StrictStr] = Field(default=None, description="Target server, including port.")
    source_ip: Optional[StrictStr] = Field(default=None, description="IP address of source endpoint agent.", alias="sourceIp")
    source_prefix: Optional[StrictStr] = Field(default=None, description="IP prefix of source endpoint agent.", alias="sourcePrefix")
    application: Optional[StrictStr] = Field(default=None, description="Which supported application to monitor, can be one of `webex`, `zoom`, `microsoft-teams`.")
    protocol: Optional[EndpointTestResultProtocol] = None
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    udp_probe_mode: Optional[UdpProbeModeResponse] = Field(default=None, alias="udpProbeMode")
    webex: Optional[DynamicEndpointTestWebex] = None
    location: Optional[StrictStr] = Field(default=None, description="Geographic location of the path visualization.")
    path_traces: Optional[List[EndpointPathTrace]] = Field(default=None, description="Shows an iteration of path trace, with each iteration specified by a pathId.", alias="pathTraces")
    __properties: ClassVar[List[str]] = ["aid", "testId", "agentId", "roundId", "serverIp", "networkProfile", "systemMetrics", "originalTargetProfile", "vpnProfile", "asnDetails", "server", "sourceIp", "sourcePrefix", "application", "protocol", "tcpProbeMode", "udpProbeMode", "webex", "location", "pathTraces"]

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
        """Create an instance of PathVisDynamicEndpointTestResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "test_id",
            "agent_id",
            "round_id",
            "server_ip",
            "server",
            "source_ip",
            "source_prefix",
            "location",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of network_profile
        if self.network_profile:
            _dict['networkProfile'] = self.network_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_metrics
        if self.system_metrics:
            _dict['systemMetrics'] = self.system_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_target_profile
        if self.original_target_profile:
            _dict['originalTargetProfile'] = self.original_target_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpn_profile
        if self.vpn_profile:
            _dict['vpnProfile'] = self.vpn_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asn_details
        if self.asn_details:
            _dict['asnDetails'] = self.asn_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webex
        if self.webex:
            _dict['webex'] = self.webex.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in path_traces (list)
        _items = []
        if self.path_traces:
            for _item in self.path_traces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pathTraces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathVisDynamicEndpointTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "testId": obj.get("testId"),
            "agentId": obj.get("agentId"),
            "roundId": obj.get("roundId"),
            "serverIp": obj.get("serverIp"),
            "networkProfile": NetworkProfile.from_dict(obj["networkProfile"]) if obj.get("networkProfile") is not None else None,
            "systemMetrics": SystemMetrics.from_dict(obj["systemMetrics"]) if obj.get("systemMetrics") is not None else None,
            "originalTargetProfile": TargetProfile.from_dict(obj["originalTargetProfile"]) if obj.get("originalTargetProfile") is not None else None,
            "vpnProfile": VpnProfile.from_dict(obj["vpnProfile"]) if obj.get("vpnProfile") is not None else None,
            "asnDetails": AsnDetails.from_dict(obj["asnDetails"]) if obj.get("asnDetails") is not None else None,
            "server": obj.get("server"),
            "sourceIp": obj.get("sourceIp"),
            "sourcePrefix": obj.get("sourcePrefix"),
            "application": obj.get("application"),
            "protocol": obj.get("protocol"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "udpProbeMode": obj.get("udpProbeMode"),
            "webex": DynamicEndpointTestWebex.from_dict(obj["webex"]) if obj.get("webex") is not None else None,
            "location": obj.get("location"),
            "pathTraces": [EndpointPathTrace.from_dict(_item) for _item in obj["pathTraces"]] if obj.get("pathTraces") is not None else None
        })
        return _obj


