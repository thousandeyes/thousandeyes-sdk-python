# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.agents.models.enterprise_agent_state import EnterpriseAgentState
from thousandeyes_sdk.agents.models.error_detail import ErrorDetail
from typing import Optional, Set
from typing_extensions import Self

class ClusterMember(BaseModel):
    """
    ClusterMember
    """ # noqa: E501
    ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of private IP addresses.", alias="ipAddresses")
    public_ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of public IP addresses.", alias="publicIpAddresses")
    network: Optional[StrictStr] = Field(default=None, description="Network (including ASN) of agent’s public IP.")
    member_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the cluster member", alias="memberId")
    name: Optional[StrictStr] = Field(default=None, description="Name of the cluster member")
    error_details: Optional[List[ErrorDetail]] = Field(default=None, description="If an enterprise agent or a cluster member presents at least one error, the errors will be shown as an array of entries in the errorDetails field (Enterprise Agents and Enterprise Cluster members only)", alias="errorDetails")
    last_seen: Optional[datetime] = Field(default=None, description="UTC last seen date (ISO date-time format).", alias="lastSeen")
    agent_state: Optional[EnterpriseAgentState] = Field(default=None, alias="agentState")
    target_for_tests: Optional[StrictStr] = Field(default=None, description="Test target IP address.", alias="targetForTests")
    utilization: Optional[StrictInt] = Field(default=None, description="Shows overall utilization percentage (online Enterprise Agents and Enterprise Clusters only).")
    __properties: ClassVar[List[str]] = ["ipAddresses", "publicIpAddresses", "network", "memberId", "name", "errorDetails", "lastSeen", "agentState", "targetForTests", "utilization"]

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
        """Create an instance of ClusterMember from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "ip_addresses",
            "public_ip_addresses",
            "network",
            "member_id",
            "name",
            "error_details",
            "last_seen",
            "utilization",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in error_details (list)
        _items = []
        if self.error_details:
            for _item in self.error_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errorDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipAddresses": obj.get("ipAddresses"),
            "publicIpAddresses": obj.get("publicIpAddresses"),
            "network": obj.get("network"),
            "memberId": obj.get("memberId"),
            "name": obj.get("name"),
            "errorDetails": [ErrorDetail.from_dict(_item) for _item in obj["errorDetails"]] if obj.get("errorDetails") is not None else None,
            "lastSeen": obj.get("lastSeen"),
            "agentState": obj.get("agentState"),
            "targetForTests": obj.get("targetForTests"),
            "utilization": obj.get("utilization")
        })
        return _obj


