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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PathVisEndpoint(BaseModel):
    """
    PathVisEndpoint
    """ # noqa: E501
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the hop", alias="ipAddress")
    mss: Optional[StrictInt] = Field(default=None, description="Maximum segment size in bytes")
    number_of_hops: Optional[StrictInt] = Field(default=None, description="Number of hops for path trace to destination", alias="numberOfHops")
    path_id: Optional[StrictStr] = Field(default=None, description="Unique ID of path trace", alias="pathId")
    path_mtu: Optional[StrictInt] = Field(default=None, description="MTU sizes on network from agents to the target", alias="pathMtu")
    response_time: Optional[StrictInt] = Field(default=None, description="RTT of the path trace to the destination in milliseconds", alias="responseTime")
    __properties: ClassVar[List[str]] = ["ipAddress", "mss", "numberOfHops", "pathId", "pathMtu", "responseTime"]

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
        """Create an instance of PathVisEndpoint from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "ip_address",
            "mss",
            "number_of_hops",
            "path_id",
            "path_mtu",
            "response_time",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathVisEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipAddress": obj.get("ipAddress"),
            "mss": obj.get("mss"),
            "numberOfHops": obj.get("numberOfHops"),
            "pathId": obj.get("pathId"),
            "pathMtu": obj.get("pathMtu"),
            "responseTime": obj.get("responseTime")
        })
        return _obj


