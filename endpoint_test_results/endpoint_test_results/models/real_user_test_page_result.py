# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
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
from endpoint_test_results.models.real_user_test_page_page_timings import RealUserTestPagePageTimings
from endpoint_test_results.models.system_metrics import SystemMetrics
from typing import Optional, Set
from typing_extensions import Self

class RealUserTestPageResult(BaseModel):
    """
    RealUserTestPageResult
    """ # noqa: E501
    page_id: Optional[StrictStr] = Field(default=None, description="Web page ID. The page ID is unique only within an endpoint real user test.", alias="pageId")
    page_title: Optional[StrictStr] = Field(default=None, description="Web page title.", alias="pageTitle")
    page_url: Optional[StrictStr] = Field(default=None, description="Web page url", alias="pageUrl")
    load_date: Optional[datetime] = Field(default=None, description="UTC date when page load started (ISO date-time format).", alias="loadDate")
    response_code: Optional[StrictInt] = Field(default=None, description="HTTP response code.", alias="responseCode")
    page_timings: Optional[RealUserTestPagePageTimings] = Field(default=None, alias="pageTimings")
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint agent, from `/endpoint/agents` endpoint.", alias="agentId")
    id: Optional[StrictStr] = Field(default=None, description="Endpoint real user test ID. Each endpoint real user test occurrence has a unique ID.")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round.", alias="roundId")
    response_time: Optional[StrictInt] = Field(default=None, description="HTTP server response in milliseconds.", alias="responseTime")
    system_metrics: Optional[SystemMetrics] = Field(default=None, alias="systemMetrics")
    __properties: ClassVar[List[str]] = ["pageId", "pageTitle", "pageUrl", "loadDate", "responseCode", "pageTimings", "agentId", "id", "roundId", "responseTime", "systemMetrics"]

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
        """Create an instance of RealUserTestPageResult from a JSON string"""
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
            "page_id",
            "page_title",
            "page_url",
            "load_date",
            "response_code",
            "agent_id",
            "id",
            "round_id",
            "response_time",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of page_timings
        if self.page_timings:
            _dict['pageTimings'] = self.page_timings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_metrics
        if self.system_metrics:
            _dict['systemMetrics'] = self.system_metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RealUserTestPageResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pageId": obj.get("pageId"),
            "pageTitle": obj.get("pageTitle"),
            "pageUrl": obj.get("pageUrl"),
            "loadDate": obj.get("loadDate"),
            "responseCode": obj.get("responseCode"),
            "pageTimings": RealUserTestPagePageTimings.from_dict(obj["pageTimings"]) if obj.get("pageTimings") is not None else None,
            "agentId": obj.get("agentId"),
            "id": obj.get("id"),
            "roundId": obj.get("roundId"),
            "responseTime": obj.get("responseTime"),
            "systemMetrics": SystemMetrics.from_dict(obj["systemMetrics"]) if obj.get("systemMetrics") is not None else None
        })
        return _obj


