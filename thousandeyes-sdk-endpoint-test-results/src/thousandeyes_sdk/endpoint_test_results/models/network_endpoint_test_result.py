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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from thousandeyes_sdk.endpoint_test_results.models.endpoint_ping_data_point_score import EndpointPingDataPointScore
from thousandeyes_sdk.endpoint_test_results.models.endpoint_zta_metrics import EndpointZtaMetrics
from thousandeyes_sdk.endpoint_test_results.models.network_profile import NetworkProfile
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from thousandeyes_sdk.endpoint_test_results.models.target_profile import TargetProfile
from thousandeyes_sdk.endpoint_test_results.models.vpn_profile import VpnProfile
from typing import Optional, Set
from typing_extensions import Self

class NetworkEndpointTestResult(BaseModel):
    """
    NetworkEndpointTestResult
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
    avg_latency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Average RTT for packets sent to destination.", alias="avgLatency")
    error_details: Optional[StrictStr] = Field(default=None, description="Error details, if an error was encountered.", alias="errorDetails")
    jitter: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Standard deviation of latency.")
    score: Optional[EndpointPingDataPointScore] = None
    zta_metrics: Optional[List[EndpointZtaMetrics]] = Field(default=None, alias="ztaMetrics")
    is_icmp_blocked: Optional[StrictBool] = Field(default=None, description="Set to `true` if network target is blocking ICMP echo (ping) queries.", alias="isIcmpBlocked")
    loss: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of packets not reaching destination.")
    max_latency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum RTT for packets sent to destination.", alias="maxLatency")
    min_latency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum RTT for packets sent to destination.", alias="minLatency")
    __properties: ClassVar[List[str]] = ["aid", "testId", "agentId", "roundId", "serverIp", "networkProfile", "systemMetrics", "originalTargetProfile", "vpnProfile", "avgLatency", "errorDetails", "jitter", "score", "ztaMetrics", "isIcmpBlocked", "loss", "maxLatency", "minLatency"]

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
        """Create an instance of NetworkEndpointTestResult from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "test_id",
            "agent_id",
            "round_id",
            "server_ip",
            "avg_latency",
            "error_details",
            "jitter",
            "is_icmp_blocked",
            "loss",
            "max_latency",
            "min_latency",
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
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in zta_metrics (list)
        _items = []
        if self.zta_metrics:
            for _item in self.zta_metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ztaMetrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkEndpointTestResult from a dict"""
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
            "avgLatency": obj.get("avgLatency"),
            "errorDetails": obj.get("errorDetails"),
            "jitter": obj.get("jitter"),
            "score": EndpointPingDataPointScore.from_dict(obj["score"]) if obj.get("score") is not None else None,
            "ztaMetrics": [EndpointZtaMetrics.from_dict(_item) for _item in obj["ztaMetrics"]] if obj.get("ztaMetrics") is not None else None,
            "isIcmpBlocked": obj.get("isIcmpBlocked"),
            "loss": obj.get("loss"),
            "maxLatency": obj.get("maxLatency"),
            "minLatency": obj.get("minLatency")
        })
        return _obj


