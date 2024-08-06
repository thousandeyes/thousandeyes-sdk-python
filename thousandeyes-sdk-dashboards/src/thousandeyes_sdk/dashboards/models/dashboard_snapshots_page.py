# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.dashboards.models.api_dashboard_snapshot import ApiDashboardSnapshot
from thousandeyes_sdk.dashboards.models.pagination_links import PaginationLinks
from typing import Optional, Set
from typing_extensions import Self

class DashboardSnapshotsPage(BaseModel):
    """
    Dashboard snapshots page.
    """ # noqa: E501
    pages: Optional[Dict[str, Any]] = None
    dashboard_snapshots: Optional[List[ApiDashboardSnapshot]] = Field(default=None, alias="dashboardSnapshots")
    links: Optional[PaginationLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["pages", "dashboardSnapshots", "_links"]

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
        """Create an instance of DashboardSnapshotsPage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dashboard_snapshots (list)
        _items = []
        if self.dashboard_snapshots:
            for _item in self.dashboard_snapshots:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dashboardSnapshots'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DashboardSnapshotsPage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pages": obj.get("pages"),
            "dashboardSnapshots": [ApiDashboardSnapshot.from_dict(_item) for _item in obj["dashboardSnapshots"]] if obj.get("dashboardSnapshots") is not None else None,
            "_links": PaginationLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


