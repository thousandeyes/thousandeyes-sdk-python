# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
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
from thousandeyes_sdk.test_results.models.bgp_hop import BgpHop
from thousandeyes_sdk.test_results.models.monitor import Monitor
from thousandeyes_sdk.test_results.models.test_result_app_links import TestResultAppLinks
from typing import Optional, Set
from typing_extensions import Self

class BgpTestRouteInformationResult(BaseModel):
    """
    BgpTestRouteInformationResult
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Data point date UTC (ISO date-time format).", alias="date")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="roundId")
    links: Optional[TestResultAppLinks] = Field(default=None, alias="_links")
    monitor: Optional[Monitor] = None
    prefix_id: Optional[StrictStr] = Field(default=None, description="Internally tracked prefix ID.", alias="prefixId")
    prefix: Optional[StrictStr] = Field(default=None, description="Prefix being tracked.")
    is_active: Optional[StrictBool] = Field(default=None, description="Represents whether the route is active or inactive. An inactive route was an active route in the previous test round and is now superseded by another active (preferred) route. When requesting data for the test round in which a route change happened, both routes (active and inactive one) are included in the response.", alias="isActive")
    hops: Optional[List[BgpHop]] = None
    __properties: ClassVar[List[str]] = ["date", "roundId", "_links", "monitor", "prefixId", "prefix", "isActive", "hops"]

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
        """Create an instance of BgpTestRouteInformationResult from a JSON string"""
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
            "var_date",
            "round_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of monitor
        if self.monitor:
            _dict['monitor'] = self.monitor.to_dict()
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
        """Create an instance of BgpTestRouteInformationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "roundId": obj.get("roundId"),
            "_links": TestResultAppLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "monitor": Monitor.from_dict(obj["monitor"]) if obj.get("monitor") is not None else None,
            "prefixId": obj.get("prefixId"),
            "prefix": obj.get("prefix"),
            "isActive": obj.get("isActive"),
            "hops": [BgpHop.from_dict(_item) for _item in obj["hops"]] if obj.get("hops") is not None else None
        })
        return _obj

