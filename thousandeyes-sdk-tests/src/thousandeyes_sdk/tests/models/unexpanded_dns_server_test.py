# coding: utf-8

"""
    Tests API

    This API allows you to list, create, edit, and delete Network and Application Synthetics tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.tests.models.dns_query_class import DnsQueryClass
from thousandeyes_sdk.tests.models.test_dns_server import TestDnsServer
from thousandeyes_sdk.tests.models.test_dns_transport_protocol import TestDnsTransportProtocol
from thousandeyes_sdk.tests.models.test_interval import TestInterval
from thousandeyes_sdk.tests.models.test_ipv6_policy import TestIpv6Policy
from thousandeyes_sdk.tests.models.test_links import TestLinks
from thousandeyes_sdk.tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.tests.models.test_protocol import TestProtocol
from typing import Optional, Set
from typing_extensions import Self

class UnexpandedDnsServerTest(BaseModel):
    """
    UnexpandedDnsServerTest
    """ # noqa: E501
    interval: TestInterval
    alerts_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if alerts are enabled.", alias="alertsEnabled")
    enabled: Optional[StrictBool] = Field(default=True, description="Test is enabled.")
    created_by: Optional[StrictStr] = Field(default=None, description="User that created the test.", alias="createdBy")
    created_date: Optional[datetime] = Field(default=None, description="UTC created date (ISO date-time format).", alias="createdDate")
    description: Optional[StrictStr] = Field(default=None, description="A description of the test.")
    live_share: Optional[StrictBool] = Field(default=None, description="Indicates if the test is shared with the account group.", alias="liveShare")
    modified_by: Optional[StrictStr] = Field(default=None, description="User that modified the test.", alias="modifiedBy")
    modified_date: Optional[datetime] = Field(default=None, description="UTC last modification date (ISO date-time format).", alias="modifiedDate")
    saved_event: Optional[StrictBool] = Field(default=None, description="Indicates if the test is a saved event.  **Note**: **Saved Events** are now called **Private Snapshots** in the user interface. This change does not affect API. ", alias="savedEvent")
    test_id: Optional[StrictStr] = Field(default=None, description="Each test is assigned an unique ID; this is used to access test information and results from other endpoints.", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="The name of the test. Test name must be unique.", alias="testName")
    type: Optional[StrictStr] = None
    links: Optional[TestLinks] = Field(default=None, alias="_links")
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
    randomized_start_time: Optional[StrictBool] = Field(default=False, description="Indicates whether agents should randomize the start time in each test round.", alias="randomizedStartTime")
    recursive_queries: Optional[StrictBool] = Field(default=None, description="Set true to run query with RD (recursion desired) flag enabled.", alias="recursiveQueries")
    ipv6_policy: Optional[TestIpv6Policy] = Field(default=None, alias="ipv6Policy")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    dns_query_class: Optional[DnsQueryClass] = Field(default=None, alias="dnsQueryClass")
    bgp_measurements: Optional[StrictBool] = Field(default=True, description="Set to `true` to enable bgp measurements.", alias="bgpMeasurements")
    use_public_bgp: Optional[StrictBool] = Field(default=True, description="Indicate if all available public BGP monitors should be used, when ommited defaults to `bgpMeasurements` value.", alias="usePublicBgp")
    __properties: ClassVar[List[str]] = ["interval", "alertsEnabled", "enabled", "createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "bandwidthMeasurements", "dnsServers", "dnsTransportProtocol", "domain", "mtuMeasurements", "networkMeasurements", "numPathTraces", "pathTraceMode", "probeMode", "protocol", "randomizedStartTime", "recursiveQueries", "ipv6Policy", "fixedPacketRate", "dnsQueryClass", "bgpMeasurements", "usePublicBgp"]

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
        """Create an instance of UnexpandedDnsServerTest from a JSON string"""
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
            "created_by",
            "created_date",
            "live_share",
            "modified_by",
            "modified_date",
            "saved_event",
            "test_id",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
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
        """Create an instance of UnexpandedDnsServerTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interval": obj.get("interval"),
            "alertsEnabled": obj.get("alertsEnabled"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "createdBy": obj.get("createdBy"),
            "createdDate": obj.get("createdDate"),
            "description": obj.get("description"),
            "liveShare": obj.get("liveShare"),
            "modifiedBy": obj.get("modifiedBy"),
            "modifiedDate": obj.get("modifiedDate"),
            "savedEvent": obj.get("savedEvent"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "type": obj.get("type"),
            "_links": TestLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
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
            "randomizedStartTime": obj.get("randomizedStartTime") if obj.get("randomizedStartTime") is not None else False,
            "recursiveQueries": obj.get("recursiveQueries"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "dnsQueryClass": obj.get("dnsQueryClass"),
            "bgpMeasurements": obj.get("bgpMeasurements") if obj.get("bgpMeasurements") is not None else True,
            "usePublicBgp": obj.get("usePublicBgp") if obj.get("usePublicBgp") is not None else True
        })
        return _obj


