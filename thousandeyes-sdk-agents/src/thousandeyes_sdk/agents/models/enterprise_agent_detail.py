# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.agents.models.account_group import AccountGroup
from thousandeyes_sdk.agents.models.cluster_member import ClusterMember
from thousandeyes_sdk.agents.models.enterprise_agent_ipv6_policy import EnterpriseAgentIpv6Policy
from thousandeyes_sdk.agents.models.enterprise_agent_state import EnterpriseAgentState
from thousandeyes_sdk.agents.models.error_detail import ErrorDetail
from thousandeyes_sdk.agents.models.interface_ip_mapping import InterfaceIpMapping
from thousandeyes_sdk.agents.models.labels import Labels
from thousandeyes_sdk.agents.models.notification_rules import NotificationRules
from thousandeyes_sdk.agents.models.self_links import SelfLinks
from thousandeyes_sdk.agents.models.simple_test import SimpleTest
from typing import Optional, Set
from typing_extensions import Self

class EnterpriseAgentDetail(BaseModel):
    """
    EnterpriseAgentDetail
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
    cluster_members: Optional[List[ClusterMember]] = Field(default=None, description="If an enterprise agent is clustered, detailed information about each cluster member will be shown as array entries in the clusterMembers field. This field is not shown for Enterprise Agents in standalone mode, or for Cloud Agents.", alias="clusterMembers")
    utilization: Optional[StrictInt] = Field(default=None, description="Shows overall utilization percentage (online Enterprise Agents and Enterprise Clusters only).")
    account_groups: Optional[List[AccountGroup]] = Field(default=None, description="List of account groups. See /accounts-groups to pull a list of account IDs", alias="accountGroups")
    ipv6_policy: Optional[EnterpriseAgentIpv6Policy] = Field(default=None, alias="ipv6Policy")
    error_details: Optional[List[ErrorDetail]] = Field(default=None, description="If an enterprise agent or a cluster member presents at least one error, the errors will be shown as an array of entries in the errorDetails field (Enterprise Agents and Enterprise Cluster members only)", alias="errorDetails")
    hostname: Optional[StrictStr] = Field(default=None, description="Fully qualified domain name of the agent (Enterprise Agents only)")
    last_seen: Optional[datetime] = Field(default=None, description="UTC last seen date (ISO date-time format).", alias="lastSeen")
    agent_state: Optional[EnterpriseAgentState] = Field(default=None, alias="agentState")
    keep_browser_cache: Optional[StrictBool] = Field(default=None, description="Flag indicating if the agent retains cache.", alias="keepBrowserCache")
    created_date: Optional[datetime] = Field(default=None, description="UTC Agent creation date (ISO date-time format).", alias="createdDate")
    target_for_tests: Optional[StrictStr] = Field(default=None, description="Test target IP address.", alias="targetForTests")
    local_resolution_prefixes: Optional[List[StrictStr]] = Field(default=None, description="To perform rDNS lookups for public IP ranges, this field represents the public IP ranges. The range must be in CIDR notation; for example, 10.1.1.0/24. Maximum of 5 prefixes allowed (Enterprise Agents and Enterprise Agent clusters only).", alias="localResolutionPrefixes")
    interface_ip_mappings: Optional[List[InterfaceIpMapping]] = Field(default=None, alias="interfaceIpMappings")
    tests: Optional[List[SimpleTest]] = Field(default=None, description="List of tests. See `/tests` for more information.")
    notification_rules: Optional[List[NotificationRules]] = Field(default=None, description="List of notification rule objects configured on agent", alias="notificationRules")
    labels: Optional[List[Labels]] = Field(default=None, description="List of labels. See `/labels` for more information.")
    agent_type: Annotated[str, Field(strict=True)] = Field(description="Enterprise agent type.", alias="agentType")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["ipAddresses", "publicIpAddresses", "network", "agentId", "agentName", "location", "countryId", "enabled", "prefix", "verifySslCertificates", "clusterMembers", "utilization", "accountGroups", "ipv6Policy", "errorDetails", "hostname", "lastSeen", "agentState", "keepBrowserCache", "createdDate", "targetForTests", "localResolutionPrefixes", "interfaceIpMappings", "tests", "notificationRules", "labels", "agentType", "_links"]

    @field_validator('agent_type')
    def agent_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^enterprise$", value):
            raise ValueError(r"must validate the regular expression /^enterprise$/")
        return value

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
        """Create an instance of EnterpriseAgentDetail from a JSON string"""
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
            "cluster_members",
            "utilization",
            "error_details",
            "hostname",
            "last_seen",
            "created_date",
            "interface_ip_mappings",
            "labels",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_members (list)
        _items = []
        if self.cluster_members:
            for _item in self.cluster_members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusterMembers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_groups (list)
        _items = []
        if self.account_groups:
            for _item in self.account_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in error_details (list)
        _items = []
        if self.error_details:
            for _item in self.error_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errorDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in interface_ip_mappings (list)
        _items = []
        if self.interface_ip_mappings:
            for _item in self.interface_ip_mappings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['interfaceIpMappings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tests (list)
        _items = []
        if self.tests:
            for _item in self.tests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notification_rules (list)
        _items = []
        if self.notification_rules:
            for _item in self.notification_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notificationRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnterpriseAgentDetail from a dict"""
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
            "clusterMembers": [ClusterMember.from_dict(_item) for _item in obj["clusterMembers"]] if obj.get("clusterMembers") is not None else None,
            "utilization": obj.get("utilization"),
            "accountGroups": [AccountGroup.from_dict(_item) for _item in obj["accountGroups"]] if obj.get("accountGroups") is not None else None,
            "ipv6Policy": obj.get("ipv6Policy"),
            "errorDetails": [ErrorDetail.from_dict(_item) for _item in obj["errorDetails"]] if obj.get("errorDetails") is not None else None,
            "hostname": obj.get("hostname"),
            "lastSeen": obj.get("lastSeen"),
            "agentState": obj.get("agentState"),
            "keepBrowserCache": obj.get("keepBrowserCache"),
            "createdDate": obj.get("createdDate"),
            "targetForTests": obj.get("targetForTests"),
            "localResolutionPrefixes": obj.get("localResolutionPrefixes"),
            "interfaceIpMappings": [InterfaceIpMapping.from_dict(_item) for _item in obj["interfaceIpMappings"]] if obj.get("interfaceIpMappings") is not None else None,
            "tests": [SimpleTest.from_dict(_item) for _item in obj["tests"]] if obj.get("tests") is not None else None,
            "notificationRules": [NotificationRules.from_dict(_item) for _item in obj["notificationRules"]] if obj.get("notificationRules") is not None else None,
            "labels": [Labels.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "agentType": obj.get("agentType"),
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


