# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UsageQuota(BaseModel):
    """
    UsageQuota
    """ # noqa: E501
    month_start: Optional[datetime] = Field(default=None, description="Beginning of usage period in UTC (ISO date-time format).", alias="monthStart")
    month_end: Optional[datetime] = Field(default=None, description="End of usage period in UTC (ISO date-time format)..", alias="monthEnd")
    cloud_units_included: Optional[StrictInt] = Field(default=None, description="Monthly number of cloud units allocated, as part of the contract.", alias="cloudUnitsIncluded")
    endpoint_agents_included: Optional[StrictInt] = Field(default=None, description="Monthly number of endpoint agents allocated, as part of the contract.", alias="endpointAgentsIncluded")
    endpoint_agents_essentials_included: Optional[StrictInt] = Field(default=None, description="Monthly number of endpoint agents essentials allocated, as part of the contract.", alias="endpointAgentsEssentialsIncluded")
    endpoint_agents_embedded_included: Optional[StrictInt] = Field(default=None, description="Number of embedded endpoint agents allocated monthly, as specified in the contract.", alias="endpointAgentsEmbeddedIncluded")
    enterprise_agents_included: Optional[StrictInt] = Field(default=None, description="Monthly number of enterprise agents allocated, as part of the contract. Returns non-zero value only for organizations with legacy billing.", alias="enterpriseAgentsIncluded")
    __properties: ClassVar[List[str]] = ["monthStart", "monthEnd", "cloudUnitsIncluded", "endpointAgentsIncluded", "endpointAgentsEssentialsIncluded", "endpointAgentsEmbeddedIncluded", "enterpriseAgentsIncluded"]

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
        """Create an instance of UsageQuota from a JSON string"""
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
        """Create an instance of UsageQuota from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "monthStart": obj.get("monthStart"),
            "monthEnd": obj.get("monthEnd"),
            "cloudUnitsIncluded": obj.get("cloudUnitsIncluded"),
            "endpointAgentsIncluded": obj.get("endpointAgentsIncluded"),
            "endpointAgentsEssentialsIncluded": obj.get("endpointAgentsEssentialsIncluded"),
            "endpointAgentsEmbeddedIncluded": obj.get("endpointAgentsEmbeddedIncluded"),
            "enterpriseAgentsIncluded": obj.get("enterpriseAgentsIncluded")
        })
        return _obj


