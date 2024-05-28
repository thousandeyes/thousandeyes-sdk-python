# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EnterpriseAgentUnits(BaseModel):
    """
    EnterpriseAgentUnits
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="Unique identifier of the account group owning the enterprise agent units.")
    account_group_name: Optional[StrictStr] = Field(default=None, description="Name of the account group which owns the enterprise agent units.", alias="accountGroupName")
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the enterprise agent generating usage.", alias="agentId")
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the enterprise agent generating usage.", alias="agentName")
    enterprise_units_used: Optional[StrictInt] = Field(default=None, description="Number of enterprise agent units owned by the specific account group in the usage period.", alias="enterpriseUnitsUsed")
    enterprise_units_projected: Optional[StrictInt] = Field(default=None, description="Number of enterprise units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing.", alias="enterpriseUnitsProjected")
    vagent_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the virtual agent generating usage", alias="vagentId")
    __properties: ClassVar[List[str]] = ["aid", "accountGroupName", "agentId", "agentName", "enterpriseUnitsUsed", "enterpriseUnitsProjected", "vagentId"]

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
        """Create an instance of EnterpriseAgentUnits from a JSON string"""
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
        """Create an instance of EnterpriseAgentUnits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "accountGroupName": obj.get("accountGroupName"),
            "agentId": obj.get("agentId"),
            "agentName": obj.get("agentName"),
            "enterpriseUnitsUsed": obj.get("enterpriseUnitsUsed"),
            "enterpriseUnitsProjected": obj.get("enterpriseUnitsProjected"),
            "vagentId": obj.get("vagentId")
        })
        return _obj

