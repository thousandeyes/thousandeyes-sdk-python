# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.tests.models.monitor import Monitor
from typing import Optional, Set
from typing_extensions import Self

class TestMonitorsProperties(BaseModel):
    """
    TestMonitorsProperties
    """ # noqa: E501
    bgp_measurements: Optional[StrictBool] = Field(default=True, description="Set to `true` to enable bgp measurements.", alias="bgpMeasurements")
    use_public_bgp: Optional[StrictBool] = Field(default=True, description="Indicate if all available public BGP monitors should be used, when ommited defaults to `bgpMeasurements` value.", alias="usePublicBgp")
    monitors: Optional[List[Monitor]] = Field(default=None, description="Contains list of enabled BGP monitors.")
    __properties: ClassVar[List[str]] = ["bgpMeasurements", "usePublicBgp", "monitors"]

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
        """Create an instance of TestMonitorsProperties from a JSON string"""
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
            "monitors",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in monitors (list)
        _items = []
        if self.monitors:
            for _item in self.monitors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monitors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestMonitorsProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bgpMeasurements": obj.get("bgpMeasurements") if obj.get("bgpMeasurements") is not None else True,
            "usePublicBgp": obj.get("usePublicBgp") if obj.get("usePublicBgp") is not None else True,
            "monitors": [Monitor.from_dict(_item) for _item in obj["monitors"]] if obj.get("monitors") is not None else None
        })
        return _obj


