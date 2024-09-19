# coding: utf-8

"""
    Event Detection API

     Event detection occurs when ThousandEyes identifies that error signals related to a component (proxy, network node, AS, server etc) have deviated from the baselines established by events. * To determine this, ThousandEyes takes the test results from all accounts groups within an organization, and analyzes that data. * Noisy test results (those that have too many errors in a short window) are removed until they stabilize, and the rest of the results are tagged with the components associated with that test result (for example, proxy, network, or server). * Next, any increase in failures from the test results and each component helps in determining the problem domain and which component may be at fault. * When this failure rate increases beyond a pre-defined threshold (set by the algorithm), an event is triggered and an email notification is sent to the user (if they've enabled email alerts).  With the Events API, you can perform the following tasks on the ThousandEyes platform: * **Retrieve Events**: Obtain a list of events and detailed information for each event. For more information about events, see [Event Detection](https://docs.thousandeyes.com/product-documentation/event-detection). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.event_detection.models.affected_agents import AffectedAgents
from thousandeyes_sdk.event_detection.models.affected_targets import AffectedTargets
from thousandeyes_sdk.event_detection.models.affected_tests import AffectedTests
from thousandeyes_sdk.event_detection.models.event_alert_severity import EventAlertSeverity
from thousandeyes_sdk.event_detection.models.event_state import EventState
from thousandeyes_sdk.event_detection.models.network_event_grouping import NetworkEventGrouping
from thousandeyes_sdk.event_detection.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class NetworkPopEventDetail(BaseModel):
    """
    NetworkPopEventDetail
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="A unique ID for each event.")
    type_name: Optional[StrictStr] = Field(default=None, description="Event type name. Examples include, Local Agent Issue, Network Path Issue, Network Outage, DNS Issue, Server Issue, and Proxy Issue.", alias="typeName")
    state: Optional[EventState] = None
    start_date: Optional[datetime] = Field(default=None, description="The start date and time (in UTC, ISO 8601 format) when the event was first detected.", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="The end date and time (in UTC, ISO 8601 format) when the event was resolved (due to timeout). This value is populated for \"ongoing\" events.", alias="endDate")
    severity: Optional[EventAlertSeverity] = None
    aid: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint.")
    summary: Optional[StrictStr] = Field(default=None, description="A brief summary describing the cause of the event.")
    affected_tests: Optional[AffectedTests] = Field(default=None, alias="affectedTests")
    affected_targets: Optional[AffectedTargets] = Field(default=None, alias="affectedTargets")
    affected_agents: Optional[AffectedAgents] = Field(default=None, alias="affectedAgents")
    cause: Optional[List[StrictStr]] = Field(default=None, description="The cause of the error.")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    type: Annotated[str, Field(strict=True)] = Field(description="Network pop event type.")
    grouping: Optional[NetworkEventGrouping] = None
    __properties: ClassVar[List[str]] = ["id", "typeName", "state", "startDate", "endDate", "severity", "aid", "summary", "affectedTests", "affectedTargets", "affectedAgents", "cause", "_links", "type", "grouping"]

    @field_validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^network-pop$", value):
            raise ValueError(r"must validate the regular expression /^network-pop$/")
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
        """Create an instance of NetworkPopEventDetail from a JSON string"""
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
            "id",
            "type_name",
            "start_date",
            "end_date",
            "summary",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of affected_tests
        if self.affected_tests:
            _dict['affectedTests'] = self.affected_tests.to_dict()
        # override the default output from pydantic by calling `to_dict()` of affected_targets
        if self.affected_targets:
            _dict['affectedTargets'] = self.affected_targets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of affected_agents
        if self.affected_agents:
            _dict['affectedAgents'] = self.affected_agents.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grouping
        if self.grouping:
            _dict['grouping'] = self.grouping.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkPopEventDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "typeName": obj.get("typeName"),
            "state": obj.get("state"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "severity": obj.get("severity"),
            "aid": obj.get("aid"),
            "summary": obj.get("summary"),
            "affectedTests": AffectedTests.from_dict(obj["affectedTests"]) if obj.get("affectedTests") is not None else None,
            "affectedTargets": AffectedTargets.from_dict(obj["affectedTargets"]) if obj.get("affectedTargets") is not None else None,
            "affectedAgents": AffectedAgents.from_dict(obj["affectedAgents"]) if obj.get("affectedAgents") is not None else None,
            "cause": obj.get("cause"),
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "type": obj.get("type"),
            "grouping": NetworkEventGrouping.from_dict(obj["grouping"]) if obj.get("grouping") is not None else None
        })
        return _obj


