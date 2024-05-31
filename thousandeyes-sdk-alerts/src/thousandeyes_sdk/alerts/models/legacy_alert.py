# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LegacyAlert(BaseModel):
    """
    LegacyAlert
    """ # noqa: E501
    alert_id: Optional[StrictStr] = Field(default=None, description="A unique ID for each individual alert occurrence.", alias="alertId")
    date_start: Optional[StrictStr] = Field(default=None, description="The start date and time for querying alerts.", alias="dateStart")
    date_end: Optional[StrictStr] = Field(default=None, description="The end date and time for querying alerts.", alias="dateEnd")
    rule_id: Optional[StrictInt] = Field(default=None, description="Unique ID of the rule.", alias="ruleId")
    state: Optional[StrictStr] = Field(default=None, description="Current state of the alert. Possible values: clear or trigger.")
    severity: Optional[StrictStr] = Field(default=None, description="The severity of the alert.")
    permalink: Optional[StrictStr] = Field(default=None, description="Hyperlink to alerts list, with row expanded")
    api_links: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of hyperlinks to other areas of the API", alias="apiLinks")
    __properties: ClassVar[List[str]] = ["alertId", "dateStart", "dateEnd", "ruleId", "state", "severity", "permalink", "apiLinks"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'CLEARED']):
            raise ValueError("must be one of enum values ('ACTIVE', 'CLEARED')")
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
        """Create an instance of LegacyAlert from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "alert_id",
            "date_start",
            "date_end",
            "rule_id",
            "state",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LegacyAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertId": obj.get("alertId"),
            "dateStart": obj.get("dateStart"),
            "dateEnd": obj.get("dateEnd"),
            "ruleId": obj.get("ruleId"),
            "state": obj.get("state"),
            "severity": obj.get("severity"),
            "permalink": obj.get("permalink"),
            "apiLinks": obj.get("apiLinks")
        })
        return _obj


