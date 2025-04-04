# coding: utf-8

"""
    Tests API

    This API allows you to list, create, edit, and delete Network and Application Synthetics tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.tests.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType
from typing import Optional, Set
from typing_extensions import Self

class AgentResponse(BaseModel):
    """
    AgentResponse
    """ # noqa: E501
    ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of private IP addresses.", alias="ipAddresses")
    public_ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of public IP addresses.", alias="publicIpAddresses")
    network: Optional[StrictStr] = Field(default=None, description="Network (including ASN) of agent’s public IP.")
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the agent.", alias="agentId")
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the agent.", alias="agentName")
    location: Optional[StrictStr] = Field(default=None, description="Location of the agent.")
    country_id: Optional[StrictStr] = Field(default=None, description="2-digit ISO country code", alias="countryId")
    enabled: Optional[StrictBool] = Field(default=None, description="Flag indicating if the agent is enabled.")
    prefix: Optional[StrictStr] = Field(default=None, description="Prefix containing agents public IP address.")
    verify_ssl_certificates: Optional[StrictBool] = Field(default=None, description="Flag indicating if has normal SSL operations or  if instead it's set to ignore SSL errors on browserbot-based tests.", alias="verifySslCertificates")
    agent_type: CloudEnterpriseAgentType = Field(alias="agentType")
    __properties: ClassVar[List[str]] = ["ipAddresses", "publicIpAddresses", "network", "agentId", "agentName", "location", "countryId", "enabled", "prefix", "verifySslCertificates", "agentType"]

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
        """Create an instance of AgentResponse from a JSON string"""
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
            "agent_id",
            "location",
            "country_id",
            "prefix",
            "verify_ssl_certificates",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipAddresses": obj.get("ipAddresses"),
            "publicIpAddresses": obj.get("publicIpAddresses"),
            "network": obj.get("network"),
            "agentId": obj.get("agentId"),
            "agentName": obj.get("agentName"),
            "location": obj.get("location"),
            "countryId": obj.get("countryId"),
            "enabled": obj.get("enabled"),
            "prefix": obj.get("prefix"),
            "verifySslCertificates": obj.get("verifySslCertificates"),
            "agentType": obj.get("agentType")
        })
        return _obj


