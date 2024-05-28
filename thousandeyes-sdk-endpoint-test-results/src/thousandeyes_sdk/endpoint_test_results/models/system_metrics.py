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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from thousandeyes_sdk.endpoint_test_results.models.cpu_utilization import CpuUtilization
from thousandeyes_sdk.endpoint_test_results.models.physical_memory_used_bytes import PhysicalMemoryUsedBytes
from typing import Optional, Set
from typing_extensions import Self

class SystemMetrics(BaseModel):
    """
    SystemMetrics
    """ # noqa: E501
    start_time_ms: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The start time of metrics collection, expressed in milliseconds since the Epoch.", alias="startTimeMs")
    end_time_ms: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The end time of metrics collection, expressed in milliseconds since the Epoch.", alias="endTimeMs")
    cpu_utilization: Optional[CpuUtilization] = Field(default=None, alias="cpuUtilization")
    physical_memory_used_bytes: Optional[PhysicalMemoryUsedBytes] = Field(default=None, alias="physicalMemoryUsedBytes")
    physical_memory_total_bytes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total physical memory of the system.", alias="physicalMemoryTotalBytes")
    __properties: ClassVar[List[str]] = ["startTimeMs", "endTimeMs", "cpuUtilization", "physicalMemoryUsedBytes", "physicalMemoryTotalBytes"]

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
        """Create an instance of SystemMetrics from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "start_time_ms",
            "end_time_ms",
            "physical_memory_total_bytes",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cpu_utilization
        if self.cpu_utilization:
            _dict['cpuUtilization'] = self.cpu_utilization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of physical_memory_used_bytes
        if self.physical_memory_used_bytes:
            _dict['physicalMemoryUsedBytes'] = self.physical_memory_used_bytes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startTimeMs": obj.get("startTimeMs"),
            "endTimeMs": obj.get("endTimeMs"),
            "cpuUtilization": CpuUtilization.from_dict(obj["cpuUtilization"]) if obj.get("cpuUtilization") is not None else None,
            "physicalMemoryUsedBytes": PhysicalMemoryUsedBytes.from_dict(obj["physicalMemoryUsedBytes"]) if obj.get("physicalMemoryUsedBytes") is not None else None,
            "physicalMemoryTotalBytes": obj.get("physicalMemoryTotalBytes")
        })
        return _obj

