# coding: utf-8

"""
    Emulation API

    The Emulation API facilitates the retrieval of user-agent strings for HTTP, pageload, and transaction tests. It also enables the retrieval and addition of emulated devices for pageload and transaction tests.  To access Emulation API endpoints, the following permissions are required:  * `Settings Tests Read` for read operations. * `Settings Tests Update` for write operations. 

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
from typing_extensions import Annotated
from thousandeyes_sdk.emulation.models.emulated_device_category import EmulatedDeviceCategory
from typing import Optional, Set
from typing_extensions import Self

class EmulatedDeviceResponse(BaseModel):
    """
    EmulatedDeviceResponse
    """ # noqa: E501
    category: EmulatedDeviceCategory
    width: Annotated[int, Field(le=9999, strict=True, ge=50)] = Field(description="The width of the display of the emulated device.")
    height: Annotated[int, Field(le=9999, strict=True, ge=50)] = Field(description="The height of the display of the emulated device.")
    name: Optional[StrictStr] = Field(default=None, description="The device name")
    code_name: Optional[StrictStr] = Field(default=None, description="A code corresponding to the device name.", alias="codeName")
    id: Optional[StrictStr] = Field(default=None, description="ID of the emulated device.")
    available_user_agents: Optional[List[StrictStr]] = Field(default=None, description="A list of user-agent strings for this emulated device.", alias="availableUserAgents")
    default_user_agent_template: Optional[StrictStr] = Field(default=None, description="The default user-agent template to use for this device.", alias="defaultUserAgentTemplate")
    __properties: ClassVar[List[str]] = ["category", "width", "height", "name", "codeName", "id", "availableUserAgents", "defaultUserAgentTemplate"]

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
        """Create an instance of EmulatedDeviceResponse from a JSON string"""
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
        """Create an instance of EmulatedDeviceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "name": obj.get("name"),
            "codeName": obj.get("codeName"),
            "id": obj.get("id"),
            "availableUserAgents": obj.get("availableUserAgents"),
            "defaultUserAgentTemplate": obj.get("defaultUserAgentTemplate")
        })
        return _obj


