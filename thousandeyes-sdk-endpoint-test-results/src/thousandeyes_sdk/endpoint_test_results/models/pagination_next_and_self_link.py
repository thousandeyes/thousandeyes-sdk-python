# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.link import Link
from typing import Optional, Set
from typing_extensions import Self

class PaginationNextAndSelfLink(BaseModel):
    """
    A links object containing a related link for forward pagination.
    """ # noqa: E501
    next: Optional[Link] = None
    var_self: Optional[Link] = Field(default=None, alias="self")
    __properties: ClassVar[List[str]] = ["next", "self"]

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
        """Create an instance of PaginationNextAndSelfLink from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of next
        if self.next:
            _dict['next'] = self.next.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginationNextAndSelfLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "next": Link.from_dict(obj["next"]) if obj.get("next") is not None else None,
            "self": Link.from_dict(obj["self"]) if obj.get("self") is not None else None
        })
        return _obj


