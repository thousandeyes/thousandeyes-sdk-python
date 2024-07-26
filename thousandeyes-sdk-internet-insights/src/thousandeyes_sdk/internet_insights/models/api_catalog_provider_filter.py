# coding: utf-8

"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows.  For more information about Internet Insights, see the [Internet Insights](https://docs.thousandeyes.com/product-documentation/internet-insights). 

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiCatalogProviderFilter(BaseModel):
    """
    Advanced filter query used to filter the response. The provider name, location, asn can be partial names. Can filter on: - Provider name - Provider type - Region - Location - ASN - included
    """ # noqa: E501
    provider_name: Optional[StrictStr] = Field(default=None, description="The name of the catalog provider.", alias="providerName")
    provider_type: Optional[StrictStr] = Field(default=None, description="The type of catalog provider.", alias="providerType")
    region: Optional[StrictStr] = Field(default=None, description="The catalog provider region.")
    location: Optional[StrictStr] = Field(default=None, description="Location of the catalog provider.")
    asn: Optional[StrictStr] = Field(default=None, description="Name of the ASN (Autonomous Systems Number) covered by providers.")
    included: Optional[StrictBool] = Field(default=None, description="Indicates whether the catalog provider is included in the licensed packages. true returns providers covered by licensed packages, false returns providers not covered by licensed packages.")
    __properties: ClassVar[List[str]] = ["providerName", "providerType", "region", "location", "asn", "included"]

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
        """Create an instance of ApiCatalogProviderFilter from a JSON string"""
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
        """Create an instance of ApiCatalogProviderFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providerName": obj.get("providerName"),
            "providerType": obj.get("providerType"),
            "region": obj.get("region"),
            "location": obj.get("location"),
            "asn": obj.get("asn"),
            "included": obj.get("included")
        })
        return _obj


