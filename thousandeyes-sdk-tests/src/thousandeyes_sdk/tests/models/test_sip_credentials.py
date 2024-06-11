# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.7
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
from thousandeyes_sdk.tests.models.sip_test_protocol import SipTestProtocol
from typing import Optional, Set
from typing_extensions import Self

class TestSipCredentials(BaseModel):
    """
    TestSipCredentials
    """ # noqa: E501
    auth_user: Optional[StrictStr] = Field(default=None, description="Username for authentication with SIP server.", alias="authUser")
    password: Optional[StrictStr] = Field(default=None, description="Password for Basic/NTLM authentication.")
    port: Annotated[int, Field(le=65535, strict=True, ge=1)] = Field(description="Target port.")
    protocol: Optional[SipTestProtocol] = None
    sip_registrar: Optional[StrictStr] = Field(default=None, description="SIP server to be tested, specified by domain name or IP address.", alias="sipRegistrar")
    user: Optional[StrictStr] = Field(default=None, description="Username for SIP registration, should be unique within a ThousandEyes account group.")
    __properties: ClassVar[List[str]] = ["authUser", "password", "port", "protocol", "sipRegistrar", "user"]

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
        """Create an instance of TestSipCredentials from a JSON string"""
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
        """Create an instance of TestSipCredentials from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authUser": obj.get("authUser"),
            "password": obj.get("password"),
            "port": obj.get("port") if obj.get("port") is not None else 49153,
            "protocol": obj.get("protocol"),
            "sipRegistrar": obj.get("sipRegistrar"),
            "user": obj.get("user")
        })
        return _obj


