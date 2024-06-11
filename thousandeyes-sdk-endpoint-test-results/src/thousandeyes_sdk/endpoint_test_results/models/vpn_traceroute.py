# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.traceroute_hop import TracerouteHop
from typing import Optional, Set
from typing_extensions import Self

class VpnTraceroute(BaseModel):
    """
    VpnTraceroute
    """ # noqa: E501
    destination: Optional[StrictStr] = Field(default=None, description="The target IP address.")
    error: Optional[StrictStr] = Field(default=None, description="Only present when there is an error")
    info_flags: Optional[List[StrictStr]] = Field(default=None, alias="infoFlags")
    internal_errors: Optional[List[StrictStr]] = Field(default=None, alias="internalErrors")
    hops: Optional[List[TracerouteHop]] = None
    __properties: ClassVar[List[str]] = ["destination", "error", "infoFlags", "internalErrors", "hops"]

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
        """Create an instance of VpnTraceroute from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "destination",
            "error",
            "info_flags",
            "internal_errors",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in hops (list)
        _items = []
        if self.hops:
            for _item in self.hops:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hops'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VpnTraceroute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination": obj.get("destination"),
            "error": obj.get("error"),
            "infoFlags": obj.get("infoFlags"),
            "internalErrors": obj.get("internalErrors"),
            "hops": [TracerouteHop.from_dict(_item) for _item in obj["hops"]] if obj.get("hops") is not None else None
        })
        return _obj


