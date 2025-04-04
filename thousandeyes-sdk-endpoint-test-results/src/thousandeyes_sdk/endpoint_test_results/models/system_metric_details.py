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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.application_metrics import ApplicationMetrics
from typing import Optional, Set
from typing_extensions import Self

class SystemMetricDetails(BaseModel):
    """
    Details of system metrics that contain top applications by CPU/memory usage. Not populated by default. 
    """ # noqa: E501
    top_cpu_applications: Optional[List[ApplicationMetrics]] = Field(default=None, description="A list of applications that consume more than 2% of the CPU.", alias="topCpuApplications")
    top_memory_applications: Optional[List[ApplicationMetrics]] = Field(default=None, description="A list of applications that consume more than 2% of the RAM.", alias="topMemoryApplications")
    __properties: ClassVar[List[str]] = ["topCpuApplications", "topMemoryApplications"]

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
        """Create an instance of SystemMetricDetails from a JSON string"""
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
            "top_cpu_applications",
            "top_memory_applications",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in top_cpu_applications (list)
        _items = []
        if self.top_cpu_applications:
            for _item in self.top_cpu_applications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['topCpuApplications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in top_memory_applications (list)
        _items = []
        if self.top_memory_applications:
            for _item in self.top_memory_applications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['topMemoryApplications'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemMetricDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "topCpuApplications": [ApplicationMetrics.from_dict(_item) for _item in obj["topCpuApplications"]] if obj.get("topCpuApplications") is not None else None,
            "topMemoryApplications": [ApplicationMetrics.from_dict(_item) for _item in obj["topMemoryApplications"]] if obj.get("topMemoryApplications") is not None else None
        })
        return _obj


