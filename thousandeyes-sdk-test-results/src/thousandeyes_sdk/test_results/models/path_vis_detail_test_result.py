# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.test_results.models.path_vis_direction import PathVisDirection
from thousandeyes_sdk.test_results.models.path_vis_route import PathVisRoute
from thousandeyes_sdk.test_results.models.test_result_agent import TestResultAgent
from thousandeyes_sdk.test_results.models.test_result_app_links import TestResultAppLinks
from typing import Optional, Set
from typing_extensions import Self

class PathVisDetailTestResult(BaseModel):
    """
    PathVisDetailTestResult
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Data point date UTC (ISO date-time format).", alias="date")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="roundId")
    links: Optional[TestResultAppLinks] = Field(default=None, alias="_links")
    start_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="startTime")
    end_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the end time of the round", alias="endTime")
    agent: Optional[TestResultAgent] = None
    server: Optional[StrictStr] = Field(default=None, description="Target server, including port (if method used is TCP)")
    server_ip: Optional[StrictStr] = Field(default=None, description="IP of target server", alias="serverIp")
    source_ip: Optional[StrictStr] = Field(default=None, description="IP address of source agent", alias="sourceIp")
    source_prefix: Optional[StrictStr] = Field(default=None, description="IP prefix of source agent", alias="sourcePrefix")
    target_is_proxy: Optional[StrictBool] = Field(default=None, description="Specifies whether the traces are targeting a proxy. If not set, it is considered as false.", alias="targetIsProxy")
    direction: Optional[PathVisDirection] = None
    path_traces: Optional[List[PathVisRoute]] = Field(default=None, description="Shows 3 iterations of path trace, with each iteration specified by a pathId", alias="pathTraces")
    __properties: ClassVar[List[str]] = ["date", "roundId", "_links", "startTime", "endTime", "agent", "server", "serverIp", "sourceIp", "sourcePrefix", "targetIsProxy", "direction", "pathTraces"]

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
        """Create an instance of PathVisDetailTestResult from a JSON string"""
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
            "server",
            "server_ip",
            "source_ip",
            "source_prefix",
            "target_is_proxy",
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
        """Create an instance of PathVisDetailTestResult from a dict"""
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
            "agent": TestResultAgent.from_dict(obj["agent"]) if obj.get("agent") is not None else None,
            "server": obj.get("server"),
            "serverIp": obj.get("serverIp"),
            "sourceIp": obj.get("sourceIp"),
            "sourcePrefix": obj.get("sourcePrefix"),
            "targetIsProxy": obj.get("targetIsProxy"),
            "direction": obj.get("direction"),
            "pathTraces": [PathVisRoute.from_dict(_item) for _item in obj["pathTraces"]] if obj.get("pathTraces") is not None else None
        })
        return _obj


