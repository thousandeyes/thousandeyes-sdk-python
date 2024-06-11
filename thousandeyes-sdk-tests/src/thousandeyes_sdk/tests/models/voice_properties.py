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
from thousandeyes_sdk.tests.models.test_dscp_id import TestDscpId
from typing import Optional, Set
from typing_extensions import Self

class VoiceProperties(BaseModel):
    """
    VoiceProperties
    """ # noqa: E501
    codec: Optional[StrictStr] = Field(default=None, description="Codec label")
    codec_id: Optional[StrictStr] = Field(default=None, description="Coded ID, [see the list of acceptable values](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/working-with-test-settings#rtp-stream-advanced-settings-tab)", alias="codecId")
    dscp: Optional[StrictStr] = Field(default=None, description="DSCP label.")
    dscp_id: Optional[TestDscpId] = Field(default=None, alias="dscpId")
    duration: Optional[Annotated[int, Field(le=30, strict=True, ge=5)]] = Field(default=5, description="Duration of the test in seconds.")
    jitter_buffer: Optional[Annotated[int, Field(le=150, strict=True, ge=0)]] = Field(default=40, description="De-jitter buffer size in seconds.", alias="jitterBuffer")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1024)]] = Field(default=None, description="Port number for the chosen protocol.")
    target_agent_id: StrictStr = Field(description="Agent ID of the target agent for the test.", alias="targetAgentId")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["codec", "codecId", "dscp", "dscpId", "duration", "jitterBuffer", "numPathTraces", "port", "targetAgentId", "type"]

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
        """Create an instance of VoiceProperties from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "codec",
            "dscp",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VoiceProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "codec": obj.get("codec"),
            "codecId": obj.get("codecId"),
            "dscp": obj.get("dscp"),
            "dscpId": obj.get("dscpId"),
            "duration": obj.get("duration") if obj.get("duration") is not None else 5,
            "jitterBuffer": obj.get("jitterBuffer") if obj.get("jitterBuffer") is not None else 40,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "port": obj.get("port"),
            "targetAgentId": obj.get("targetAgentId"),
            "type": obj.get("type")
        })
        return _obj


