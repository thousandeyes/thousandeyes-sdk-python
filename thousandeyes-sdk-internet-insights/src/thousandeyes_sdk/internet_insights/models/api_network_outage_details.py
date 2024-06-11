# coding: utf-8

"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows.  For more information about Internet Insights, see the [Internet Insights](https://docs.thousandeyes.com/product-documentation/internet-insights). 

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.internet_insights.models.api_affected_agent import ApiAffectedAgent
from thousandeyes_sdk.internet_insights.models.api_affected_test import ApiAffectedTest
from thousandeyes_sdk.internet_insights.models.api_network_outage_affected_location import ApiNetworkOutageAffectedLocation
from thousandeyes_sdk.internet_insights.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class ApiNetworkOutageDetails(BaseModel):
    """
    ApiNetworkOutageDetails
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The ID of the outage.")
    provider_name: Optional[StrictStr] = Field(default=None, description="The name of the affected provider.", alias="providerName")
    provider_type: Optional[StrictStr] = Field(default=None, description="The type of the affected provider.", alias="providerType")
    network_name: Optional[StrictStr] = Field(default=None, description="The affected network.", alias="networkName")
    asn: Optional[StrictInt] = Field(default=None, description="ASN number")
    start_date: Optional[StrictStr] = Field(default=None, description="Date and time when the outage started.", alias="startDate")
    start_round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) when the outage started.", alias="startRoundId")
    end_date: Optional[StrictStr] = Field(default=None, description="Date and time when the outage ended.", alias="endDate")
    end_round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) when the outage ended.", alias="endRoundId")
    duration: Optional[StrictInt] = Field(default=None, description="Duration of the outage in seconds.")
    affected_tests: Optional[List[ApiAffectedTest]] = Field(default=None, description="List of affected tests.", alias="affectedTests")
    affected_domains: Optional[List[StrictStr]] = Field(default=None, description="List of affected domains.", alias="affectedDomains")
    affected_agents: Optional[List[ApiAffectedAgent]] = Field(default=None, description="List of affected agents.", alias="affectedAgents")
    affected_locations: Optional[List[ApiNetworkOutageAffectedLocation]] = Field(default=None, description="List of affected locations.", alias="affectedLocations")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "providerName", "providerType", "networkName", "asn", "startDate", "startRoundId", "endDate", "endRoundId", "duration", "affectedTests", "affectedDomains", "affectedAgents", "affectedLocations", "_links"]

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
        """Create an instance of ApiNetworkOutageDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in affected_tests (list)
        _items = []
        if self.affected_tests:
            for _item in self.affected_tests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['affectedTests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in affected_agents (list)
        _items = []
        if self.affected_agents:
            for _item in self.affected_agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['affectedAgents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in affected_locations (list)
        _items = []
        if self.affected_locations:
            for _item in self.affected_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['affectedLocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiNetworkOutageDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "providerName": obj.get("providerName"),
            "providerType": obj.get("providerType"),
            "networkName": obj.get("networkName"),
            "asn": obj.get("asn"),
            "startDate": obj.get("startDate"),
            "startRoundId": obj.get("startRoundId"),
            "endDate": obj.get("endDate"),
            "endRoundId": obj.get("endRoundId"),
            "duration": obj.get("duration"),
            "affectedTests": [ApiAffectedTest.from_dict(_item) for _item in obj["affectedTests"]] if obj.get("affectedTests") is not None else None,
            "affectedDomains": obj.get("affectedDomains"),
            "affectedAgents": [ApiAffectedAgent.from_dict(_item) for _item in obj["affectedAgents"]] if obj.get("affectedAgents") is not None else None,
            "affectedLocations": [ApiNetworkOutageAffectedLocation.from_dict(_item) for _item in obj["affectedLocations"]] if obj.get("affectedLocations") is not None else None,
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


