# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_agents.models.vpn_type import VpnType
from typing import Optional, Set
from typing_extensions import Self

class EndpointVpnProfile(BaseModel):
    """
    EndpointVpnProfile
    """ # noqa: E501
    interface_name: Optional[StrictStr] = Field(default=None, description="Interface name associated with `interfaceProfile`.", alias="interfaceName")
    vpn_type: Optional[VpnType] = Field(default=None, alias="vpnType")
    vpn_gateway_address: Optional[StrictStr] = Field(default=None, description="IP address of the VPN gateway.", alias="vpnGatewayAddress")
    vpn_client_addresses: List[StrictStr] = Field(description="List of private IP addresses assigned to the device, by the VPN server.", alias="vpnClientAddresses")
    vpn_client_network_range: List[StrictStr] = Field(description="List of private networks assigned to the device, by the VPN server.", alias="vpnClientNetworkRange")
    __properties: ClassVar[List[str]] = ["interfaceName", "vpnType", "vpnGatewayAddress", "vpnClientAddresses", "vpnClientNetworkRange"]

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
        """Create an instance of EndpointVpnProfile from a JSON string"""
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
        """Create an instance of EndpointVpnProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interfaceName": obj.get("interfaceName"),
            "vpnType": obj.get("vpnType"),
            "vpnGatewayAddress": obj.get("vpnGatewayAddress"),
            "vpnClientAddresses": obj.get("vpnClientAddresses"),
            "vpnClientNetworkRange": obj.get("vpnClientNetworkRange")
        })
        return _obj


