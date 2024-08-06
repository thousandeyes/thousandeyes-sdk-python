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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.dashboards.models.api_dashboard_asw import ApiDashboardAsw
from thousandeyes_sdk.dashboards.models.api_widget_data_point import ApiWidgetDataPoint
from typing import Optional, Set
from typing_extensions import Self

class ApiMultiMetricColumnData(BaseModel):
    """
    The data presented within a single column of a Multi-Metric table.
    """ # noqa: E501
    column_id: Optional[StrictStr] = Field(default=None, description="Identifier of the column.", alias="columnId")
    bin_size: Optional[StrictInt] = Field(default=None, description="Duration of each bin.", alias="binSize")
    points: Optional[List[ApiWidgetDataPoint]] = None
    status: Optional[StrictStr] = Field(default=None, description="Message for not fully configured card or no data.")
    alert_suppression_windows: Optional[List[ApiDashboardAsw]] = Field(default=None, alias="alertSuppressionWindows")
    __properties: ClassVar[List[str]] = ["columnId", "binSize", "points", "status", "alertSuppressionWindows"]

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
        """Create an instance of ApiMultiMetricColumnData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in points (list)
        _items = []
        if self.points:
            for _item in self.points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['points'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in alert_suppression_windows (list)
        _items = []
        if self.alert_suppression_windows:
            for _item in self.alert_suppression_windows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alertSuppressionWindows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiMultiMetricColumnData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "columnId": obj.get("columnId"),
            "binSize": obj.get("binSize"),
            "points": [ApiWidgetDataPoint.from_dict(_item) for _item in obj["points"]] if obj.get("points") is not None else None,
            "status": obj.get("status"),
            "alertSuppressionWindows": [ApiDashboardAsw.from_dict(_item) for _item in obj["alertSuppressionWindows"]] if obj.get("alertSuppressionWindows") is not None else None
        })
        return _obj


