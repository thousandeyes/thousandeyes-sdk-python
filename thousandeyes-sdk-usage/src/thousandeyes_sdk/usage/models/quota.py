# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.usage.models.account_group_quota import AccountGroupQuota
from thousandeyes_sdk.usage.models.organization_quota import OrganizationQuota
from typing import Optional, Set
from typing_extensions import Self

class Quota(BaseModel):
    """
    Quota
    """ # noqa: E501
    organization_quota: Optional[OrganizationQuota] = Field(default=None, alias="organizationQuota")
    account_group_quotas: Optional[List[AccountGroupQuota]] = Field(default=None, alias="accountGroupQuotas")
    __properties: ClassVar[List[str]] = ["organizationQuota", "accountGroupQuotas"]

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
        """Create an instance of Quota from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization_quota
        if self.organization_quota:
            _dict['organizationQuota'] = self.organization_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in account_group_quotas (list)
        _items = []
        if self.account_group_quotas:
            for _item in self.account_group_quotas:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountGroupQuotas'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Quota from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "organizationQuota": OrganizationQuota.from_dict(obj["organizationQuota"]) if obj.get("organizationQuota") is not None else None,
            "accountGroupQuotas": [AccountGroupQuota.from_dict(_item) for _item in obj["accountGroupQuotas"]] if obj.get("accountGroupQuotas") is not None else None
        })
        return _obj


