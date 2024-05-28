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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PathVisHop(BaseModel):
    """
    PathVisHop
    """ # noqa: E501
    hop: Optional[StrictInt] = Field(default=None, description="The hop index.")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the hop.", alias="ipAddress")
    prefix: Optional[StrictStr] = Field(default=None, description="Prefix of IP address shown in CIDR.")
    rdns: Optional[StrictStr] = Field(default=None, description="Reverse DNS entry of IP, if available.")
    network: Optional[StrictStr] = Field(default=None, description="Autonomous System originating the prefix.")
    response_time: Optional[StrictInt] = Field(default=None, description="RTT to the hop’s IP in milliseconds.", alias="responseTime")
    location: Optional[StrictStr] = Field(default=None, description="Location information for the hop.")
    __properties: ClassVar[List[str]] = ["hop", "ipAddress", "prefix", "rdns", "network", "responseTime", "location"]

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
        """Create an instance of PathVisHop from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "hop",
            "ip_address",
            "prefix",
            "rdns",
            "network",
            "response_time",
            "location",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathVisHop from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hop": obj.get("hop"),
            "ipAddress": obj.get("ipAddress"),
            "prefix": obj.get("prefix"),
            "rdns": obj.get("rdns"),
            "network": obj.get("network"),
            "responseTime": obj.get("responseTime"),
            "location": obj.get("location")
        })
        return _obj

