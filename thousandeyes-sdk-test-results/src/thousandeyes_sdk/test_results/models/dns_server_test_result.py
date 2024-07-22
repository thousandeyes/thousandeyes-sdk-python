# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.test_results.models.agent import Agent
from thousandeyes_sdk.test_results.models.test_result_app_links import TestResultAppLinks
from typing import Optional, Set
from typing_extensions import Self

class DnsServerTestResult(BaseModel):
    """
    DnsServerTestResult
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Data point date UTC (ISO date-time format).", alias="date")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="roundId")
    links: Optional[TestResultAppLinks] = Field(default=None, alias="_links")
    start_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="startTime")
    end_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the end time of the round", alias="endTime")
    agent: Optional[Agent] = None
    server_id: Optional[StrictStr] = Field(default=None, description="Internal ID of DNS server being tested", alias="serverId")
    server: Optional[StrictStr] = Field(default=None, description="Canonical name of server being tested")
    resolution_time: Optional[StrictInt] = Field(default=None, description="How long it took to run the query against the serverow long it took to run the query against the server", alias="resolutionTime")
    error_details: Optional[StrictStr] = Field(default=None, description="Error details, if an error were encountered", alias="errorDetails")
    mappings: Optional[StrictStr] = Field(default=None, description="Final mappings returned from the request")
    __properties: ClassVar[List[str]] = ["date", "roundId", "_links", "startTime", "endTime", "agent", "serverId", "server", "resolutionTime", "errorDetails", "mappings"]

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
        """Create an instance of DnsServerTestResult from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "var_date",
            "round_id",
            "start_time",
            "end_time",
            "server_id",
            "server",
            "resolution_time",
            "error_details",
            "mappings",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent
        if self.agent:
            _dict['agent'] = self.agent.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DnsServerTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "roundId": obj.get("roundId"),
            "_links": TestResultAppLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "agent": Agent.from_dict(obj["agent"]) if obj.get("agent") is not None else None,
            "serverId": obj.get("serverId"),
            "server": obj.get("server"),
            "resolutionTime": obj.get("resolutionTime"),
            "errorDetails": obj.get("errorDetails"),
            "mappings": obj.get("mappings")
        })
        return _obj


