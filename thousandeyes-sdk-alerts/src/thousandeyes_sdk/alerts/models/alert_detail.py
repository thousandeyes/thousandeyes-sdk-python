# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.12
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
from thousandeyes_sdk.alerts.models.alert_links import AlertLinks
from thousandeyes_sdk.alerts.models.alert_meta import AlertMeta
from thousandeyes_sdk.alerts.models.alert_metric_detail import AlertMetricDetail
from thousandeyes_sdk.alerts.models.alert_type import AlertType
from thousandeyes_sdk.alerts.models.severity import Severity
from thousandeyes_sdk.alerts.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class AlertDetail(BaseModel):
    """
    AlertDetail
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="A unique ID for each individual alert occurrence.")
    alert_type: Optional[AlertType] = Field(default=None, alias="alertType")
    start_date: Optional[datetime] = Field(default=None, description="The start date and time (in UTC, ISO 8601 format) for querying alerts.", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="The end date and time (in UTC, ISO 8601 format) for querying alerts.", alias="endDate")
    violation_count: Optional[StrictInt] = Field(default=None, description="Number of sources that meet the alert criteria.", alias="violationCount")
    duration: Optional[StrictInt] = Field(default=None, description="Duration in seconds the alert was active")
    suppressed: Optional[StrictBool] = Field(default=None, description="Indicates whether the alert is currently suppressed by a real-time ASW.")
    meta: Optional[AlertMeta] = None
    links: Optional[AlertLinks] = Field(default=None, alias="_links")
    state: Optional[State] = None
    severity: Optional[Severity] = None
    details: Optional[List[AlertMetricDetail]] = None
    __properties: ClassVar[List[str]] = ["id", "alertType", "startDate", "endDate", "violationCount", "duration", "suppressed", "meta", "_links", "state", "severity", "details"]

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
        """Create an instance of AlertDetail from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "start_date",
            "end_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlertDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "alertType": obj.get("alertType"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "violationCount": obj.get("violationCount"),
            "duration": obj.get("duration"),
            "suppressed": obj.get("suppressed"),
            "meta": AlertMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "_links": AlertLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "state": obj.get("state"),
            "severity": obj.get("severity"),
            "details": [AlertMetricDetail.from_dict(_item) for _item in obj["details"]] if obj.get("details") is not None else None
        })
        return _obj


