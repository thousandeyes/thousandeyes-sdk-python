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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class InterfaceGroup(BaseModel):
    """
    InterfaceGroup
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="Account Group Id")
    group_id: Optional[StrictStr] = Field(default=None, description="Group ID", alias="groupId")
    group_name: Optional[StrictStr] = Field(default=None, description="Name of the path visualization interface group", alias="groupName")
    ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of IP addresses associated with the interface group", alias="ipAddresses")
    rdns_regexes: Optional[List[StrictStr]] = Field(default=None, description="Array of RDNS Regexes associated with the interface group", alias="rdnsRegexes")
    __properties: ClassVar[List[str]] = ["aid", "groupId", "groupName", "ipAddresses", "rdnsRegexes"]

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
        """Create an instance of InterfaceGroup from a JSON string"""
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
            "aid",
            "group_id",
            "rdns_regexes",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InterfaceGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "groupId": obj.get("groupId"),
            "groupName": obj.get("groupName"),
            "ipAddresses": obj.get("ipAddresses"),
            "rdnsRegexes": obj.get("rdnsRegexes")
        })
        return _obj


