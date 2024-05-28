# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.instant_tests.models.api_predefined_variable import ApiPredefinedVariable
from thousandeyes_sdk.instant_tests.models.api_request import ApiRequest
from thousandeyes_sdk.instant_tests.models.test_agent import TestAgent
from thousandeyes_sdk.instant_tests.models.test_links import TestLinks
from thousandeyes_sdk.instant_tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.instant_tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.instant_tests.models.test_protocol import TestProtocol
from thousandeyes_sdk.instant_tests.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class ApiInstantTestRequest(BaseModel):
    """
    ApiInstantTestRequest
    """ # noqa: E501
    created_by: Optional[StrictStr] = Field(default=None, description="User that created the test.", alias="createdBy")
    created_date: Optional[datetime] = Field(default=None, description="UTC created date (ISO date-time format).", alias="createdDate")
    description: Optional[StrictStr] = Field(default=None, description="A description of the test.")
    live_share: Optional[StrictBool] = Field(default=None, description="Indicates if the test is shared with the account group.", alias="liveShare")
    modified_by: Optional[StrictStr] = Field(default=None, description="User that modified the test.", alias="modifiedBy")
    modified_date: Optional[datetime] = Field(default=None, description="UTC last modification date (ISO date-time format).", alias="modifiedDate")
    saved_event: Optional[StrictBool] = Field(default=None, description="Indicates if the test is a saved event.", alias="savedEvent")
    test_id: Optional[StrictStr] = Field(default=None, description="Each test is assigned an unique ID; this is used to access test information and results from other endpoints.", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="The name of the test. Test name must be unique.", alias="testName")
    type: Optional[StrictStr] = None
    links: Optional[TestLinks] = Field(default=None, alias="_links")
    labels: Optional[List[StrictStr]] = Field(default=None, description="A list of test label identifiers (get `labelId` from `/labels` endpoint).")
    shared_with_accounts: Optional[List[StrictStr]] = Field(default=None, description="A list of account group identifiers that the test is shared with (get `aid` from `/account-groups` endpoint).", alias="sharedWithAccounts")
    follow_redirects: Optional[StrictBool] = Field(default=True, description="Indicates if HTTP/301 or HTTP/302 redirect directives should be followed. To disable following redirects, set this parameter to false.", alias="followRedirects")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    predefined_variables: Optional[List[ApiPredefinedVariable]] = Field(default=None, alias="predefinedVariables")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    requests: List[ApiRequest]
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    target_time: Optional[Annotated[int, Field(le=60, strict=True, ge=0)]] = Field(default=None, description="Target time for completion metric, defaults to 50% of time limit specified in seconds. (0 means default behavior)", alias="targetTime")
    time_limit: Optional[Annotated[int, Field(le=180, strict=True, ge=5)]] = Field(default=30, description="Time limit for transaction in seconds. Exceeding this limit will result in a Timeout error.", alias="timeLimit")
    url: StrictStr = Field(description="Target for the test.")
    agents: List[TestAgent] = Field(description="A list of objects with `agentId` (required) and `sourceIpAddress` (optional).")
    credentials: Optional[List[StrictStr]] = Field(default=None, description="Contains a list of credential IDs (get `credentialId` from `/credentials` endpoint).")
    __properties: ClassVar[List[str]] = ["createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "labels", "sharedWithAccounts", "followRedirects", "mtuMeasurements", "networkMeasurements", "numPathTraces", "pathTraceMode", "predefinedVariables", "probeMode", "protocol", "requests", "sslVersionId", "targetTime", "timeLimit", "url", "agents", "credentials"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiInstantTestRequest from a JSON string"""
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
            "created_by",
            "created_date",
            "live_share",
            "modified_by",
            "modified_date",
            "saved_event",
            "test_id",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in predefined_variables (list)
        _items = []
        if self.predefined_variables:
            for _item in self.predefined_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['predefinedVariables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
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
        """Create an instance of ApiInstantTestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdBy": obj.get("createdBy"),
            "createdDate": obj.get("createdDate"),
            "description": obj.get("description"),
            "liveShare": obj.get("liveShare"),
            "modifiedBy": obj.get("modifiedBy"),
            "modifiedDate": obj.get("modifiedDate"),
            "savedEvent": obj.get("savedEvent"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "type": obj.get("type"),
            "_links": TestLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "labels": obj.get("labels"),
            "sharedWithAccounts": obj.get("sharedWithAccounts"),
            "followRedirects": obj.get("followRedirects") if obj.get("followRedirects") is not None else True,
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "pathTraceMode": obj.get("pathTraceMode"),
            "predefinedVariables": [ApiPredefinedVariable.from_dict(_item) for _item in obj["predefinedVariables"]] if obj.get("predefinedVariables") is not None else None,
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "requests": [ApiRequest.from_dict(_item) for _item in obj["requests"]] if obj.get("requests") is not None else None,
            "sslVersionId": obj.get("sslVersionId"),
            "targetTime": obj.get("targetTime"),
            "timeLimit": obj.get("timeLimit") if obj.get("timeLimit") is not None else 30,
            "url": obj.get("url"),
            "agents": [TestAgent.from_dict(_item) for _item in obj["agents"]] if obj.get("agents") is not None else None,
            "credentials": obj.get("credentials")
        })
        return _obj

