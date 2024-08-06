# coding: utf-8

"""
    BGP Monitors API

     Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.  When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.  For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility). 

    The version of the OpenAPI document: 7.0.14
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

class Link(BaseModel):
    """
    A hyperlink from the containing resource to a URI.
    """ # noqa: E501
    href: StrictStr = Field(description="Its value is either a URI [RFC3986] or a URI template [RFC6570].")
    templated: Optional[StrictBool] = Field(default=None, description="Should be true when the link object's \"href\" property is a URI template.")
    type: Optional[StrictStr] = Field(default=None, description="Used as a hint to indicate the media type expected when dereferencing the target resource.")
    deprecation: Optional[StrictStr] = Field(default=None, description="Its presence indicates that the link is to be deprecated at a future date. Its value is a URL that should provide further information about the deprecation.")
    name: Optional[StrictStr] = Field(default=None, description="Its value may be used as a secondary key for selecting link objects that share the same relation type.")
    profile: Optional[StrictStr] = Field(default=None, description="A URI that hints about the profile of the target resource.")
    title: Optional[StrictStr] = Field(default=None, description="Intended for labelling the link with a human-readable identifier")
    hreflang: Optional[StrictStr] = Field(default=None, description="Indicates the language of the target resource")
    __properties: ClassVar[List[str]] = ["href", "templated", "type", "deprecation", "name", "profile", "title", "hreflang"]

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
        """Create an instance of Link from a JSON string"""
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
        """Create an instance of Link from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "templated": obj.get("templated"),
            "type": obj.get("type"),
            "deprecation": obj.get("deprecation"),
            "name": obj.get("name"),
            "profile": obj.get("profile"),
            "title": obj.get("title"),
            "hreflang": obj.get("hreflang")
        })
        return _obj


