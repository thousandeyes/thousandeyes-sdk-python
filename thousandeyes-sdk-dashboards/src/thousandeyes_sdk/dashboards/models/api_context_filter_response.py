# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.dashboards.models.api_dashboard_filter_user_details import ApiDashboardFilterUserDetails
from thousandeyes_sdk.dashboards.models.api_data_source_filters import ApiDataSourceFilters
from thousandeyes_sdk.dashboards.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class ApiContextFilterResponse(BaseModel):
    """
    Response containing dashboard filter settings and context details.
    """ # noqa: E501
    context: List[ApiDataSourceFilters] = Field(description="List of filters to be applied to a dashboard.")
    aid: StrictStr = Field(description="Account group ID of the filter.")
    id: StrictStr = Field(description="Unique ID of the dashboard filter.")
    name: StrictStr = Field(description="The name of the dashboard filter, this must be unique.")
    description: Optional[StrictStr] = Field(default=None, description="An optional description of the filter.")
    created_by: Optional[ApiDashboardFilterUserDetails] = Field(default=None, alias="createdBy")
    modified_date: Optional[datetime] = Field(default=None, description="Timestamp when the filter was last modified.", alias="modifiedDate")
    created_date: Optional[datetime] = Field(default=None, description="Timestamp when the filter was created.", alias="createdDate")
    modified_by: Optional[ApiDashboardFilterUserDetails] = Field(default=None, alias="modifiedBy")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["context", "aid", "id", "name", "description", "createdBy", "modifiedDate", "createdDate", "modifiedBy", "_links"]

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
        """Create an instance of ApiContextFilterResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in context (list)
        _items = []
        if self.context:
            for _item in self.context:
                if _item:
                    _items.append(_item.to_dict())
            _dict['context'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiContextFilterResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "context": [ApiDataSourceFilters.from_dict(_item) for _item in obj["context"]] if obj.get("context") is not None else None,
            "aid": obj.get("aid"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "createdBy": ApiDashboardFilterUserDetails.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "modifiedDate": obj.get("modifiedDate"),
            "createdDate": obj.get("createdDate"),
            "modifiedBy": ApiDashboardFilterUserDetails.from_dict(obj["modifiedBy"]) if obj.get("modifiedBy") is not None else None,
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


