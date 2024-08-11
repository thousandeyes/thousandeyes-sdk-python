# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.agents.models.alert_integration_type import AlertIntegrationType
from typing import Optional, Set
from typing_extensions import Self

class AlertIntegrationBase(BaseModel):
    """
    AlertIntegrationBase
    """ # noqa: E501
    integration_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the integration.", alias="integrationId")
    integration_name: Optional[StrictStr] = Field(default=None, description="Name of the integration.", alias="integrationName")
    integration_type: Optional[AlertIntegrationType] = Field(default=None, alias="integrationType")
    target: Optional[StrictStr] = Field(default=None, description="Target URL of the integration.")
    auth_method: Optional[StrictStr] = Field(default=None, description="(PagerDuty only) Authentication method.", alias="authMethod")
    auth_user: Optional[StrictStr] = Field(default=None, description="(PagerDuty only) Authentication user.", alias="authUser")
    auth_token: Optional[StrictStr] = Field(default=None, description="(PagerDuty only) Authentication token.", alias="authToken")
    channel: Optional[StrictStr] = Field(default=None, description="(Slack only) Slack `#channel` or `@user`.")
    __properties: ClassVar[List[str]] = ["integrationId", "integrationName", "integrationType", "target", "authMethod", "authUser", "authToken", "channel"]

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
        """Create an instance of AlertIntegrationBase from a JSON string"""
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
        """Create an instance of AlertIntegrationBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "integrationId": obj.get("integrationId"),
            "integrationName": obj.get("integrationName"),
            "integrationType": obj.get("integrationType"),
            "target": obj.get("target"),
            "authMethod": obj.get("authMethod"),
            "authUser": obj.get("authUser"),
            "authToken": obj.get("authToken"),
            "channel": obj.get("channel")
        })
        return _obj


