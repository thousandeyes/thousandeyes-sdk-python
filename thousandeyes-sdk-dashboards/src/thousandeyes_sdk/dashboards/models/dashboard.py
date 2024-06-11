# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.dashboards.models.api_widget import ApiWidget
from thousandeyes_sdk.dashboards.models.dashboard_links import DashboardLinks
from thousandeyes_sdk.dashboards.models.default_timespan import DefaultTimespan
from typing import Optional, Set
from typing_extensions import Self

class Dashboard(BaseModel):
    """
    Dashboard upon which this dashboard snapshot is based upon.
    """ # noqa: E501
    global_filter_id: Optional[StrictStr] = Field(default=None, description="Default global dashboard filter ID (obtained from `/dashboards/filters` endpoint).", alias="globalFilterId")
    dashboard_id: Optional[StrictStr] = Field(default=None, description="Identifier of a dashboard.", alias="dashboardId")
    title: Optional[StrictStr] = Field(default=None, description="Title of a dashboard.")
    is_built_in: Optional[StrictBool] = Field(default=None, description="Indicates if a dashboard is built-in. True for built-in dashboards, false for user-created dashboards.", alias="isBuiltIn")
    aid: Optional[StrictStr] = Field(default=None, description="Identifier for the account group associated with a dashboard.")
    created_by: Optional[StrictStr] = Field(default=None, description="Identifier for the user that created a dashboard.", alias="createdBy")
    modified_by: Optional[StrictStr] = Field(default=None, description="Identifier for the user that last modified a dashboard.", alias="modifiedBy")
    modified_date: Optional[datetime] = Field(default=None, description="UTC date/time when a dashboard was last modified (ISO date-time format).", alias="modifiedDate")
    is_private: Optional[StrictBool] = Field(default=None, description="A dashboard can be viewed by other users in the account. If true, only the creator of the dashboard may view it. If false, all users in the same account may view it.", alias="isPrivate")
    is_default_for_user: Optional[StrictBool] = Field(default=None, description="Indicates whether this dashboard is the user's default. True for default, false if not.", alias="isDefaultForUser")
    is_default_for_account: Optional[StrictBool] = Field(default=None, description="Indicates whether this dashboard is the account group's default. True for default, false if not.", alias="isDefaultForAccount")
    widgets: Optional[List[ApiWidget]] = None
    description: Optional[StrictStr] = Field(default=None, description="A text description of the dashboard's purpose and functionality. This information assists users in understanding the dashboard but isn't displayed when viewing a dashboard.")
    default_timespan: Optional[DefaultTimespan] = Field(default=None, alias="defaultTimespan")
    is_global_override: Optional[StrictBool] = Field(default=None, description="When set to `true`, the defaultTimespan is used and overrides the widget's timespan. If set to `false`, the the widget's timespan is used.", alias="isGlobalOverride")
    is_migrated_report: Optional[StrictBool] = Field(default=None, description="True if this dashboard was previously a report.", alias="isMigratedReport")
    links: Optional[DashboardLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["globalFilterId", "dashboardId", "title", "isBuiltIn", "aid", "createdBy", "modifiedBy", "modifiedDate", "isPrivate", "isDefaultForUser", "isDefaultForAccount", "widgets", "description", "defaultTimespan", "isGlobalOverride", "isMigratedReport", "_links"]

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
        """Create an instance of Dashboard from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "dashboard_id",
            "is_built_in",
            "aid",
            "created_by",
            "modified_by",
            "modified_date",
            "is_default_for_user",
            "is_default_for_account",
            "is_migrated_report",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in widgets (list)
        _items = []
        if self.widgets:
            for _item in self.widgets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['widgets'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_timespan
        if self.default_timespan:
            _dict['defaultTimespan'] = self.default_timespan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dashboard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "globalFilterId": obj.get("globalFilterId"),
            "dashboardId": obj.get("dashboardId"),
            "title": obj.get("title"),
            "isBuiltIn": obj.get("isBuiltIn"),
            "aid": obj.get("aid"),
            "createdBy": obj.get("createdBy"),
            "modifiedBy": obj.get("modifiedBy"),
            "modifiedDate": obj.get("modifiedDate"),
            "isPrivate": obj.get("isPrivate"),
            "isDefaultForUser": obj.get("isDefaultForUser"),
            "isDefaultForAccount": obj.get("isDefaultForAccount"),
            "widgets": [ApiWidget.from_dict(_item) for _item in obj["widgets"]] if obj.get("widgets") is not None else None,
            "description": obj.get("description"),
            "defaultTimespan": DefaultTimespan.from_dict(obj["defaultTimespan"]) if obj.get("defaultTimespan") is not None else None,
            "isGlobalOverride": obj.get("isGlobalOverride"),
            "isMigratedReport": obj.get("isMigratedReport"),
            "_links": DashboardLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


