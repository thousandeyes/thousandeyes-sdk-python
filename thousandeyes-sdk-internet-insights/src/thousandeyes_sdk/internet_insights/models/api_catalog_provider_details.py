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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.internet_insights.models.api_asn import ApiAsn
from thousandeyes_sdk.internet_insights.models.provider_location import ProviderLocation
from thousandeyes_sdk.internet_insights.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class ApiCatalogProviderDetails(BaseModel):
    """
    ApiCatalogProviderDetails
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The catalog provider ID.")
    provider_name: Optional[StrictStr] = Field(default=None, description="The name of the catalog provider.", alias="providerName")
    provider_type: Optional[StrictStr] = Field(default=None, description="The type of catalog provider.", alias="providerType")
    region: Optional[StrictStr] = Field(default=None, description="The catalog provider region.")
    data_type: Optional[StrictStr] = Field(default=None, description="The type of data produced by the provider.", alias="dataType")
    asns: Optional[List[ApiAsn]] = Field(default=None, description="List of ASN's covered by the Provider.")
    locations: Optional[List[ProviderLocation]] = Field(default=None, description="List of locations covered by the Provider.")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "providerName", "providerType", "region", "dataType", "asns", "locations", "_links"]

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
        """Create an instance of ApiCatalogProviderDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in asns (list)
        _items = []
        if self.asns:
            for _item in self.asns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['asns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiCatalogProviderDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "providerName": obj.get("providerName"),
            "providerType": obj.get("providerType"),
            "region": obj.get("region"),
            "dataType": obj.get("dataType"),
            "asns": [ApiAsn.from_dict(_item) for _item in obj["asns"]] if obj.get("asns") is not None else None,
            "locations": [ProviderLocation.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


