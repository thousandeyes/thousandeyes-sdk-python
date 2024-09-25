# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.alerts.models.alert_links import AlertLinks
from thousandeyes_sdk.alerts.models.alert_meta import AlertMeta
from thousandeyes_sdk.alerts.models.alert_type import AlertType
from thousandeyes_sdk.alerts.models.severity import Severity
from thousandeyes_sdk.alerts.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class Alert(BaseModel):
    """
    Alert
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="A unique ID for each individual alert occurrence.")
    alert_type: Optional[AlertType] = Field(default=None, alias="alertType")
    start_date: Optional[datetime] = Field(default=None, description="(Optional) When passing `window` or `startDate` parameter,  the client will also receive the `startDate` field indicating the UTC start date of the data's time range being retrieved  (ISO date-time format).", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="(Optional) When passing `window` or `endDate` parameter,  the client will also receive the `endDate` field indicating the UTC end date of the data's time range being retrieved  (ISO date-time format).", alias="endDate")
    violation_count: Optional[StrictInt] = Field(default=None, description="Number of sources that meet the alert criteria.", alias="violationCount")
    duration: Optional[StrictInt] = Field(default=None, description="Duration in seconds the alert was active")
    suppressed: Optional[StrictBool] = Field(default=None, description="Indicates whether the alert is currently suppressed by a real-time ASW.")
    meta: Optional[AlertMeta] = None
    links: Optional[AlertLinks] = Field(default=None, alias="_links")
    alert_id: Optional[StrictStr] = Field(default=None, description="A unique ID for each individual alert occurrence.", alias="alertId")
    date_start: Optional[StrictStr] = Field(default=None, description="The start date and time for querying alerts.", alias="dateStart")
    date_end: Optional[StrictStr] = Field(default=None, description="The end date and time for querying alerts.", alias="dateEnd")
    rule_id: Optional[StrictInt] = Field(default=None, description="Unique ID of the rule.", alias="ruleId")
    state: Optional[StrictStr] = Field(default=None, description="Current state of the alert. Possible values: clear or trigger.")
    severity: Optional[StrictStr] = Field(default=None, description="The severity of the alert.")
    permalink: Optional[StrictStr] = Field(default=None, description="Hyperlink to alerts list, with row expanded")
    api_links: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of hyperlinks to other areas of the API", alias="apiLinks")
    alert_rule_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the rule.", alias="alertRuleId")
    alert_state: Optional[State] = Field(default=None, alias="alertState")
    alert_severity: Optional[Severity] = Field(default=None, alias="alertSeverity")
    __properties: ClassVar[List[str]] = ["id", "alertType", "startDate", "endDate", "violationCount", "duration", "suppressed", "meta", "_links", "alertId", "dateStart", "dateEnd", "ruleId", "state", "severity", "permalink", "apiLinks", "alertRuleId", "alertState", "alertSeverity"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'CLEARED', 'unknown']):
            raise ValueError("must be one of enum values ('ACTIVE', 'CLEARED', 'unknown')")
        return value

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INFO', 'MAJOR', 'MINOR', 'CRITICAL', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('INFO', 'MAJOR', 'MINOR', 'CRITICAL', 'UNKNOWN')")
        return value

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
        """Create an instance of Alert from a JSON string"""
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
            "id",
            "start_date",
            "end_date",
            "alert_id",
            "date_start",
            "date_end",
            "rule_id",
            "state",
            "alert_rule_id",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Alert from a dict"""
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
            "alertId": obj.get("alertId"),
            "dateStart": obj.get("dateStart"),
            "dateEnd": obj.get("dateEnd"),
            "ruleId": obj.get("ruleId"),
            "state": obj.get("state"),
            "severity": obj.get("severity"),
            "permalink": obj.get("permalink"),
            "apiLinks": obj.get("apiLinks"),
            "alertRuleId": obj.get("alertRuleId"),
            "alertState": obj.get("alertState"),
            "alertSeverity": obj.get("alertSeverity")
        })
        return _obj


