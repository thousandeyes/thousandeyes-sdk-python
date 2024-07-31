# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.instant_tests.models.test_dscp_id import TestDscpId
from thousandeyes_sdk.instant_tests.models.test_ipv6_policy import TestIpv6Policy
from thousandeyes_sdk.instant_tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.instant_tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.instant_tests.models.test_protocol import TestProtocol
from typing import Optional, Set
from typing_extensions import Self

class AgentToServerProperties(BaseModel):
    """
    AgentToServerProperties
    """ # noqa: E501
    bandwidth_measurements: Optional[StrictBool] = Field(default=None, description="Set to `true` to enable bandwidth measurements, only applies to Enterprise agents assigned to the test.", alias="bandwidthMeasurements")
    continuous_mode: Optional[StrictBool] = Field(default=None, description="To enable continuous monitoring, set this parameter to `true` to.  When continuous monitoring is enabled, the following actions occur: * `fixedPacketRate` is enforced * `bandwidthMeasurements` are disabled * If the `protocol` is set to `tcp`, `probeMode` is set to `syn`. ", alias="continuousMode")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="If continuousMode is `false`, set the fixedPacketRate to a value between 10-100. If `continuousMode` is `true`, set the `fixedPacketRate` to `1`", alias="fixedPacketRate")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=49153, description="Target port.")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    server: StrictStr = Field(description="Target name or IP address.")
    dscp: Optional[StrictStr] = Field(default=None, description="DSCP label.")
    dscp_id: Optional[TestDscpId] = Field(default=None, alias="dscpId")
    ipv6_policy: Optional[TestIpv6Policy] = Field(default=None, alias="ipv6Policy")
    ping_payload_size: Optional[Annotated[int, Field(le=1400, strict=True, ge=0)]] = Field(default=None, description="Payload size (not total packet size) for the end-to-end metric's probes, ping payload size allows values from 0 to 1400 bytes. When set to null, payload sizes are 0 bytes for ICMP-based tests and 1 byte for TCP-based tests.", alias="pingPayloadSize")
    network_measurements: Optional[StrictBool] = Field(default=False, description="View packet loss in 1-second intervals. This is only available for 1-minute interval tests. Set to `true` to enable network measurements.", alias="networkMeasurements")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["bandwidthMeasurements", "continuousMode", "fixedPacketRate", "mtuMeasurements", "numPathTraces", "pathTraceMode", "port", "probeMode", "protocol", "server", "dscp", "dscpId", "ipv6Policy", "pingPayloadSize", "networkMeasurements", "type"]

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
        """Create an instance of AgentToServerProperties from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "dscp",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentToServerProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bandwidthMeasurements": obj.get("bandwidthMeasurements"),
            "continuousMode": obj.get("continuousMode"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "pathTraceMode": obj.get("pathTraceMode"),
            "port": obj.get("port") if obj.get("port") is not None else 49153,
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "server": obj.get("server"),
            "dscp": obj.get("dscp"),
            "dscpId": obj.get("dscpId"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "pingPayloadSize": obj.get("pingPayloadSize"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else False,
            "type": obj.get("type")
        })
        return _obj


