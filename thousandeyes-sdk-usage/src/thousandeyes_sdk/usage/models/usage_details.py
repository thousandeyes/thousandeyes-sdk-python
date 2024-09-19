# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View organization usage` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View organization usage` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.usage.models.endpoint_agents_embedded import EndpointAgentsEmbedded
from thousandeyes_sdk.usage.models.endpoint_agents_essentials import EndpointAgentsEssentials
from thousandeyes_sdk.usage.models.endpoint_agents_usage import EndpointAgentsUsage
from thousandeyes_sdk.usage.models.enterprise_agent_units import EnterpriseAgentUnits
from thousandeyes_sdk.usage.models.enterprise_agents import EnterpriseAgents
from thousandeyes_sdk.usage.models.test_usage import TestUsage
from thousandeyes_sdk.usage.models.usage_quota import UsageQuota
from typing import Optional, Set
from typing_extensions import Self

class UsageDetails(BaseModel):
    """
    UsageDetails
    """ # noqa: E501
    quota: Optional[UsageQuota] = None
    cloud_units_used: Optional[StrictInt] = Field(default=None, description="Number of cloud units consumed thus far in the usage period.", alias="cloudUnitsUsed")
    cloud_units_projected: Optional[StrictInt] = Field(default=None, description="Number of cloud units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly.", alias="cloudUnitsProjected")
    cloud_units_next_billing_period: Optional[StrictInt] = Field(default=None, description="Number of cloud units projected in the upcoming usage period, based on configuration of enabled tests. This value is updated hourly.", alias="cloudUnitsNextBillingPeriod")
    enterprise_units_used: Optional[StrictInt] = Field(default=None, description="Number of enterprise units consumed in the usage period. Returns non-zero value only for organizations with metered billing.", alias="enterpriseUnitsUsed")
    enterprise_units_projected: Optional[StrictInt] = Field(default=None, description="Number of enterprise units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing.", alias="enterpriseUnitsProjected")
    enterprise_units_next_billing_period: Optional[StrictInt] = Field(default=None, description="Projected number of enterprise units for the upcoming usage period, based on the configuration of enabled tests. This value is updated hourly and returns a non-zero value only for organizations with metered billing.", alias="enterpriseUnitsNextBillingPeriod")
    connected_devices_units_used: Optional[StrictInt] = Field(default=None, description="Number of connected device units consumed in the usage period.", alias="connectedDevicesUnitsUsed")
    connected_devices_units_projected: Optional[StrictInt] = Field(default=None, description="Projected number of connected device units for the current usage period. This projection is based on the units consumed to date and the configuration of enabled tests. The value is updated hourly.", alias="connectedDevicesUnitsProjected")
    connected_devices_units_next_billing_period: Optional[StrictInt] = Field(default=None, description="Projected number of connected device units for the upcoming usage period. This projection is based on the configuration of enabled tests and is updated hourly.", alias="connectedDevicesUnitsNextBillingPeriod")
    endpoint_agents_used: Optional[StrictInt] = Field(default=None, description="Number of endpoint agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation.", alias="endpointAgentsUsed")
    endpoint_agents_essentials_used: Optional[StrictInt] = Field(default=None, description="Number of endpoint agents essentials used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation.", alias="endpointAgentsEssentialsUsed")
    endpoint_agents_embedded_used: Optional[StrictInt] = Field(default=None, description="Number of embedded endpoint agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation.", alias="endpointAgentsEmbeddedUsed")
    enterprise_agents_used: Optional[StrictInt] = Field(default=None, description="Number of enterprise agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation.", alias="enterpriseAgentsUsed")
    enterprise_agent_units: Optional[List[EnterpriseAgentUnits]] = Field(default=None, description="A breakdown of enterprise unit consumption for each agent during the current monthly period. Each entry provides data for both the current actual usage and the projected usage. Returns non-zero values for organizations with metered billing.", alias="enterpriseAgentUnits")
    tests: Optional[List[TestUsage]] = Field(default=None, description="A breakdown of unit consumption for each test during the current monthly period. Each entry provides information about both the current actual usage and the projected usage.")
    endpoint_agents: Optional[List[EndpointAgentsUsage]] = Field(default=None, description="Endpoint agents used by account group.", alias="endpointAgents")
    endpoint_agents_essentials: Optional[List[EndpointAgentsEssentials]] = Field(default=None, description="Endpoint agents essentials used by account group.", alias="endpointAgentsEssentials")
    endpoint_agents_embedded: Optional[List[EndpointAgentsEmbedded]] = Field(default=None, description="Endpoint agents embedded used by account group.", alias="endpointAgentsEmbedded")
    enterprise_agents: Optional[List[EnterpriseAgents]] = Field(default=None, description="Enterprise agents used by account group.", alias="enterpriseAgents")
    __properties: ClassVar[List[str]] = ["quota", "cloudUnitsUsed", "cloudUnitsProjected", "cloudUnitsNextBillingPeriod", "enterpriseUnitsUsed", "enterpriseUnitsProjected", "enterpriseUnitsNextBillingPeriod", "connectedDevicesUnitsUsed", "connectedDevicesUnitsProjected", "connectedDevicesUnitsNextBillingPeriod", "endpointAgentsUsed", "endpointAgentsEssentialsUsed", "endpointAgentsEmbeddedUsed", "enterpriseAgentsUsed", "enterpriseAgentUnits", "tests", "endpointAgents", "endpointAgentsEssentials", "endpointAgentsEmbedded", "enterpriseAgents"]

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
        """Create an instance of UsageDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quota
        if self.quota:
            _dict['quota'] = self.quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in enterprise_agent_units (list)
        _items = []
        if self.enterprise_agent_units:
            for _item in self.enterprise_agent_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['enterpriseAgentUnits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tests (list)
        _items = []
        if self.tests:
            for _item in self.tests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in endpoint_agents (list)
        _items = []
        if self.endpoint_agents:
            for _item in self.endpoint_agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endpointAgents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in endpoint_agents_essentials (list)
        _items = []
        if self.endpoint_agents_essentials:
            for _item in self.endpoint_agents_essentials:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endpointAgentsEssentials'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in endpoint_agents_embedded (list)
        _items = []
        if self.endpoint_agents_embedded:
            for _item in self.endpoint_agents_embedded:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endpointAgentsEmbedded'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in enterprise_agents (list)
        _items = []
        if self.enterprise_agents:
            for _item in self.enterprise_agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['enterpriseAgents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quota": UsageQuota.from_dict(obj["quota"]) if obj.get("quota") is not None else None,
            "cloudUnitsUsed": obj.get("cloudUnitsUsed"),
            "cloudUnitsProjected": obj.get("cloudUnitsProjected"),
            "cloudUnitsNextBillingPeriod": obj.get("cloudUnitsNextBillingPeriod"),
            "enterpriseUnitsUsed": obj.get("enterpriseUnitsUsed"),
            "enterpriseUnitsProjected": obj.get("enterpriseUnitsProjected"),
            "enterpriseUnitsNextBillingPeriod": obj.get("enterpriseUnitsNextBillingPeriod"),
            "connectedDevicesUnitsUsed": obj.get("connectedDevicesUnitsUsed"),
            "connectedDevicesUnitsProjected": obj.get("connectedDevicesUnitsProjected"),
            "connectedDevicesUnitsNextBillingPeriod": obj.get("connectedDevicesUnitsNextBillingPeriod"),
            "endpointAgentsUsed": obj.get("endpointAgentsUsed"),
            "endpointAgentsEssentialsUsed": obj.get("endpointAgentsEssentialsUsed"),
            "endpointAgentsEmbeddedUsed": obj.get("endpointAgentsEmbeddedUsed"),
            "enterpriseAgentsUsed": obj.get("enterpriseAgentsUsed"),
            "enterpriseAgentUnits": [EnterpriseAgentUnits.from_dict(_item) for _item in obj["enterpriseAgentUnits"]] if obj.get("enterpriseAgentUnits") is not None else None,
            "tests": [TestUsage.from_dict(_item) for _item in obj["tests"]] if obj.get("tests") is not None else None,
            "endpointAgents": [EndpointAgentsUsage.from_dict(_item) for _item in obj["endpointAgents"]] if obj.get("endpointAgents") is not None else None,
            "endpointAgentsEssentials": [EndpointAgentsEssentials.from_dict(_item) for _item in obj["endpointAgentsEssentials"]] if obj.get("endpointAgentsEssentials") is not None else None,
            "endpointAgentsEmbedded": [EndpointAgentsEmbedded.from_dict(_item) for _item in obj["endpointAgentsEmbedded"]] if obj.get("endpointAgentsEmbedded") is not None else None,
            "enterpriseAgents": [EnterpriseAgents.from_dict(_item) for _item in obj["enterpriseAgents"]] if obj.get("enterpriseAgents") is not None else None
        })
        return _obj


