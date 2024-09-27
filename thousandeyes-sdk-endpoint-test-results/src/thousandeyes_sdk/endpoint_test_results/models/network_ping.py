# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NetworkPing(BaseModel):
    """
    NetworkPing
    """ # noqa: E501
    avg_rtt: Optional[StrictInt] = Field(default=None, description="Ping average response time.", alias="avgRtt")
    max_rtt: Optional[StrictInt] = Field(default=None, description="Ping maximum response time.", alias="maxRtt")
    mean_dev_rtt: Optional[StrictInt] = Field(default=None, description="Ping mean standard deviation response time.", alias="meanDevRtt")
    min_rtt: Optional[StrictInt] = Field(default=None, description="Ping minimum response time.", alias="minRtt")
    pkts_received: Optional[StrictInt] = Field(default=None, description="Ping packets received.", alias="pktsReceived")
    pkts_sent: Optional[StrictInt] = Field(default=None, description="Ping packets sent.", alias="pktsSent")
    error: Optional[StrictStr] = Field(default=None, description="Only present when there is an error.")
    info_flags: Optional[List[StrictStr]] = Field(default=None, alias="infoFlags")
    __properties: ClassVar[List[str]] = ["avgRtt", "maxRtt", "meanDevRtt", "minRtt", "pktsReceived", "pktsSent", "error", "infoFlags"]

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
        """Create an instance of NetworkPing from a JSON string"""
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
            "avg_rtt",
            "max_rtt",
            "mean_dev_rtt",
            "min_rtt",
            "pkts_received",
            "pkts_sent",
            "error",
            "info_flags",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkPing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgRtt": obj.get("avgRtt"),
            "maxRtt": obj.get("maxRtt"),
            "meanDevRtt": obj.get("meanDevRtt"),
            "minRtt": obj.get("minRtt"),
            "pktsReceived": obj.get("pktsReceived"),
            "pktsSent": obj.get("pktsSent"),
            "error": obj.get("error"),
            "infoFlags": obj.get("infoFlags")
        })
        return _obj


