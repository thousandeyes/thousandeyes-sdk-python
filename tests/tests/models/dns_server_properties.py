# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
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
from tests.models.dns_query_class import DnsQueryClass
from tests.models.test_dns_server import TestDnsServer
from tests.models.test_dns_transport_protocol import TestDnsTransportProtocol
from tests.models.test_ipv6_policy import TestIpv6Policy
from tests.models.test_path_trace_mode import TestPathTraceMode
from tests.models.test_probe_mode import TestProbeMode
from tests.models.test_protocol import TestProtocol
from typing import Optional, Set
from typing_extensions import Self

class DnsServerProperties(BaseModel):
    """
    DnsServerProperties
    """ # noqa: E501
    bandwidth_measurements: Optional[StrictBool] = Field(default=None, description="Set to `true` to enable bandwidth measurements, only applies to Enterprise agents assigned to the test.", alias="bandwidthMeasurements")
    dns_servers: List[TestDnsServer] = Field(alias="dnsServers")
    dns_transport_protocol: Optional[TestDnsTransportProtocol] = Field(default=None, alias="dnsTransportProtocol")
    domain: StrictStr = Field(description="The target record for the test, with the record type suffixed. If no record type is specified, the test defaults to an ANY record.")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    recursive_queries: Optional[StrictBool] = Field(default=None, description="Set true to run query with RD (recursion desired) flag enabled.", alias="recursiveQueries")
    ipv6_policy: Optional[TestIpv6Policy] = Field(default=None, alias="ipv6Policy")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    dns_query_class: Optional[DnsQueryClass] = Field(default=None, alias="dnsQueryClass")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["bandwidthMeasurements", "dnsServers", "dnsTransportProtocol", "domain", "mtuMeasurements", "networkMeasurements", "numPathTraces", "pathTraceMode", "probeMode", "protocol", "recursiveQueries", "ipv6Policy", "fixedPacketRate", "dnsQueryClass", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DnsServerProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in dns_servers (list)
        _items = []
        if self.dns_servers:
            for _item in self.dns_servers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dnsServers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DnsServerProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bandwidthMeasurements": obj.get("bandwidthMeasurements"),
            "dnsServers": [TestDnsServer.from_dict(_item) for _item in obj["dnsServers"]] if obj.get("dnsServers") is not None else None,
            "dnsTransportProtocol": obj.get("dnsTransportProtocol"),
            "domain": obj.get("domain"),
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "pathTraceMode": obj.get("pathTraceMode"),
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "recursiveQueries": obj.get("recursiveQueries"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "dnsQueryClass": obj.get("dnsQueryClass"),
            "type": obj.get("type")
        })
        return _obj


