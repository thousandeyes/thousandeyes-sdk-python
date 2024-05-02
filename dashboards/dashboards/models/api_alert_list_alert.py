# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
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
from dashboards.models.alert_list_alert_type import AlertListAlertType
from typing import Optional, Set
from typing_extensions import Self

class ApiAlertListAlert(BaseModel):
    """
    Alert shown in the alert list widget.
    """ # noqa: E501
    alert_id: Optional[StrictStr] = Field(default=None, description="Identifier of the alert.", alias="alertId")
    test_id: Optional[StrictStr] = Field(default=None, description="Identifier of the test.", alias="testId")
    rule_id: Optional[StrictStr] = Field(default=None, description="Identifier of the rule.", alias="ruleId")
    alert_source: Optional[StrictStr] = Field(default=None, description="Name of the agent, monitor or device producing the alert.", alias="alertSource")
    alert_rule: Optional[StrictStr] = Field(default=None, description="Name of the alert rule that this alert belongs to.", alias="alertRule")
    alert_type: Optional[AlertListAlertType] = Field(default=None, alias="alertType")
    start_time: Optional[datetime] = Field(default=None, description="UTC date when the alert was first active.", alias="startTime")
    duration_in_seconds: Optional[StrictInt] = Field(default=None, description="Number of seconds the alert was active. If it’s still active, this number will increase every second.", alias="durationInSeconds")
    active: Optional[StrictBool] = Field(default=None, description="Set to `true` if alert is active, `false` otherwise.")
    __properties: ClassVar[List[str]] = ["alertId", "testId", "ruleId", "alertSource", "alertRule", "alertType", "startTime", "durationInSeconds", "active"]

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
        """Create an instance of ApiAlertListAlert from a JSON string"""
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
        """Create an instance of ApiAlertListAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertId": obj.get("alertId"),
            "testId": obj.get("testId"),
            "ruleId": obj.get("ruleId"),
            "alertSource": obj.get("alertSource"),
            "alertRule": obj.get("alertRule"),
            "alertType": obj.get("alertType"),
            "startTime": obj.get("startTime"),
            "durationInSeconds": obj.get("durationInSeconds"),
            "active": obj.get("active")
        })
        return _obj


