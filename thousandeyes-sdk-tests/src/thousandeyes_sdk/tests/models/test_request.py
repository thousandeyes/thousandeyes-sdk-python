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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.tests.models.test_agent_request import TestAgentRequest
from typing import Optional, Set
from typing_extensions import Self

class TestRequest(BaseModel):
    """
    TestRequest
    """ # noqa: E501
    labels: Optional[List[StrictStr]] = Field(default=None, description="Contains list of test label IDs (get `labelId` from `/labels` endpoint)")
    shared_with_accounts: Optional[List[StrictStr]] = Field(default=None, description="Contains list of account group IDs. Test is shared with the listed account groups (get `aid` from `/account-groups` endpoint)", alias="sharedWithAccounts")
    alert_rules: Optional[List[StrictStr]] = Field(default=None, description="List of alert rules IDs to apply to the test (get `ruleId` from `/alerts/rules` endpoint. If `alertsEnabled` is set to `true` and `alertRules` is not included on test creation or update, applicable user default alert rules will be used)", alias="alertRules")
    agents: List[TestAgentRequest] = Field(description="Contains list of Agent IDs (get `agentId` from `/agents` endpoint).")
    __properties: ClassVar[List[str]] = ["labels", "sharedWithAccounts", "alertRules", "agents"]

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
        """Create an instance of TestRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in agents (list)
        _items = []
        if self.agents:
            for _item in self.agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "labels": obj.get("labels"),
            "sharedWithAccounts": obj.get("sharedWithAccounts"),
            "alertRules": obj.get("alertRules"),
            "agents": [TestAgentRequest.from_dict(_item) for _item in obj["agents"]] if obj.get("agents") is not None else None
        })
        return _obj


