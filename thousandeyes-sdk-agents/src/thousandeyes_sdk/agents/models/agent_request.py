# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

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
from thousandeyes_sdk.agents.models.agent_ipv6_policy import AgentIpv6Policy
from typing import Optional, Set
from typing_extensions import Self

class AgentRequest(BaseModel):
    """
    AgentRequest
    """ # noqa: E501
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the agent.", alias="agentName")
    enabled: Optional[StrictBool] = Field(default=None, description="Flag indicating if the agent is enabled.")
    account_groups: Optional[List[StrictStr]] = Field(default=None, description="Contains a list of account groups IDs. See `/accounts-groups` for a list of account IDs", alias="accountGroups")
    ipv6_policy: Optional[AgentIpv6Policy] = Field(default=None, alias="ipv6Policy")
    keep_browser_cache: Optional[StrictBool] = Field(default=None, description="Flag indicating if the agent retains cache.", alias="keepBrowserCache")
    target_for_tests: Optional[StrictStr] = Field(default=None, description="Test target IP address.", alias="targetForTests")
    local_resolution_prefixes: Optional[List[StrictStr]] = Field(default=None, description="Public IP ranges for rDNS lookups. The range must be in CIDR notation; for example, 10.1.1.0/24. Maximum of 5 prefixes allowed (Enterprise Agents and Enterprise Agent clusters only).", alias="localResolutionPrefixes")
    tests: Optional[List[StrictStr]] = Field(default=None, description="Contains list of test IDs. See `/tests` to pull a list of available tests.")
    __properties: ClassVar[List[str]] = ["agentName", "enabled", "accountGroups", "ipv6Policy", "keepBrowserCache", "targetForTests", "localResolutionPrefixes", "tests"]

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
        """Create an instance of AgentRequest from a JSON string"""
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
        """Create an instance of AgentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentName": obj.get("agentName"),
            "enabled": obj.get("enabled"),
            "accountGroups": obj.get("accountGroups"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "keepBrowserCache": obj.get("keepBrowserCache"),
            "targetForTests": obj.get("targetForTests"),
            "localResolutionPrefixes": obj.get("localResolutionPrefixes"),
            "tests": obj.get("tests")
        })
        return _obj


