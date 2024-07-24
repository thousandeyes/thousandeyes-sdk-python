# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.10
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
from typing import Optional, Set
from typing_extensions import Self

class GenerateDashboardSnapshotRequest(BaseModel):
    """
    Request to generate a snapshot from a dashboard.
    """ # noqa: E501
    start_date: Optional[datetime] = Field(default=None, description="Date and time to start aggregating data (ISO date-time format).", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="Date and time to end aggregating data (ISO date-time format).", alias="endDate")
    display_name: Optional[StrictStr] = Field(default=None, description="The name of the snapshot, does not have to be unique.", alias="displayName")
    dashboard_id: Optional[StrictStr] = Field(default=None, description="TheIdentifierof the dashboard to generate a snapshot from", alias="dashboardId")
    anonymize_data: Optional[StrictBool] = Field(default=None, description="Set to `true` to anonymize the data in the snapshot.", alias="anonymizeData")
    timezone: Optional[StrictStr] = Field(default=None, description="Specifies the timezone used for date and time fields.")
    expiration_date: Optional[datetime] = Field(default=None, description="Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date and adhere to the ISO date-time format.", alias="expirationDate")
    __properties: ClassVar[List[str]] = ["startDate", "endDate", "displayName", "dashboardId", "anonymizeData", "timezone", "expirationDate"]

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
        """Create an instance of GenerateDashboardSnapshotRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenerateDashboardSnapshotRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "displayName": obj.get("displayName"),
            "dashboardId": obj.get("dashboardId"),
            "anonymizeData": obj.get("anonymizeData"),
            "timezone": obj.get("timezone"),
            "expirationDate": obj.get("expirationDate")
        })
        return _obj


