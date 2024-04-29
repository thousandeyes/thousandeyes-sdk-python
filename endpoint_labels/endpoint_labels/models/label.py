# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from endpoint_labels.models.filter import Filter
from endpoint_labels.models.match_type import MatchType
from typing import Optional, Set
from typing_extensions import Self

class Label(BaseModel):
    """
    A label definition.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Label identifier.")
    name: Optional[StrictStr] = Field(default=None, description="The label name.")
    color: Optional[StrictStr] = Field(default=None, description="UI color")
    match_type: Optional[MatchType] = Field(default=None, alias="matchType")
    filters: Optional[List[Filter]] = Field(default=None, description="The filters combined using the matchType to determine the label's match.")
    __properties: ClassVar[List[str]] = ["id", "name", "color", "matchType", "filters"]

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
        """Create an instance of Label from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Label from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "color": obj.get("color"),
            "matchType": obj.get("matchType"),
            "filters": [Filter.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None
        })
        return _obj

