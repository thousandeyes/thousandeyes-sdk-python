# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.7
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
from thousandeyes_sdk.test_results.models.marker import Marker
from thousandeyes_sdk.test_results.models.page import Page
from thousandeyes_sdk.test_results.models.test_result_app_links import TestResultAppLinks
from typing import Optional, Set
from typing_extensions import Self

class WebTransactionPageDetailTestResult(BaseModel):
    """
    WebTransactionPageDetailTestResult
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Data point date UTC (ISO date-time format).", alias="date")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="roundId")
    links: Optional[TestResultAppLinks] = Field(default=None, alias="_links")
    start_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="startTime")
    end_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the end time of the round", alias="endTime")
    agent: Optional[Agent] = None
    component_errors: Optional[StrictInt] = Field(default=None, description="Number of components which did not successfully load", alias="componentErrors")
    transaction_time: Optional[StrictInt] = Field(default=None, description="Elapsed execution time of the web transaction script in milliseconds", alias="transactionTime")
    error_type: Optional[StrictStr] = Field(default=None, description="Type of error encountered; corresponds to phase of connection", alias="errorType")
    error_details: Optional[StrictStr] = Field(default=None, description="Error details, if an error were encountered", alias="errorDetails")
    markers: Optional[List[Marker]] = None
    pages: Optional[List[Page]] = None
    har: Optional[Dict[str, Any]] = Field(default=None, description="See [HAR specification](http://www.softwareishard.com/blog/har-12-spec/) for details")
    __properties: ClassVar[List[str]] = ["date", "roundId", "_links", "startTime", "endTime", "agent", "componentErrors", "transactionTime", "errorType", "errorDetails", "markers", "pages", "har"]

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
        """Create an instance of WebTransactionPageDetailTestResult from a JSON string"""
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
            "component_errors",
            "transaction_time",
            "error_type",
            "error_details",
            "har",
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
        # override the default output from pydantic by calling `to_dict()` of each item in markers (list)
        _items = []
        if self.markers:
            for _item in self.markers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['markers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pages (list)
        _items = []
        if self.pages:
            for _item in self.pages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebTransactionPageDetailTestResult from a dict"""
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
            "componentErrors": obj.get("componentErrors"),
            "transactionTime": obj.get("transactionTime"),
            "errorType": obj.get("errorType"),
            "errorDetails": obj.get("errorDetails"),
            "markers": [Marker.from_dict(_item) for _item in obj["markers"]] if obj.get("markers") is not None else None,
            "pages": [Page.from_dict(_item) for _item in obj["pages"]] if obj.get("pages") is not None else None,
            "har": obj.get("har")
        })
        return _obj


