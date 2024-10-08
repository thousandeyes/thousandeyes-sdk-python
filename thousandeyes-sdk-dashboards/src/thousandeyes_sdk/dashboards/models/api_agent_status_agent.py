# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.dashboards.models.api_agent_location import ApiAgentLocation
from thousandeyes_sdk.dashboards.models.api_agent_status_ip_info import ApiAgentStatusIpInfo
from thousandeyes_sdk.dashboards.models.enterprise_agent_state import EnterpriseAgentState
from typing import Optional, Set
from typing_extensions import Self

class ApiAgentStatusAgent(BaseModel):
    """
    Agent shown in agent status widget.
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, description="Identifier of the agent.", alias="agentId")
    status: Optional[EnterpriseAgentState] = None
    ip_info: Optional[ApiAgentStatusIpInfo] = Field(default=None, alias="ipInfo")
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the agent", alias="agentName")
    location: Optional[ApiAgentLocation] = None
    __properties: ClassVar[List[str]] = ["agentId", "status", "ipInfo", "agentName", "location"]

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
        """Create an instance of ApiAgentStatusAgent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ip_info
        if self.ip_info:
            _dict['ipInfo'] = self.ip_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiAgentStatusAgent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentId": obj.get("agentId"),
            "status": obj.get("status"),
            "ipInfo": ApiAgentStatusIpInfo.from_dict(obj["ipInfo"]) if obj.get("ipInfo") is not None else None,
            "agentName": obj.get("agentName"),
            "location": ApiAgentLocation.from_dict(obj["location"]) if obj.get("location") is not None else None
        })
        return _obj


