# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

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
from thousandeyes_sdk.alerts.models.alert_suppression_window_state import AlertSuppressionWindowState
from thousandeyes_sdk.alerts.models.base_test import BaseTest
from thousandeyes_sdk.alerts.models.end_repeat import EndRepeat
from thousandeyes_sdk.alerts.models.repeat import Repeat
from thousandeyes_sdk.alerts.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class AlertSuppressionWindowDetail(BaseModel):
    """
    AlertSuppressionWindowDetail
    """ # noqa: E501
    alert_suppression_window_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the alert suppression window.", alias="alertSuppressionWindowId")
    name: Optional[StrictStr] = Field(default=None, description="Name of the alert suppression window.")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Set to `false` for `disabled`, `true` for `enabled`.", alias="isEnabled")
    status: Optional[AlertSuppressionWindowState] = None
    start_date: Optional[datetime] = Field(default=None, description="The date/time when the alert suppression window starts (ISO date-time format).", alias="startDate")
    duration: Optional[StrictInt] = Field(default=None, description="Duration in seconds the suppression window is active.")
    repeat: Optional[Repeat] = None
    end_repeat: Optional[EndRepeat] = Field(default=None, alias="endRepeat")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    tests: Optional[List[BaseTest]] = Field(default=None, description="List of tests assigned to the alert suppression window.")
    __properties: ClassVar[List[str]] = ["alertSuppressionWindowId", "name", "isEnabled", "status", "startDate", "duration", "repeat", "endRepeat", "_links", "tests"]

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
        """Create an instance of AlertSuppressionWindowDetail from a JSON string"""
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
            "alert_suppression_window_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of repeat
        if self.repeat:
            _dict['repeat'] = self.repeat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_repeat
        if self.end_repeat:
            _dict['endRepeat'] = self.end_repeat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tests (list)
        _items = []
        if self.tests:
            for _item in self.tests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlertSuppressionWindowDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertSuppressionWindowId": obj.get("alertSuppressionWindowId"),
            "name": obj.get("name"),
            "isEnabled": obj.get("isEnabled"),
            "status": obj.get("status"),
            "startDate": obj.get("startDate"),
            "duration": obj.get("duration"),
            "repeat": Repeat.from_dict(obj["repeat"]) if obj.get("repeat") is not None else None,
            "endRepeat": EndRepeat.from_dict(obj["endRepeat"]) if obj.get("endRepeat") is not None else None,
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "tests": [BaseTest.from_dict(_item) for _item in obj["tests"]] if obj.get("tests") is not None else None
        })
        return _obj

