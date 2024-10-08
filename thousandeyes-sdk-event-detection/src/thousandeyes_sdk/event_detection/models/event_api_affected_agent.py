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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.event_detection.models.agent_links import AgentLinks
from thousandeyes_sdk.event_detection.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType
from typing import Optional, Set
from typing_extensions import Self

class EventApiAffectedAgent(BaseModel):
    """
    EventApiAffectedAgent
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, description="The ID of the virtual agent.", alias="agentId")
    type: Optional[CloudEnterpriseAgentType] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the agent as defined in settings.")
    location: Optional[StrictStr] = Field(default=None, description="The name of the agent's location.")
    country_code: Optional[StrictStr] = Field(default=None, description="The country code of the agent's location .", alias="countryCode")
    affected_target_ids: Optional[List[StrictStr]] = Field(default=None, description="An array of unique target IDs that contributed data points which generated the signal for the event.", alias="affectedTargetIds")
    affected_test_ids: Optional[List[StrictStr]] = Field(default=None, description="An array of unique agent IDs that contributed data points which generated the signal for the event.", alias="affectedTestIds")
    links: Optional[AgentLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["agentId", "type", "name", "location", "countryCode", "affectedTargetIds", "affectedTestIds", "_links"]

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
        """Create an instance of EventApiAffectedAgent from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "agent_id",
            "name",
            "location",
            "country_code",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventApiAffectedAgent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentId": obj.get("agentId"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "location": obj.get("location"),
            "countryCode": obj.get("countryCode"),
            "affectedTargetIds": obj.get("affectedTargetIds"),
            "affectedTestIds": obj.get("affectedTestIds"),
            "_links": AgentLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


