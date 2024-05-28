# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
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
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_links import DynamicTestLinks
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_test_results.models.test_interval import TestInterval
from thousandeyes_sdk.endpoint_test_results.models.test_label import TestLabel
from thousandeyes_sdk.endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from typing import Optional, Set
from typing_extensions import Self

class DynamicTest(BaseModel):
    """
    DynamicTest
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint.")
    links: Optional[DynamicTestLinks] = Field(default=None, alias="_links")
    agent_selector_config: Optional[EndpointAgentSelectorConfig] = Field(default=None, alias="agentSelectorConfig")
    application: Optional[StrictStr] = Field(default=None, description="Which supported application to monitor, can be one of `webex`, `zoom`, `microsoft-teams`.")
    created_date: Optional[datetime] = Field(default=None, description="UTC created date (ISO date-time format).", alias="createdDate")
    interval: Optional[TestInterval] = None
    is_enabled: Optional[StrictBool] = Field(default=True, description="Indicates if test is enabled.", alias="isEnabled")
    has_path_trace_in_session: Optional[StrictBool] = Field(default=None, description="Enables \"in session\" path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session.", alias="hasPathTraceInSession")
    has_ping: Optional[StrictBool] = Field(default=True, description="Optional flag indicating if the test should run ping.", alias="hasPing")
    has_traceroute: Optional[StrictBool] = Field(default=True, description="Optional flag indicating if the test should run traceroute.", alias="hasTraceroute")
    modified_date: Optional[datetime] = Field(default=None, description="UTC last modification date (ISO date-time format).", alias="modifiedDate")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    protocol: Optional[EndpointTestProtocol] = None
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    test_id: Optional[StrictStr] = Field(default=None, description="Each test is assigned a unique ID; this is used to access test information and results from other endpoints.", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="Name of the test.", alias="testName")
    labels: Optional[List[TestLabel]] = None
    __properties: ClassVar[List[str]] = ["aid", "_links", "agentSelectorConfig", "application", "createdDate", "interval", "isEnabled", "hasPathTraceInSession", "hasPing", "hasTraceroute", "modifiedDate", "networkMeasurements", "protocol", "tcpProbeMode", "testId", "testName", "labels"]

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
        """Create an instance of DynamicTest from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_date",
            "modified_date",
            "test_id",
            "labels",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent_selector_config
        if self.agent_selector_config:
            _dict['agentSelectorConfig'] = self.agent_selector_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DynamicTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "_links": DynamicTestLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "agentSelectorConfig": EndpointAgentSelectorConfig.from_dict(obj["agentSelectorConfig"]) if obj.get("agentSelectorConfig") is not None else None,
            "application": obj.get("application"),
            "createdDate": obj.get("createdDate"),
            "interval": obj.get("interval"),
            "isEnabled": obj.get("isEnabled") if obj.get("isEnabled") is not None else True,
            "hasPathTraceInSession": obj.get("hasPathTraceInSession"),
            "hasPing": obj.get("hasPing") if obj.get("hasPing") is not None else True,
            "hasTraceroute": obj.get("hasTraceroute") if obj.get("hasTraceroute") is not None else True,
            "modifiedDate": obj.get("modifiedDate"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "protocol": obj.get("protocol"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "labels": [TestLabel.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None
        })
        return _obj

