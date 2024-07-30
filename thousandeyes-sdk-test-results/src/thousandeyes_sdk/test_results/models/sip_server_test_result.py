# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from thousandeyes_sdk.test_results.models.agent import Agent
from thousandeyes_sdk.test_results.models.sip_server_error_type import SipServerErrorType
from thousandeyes_sdk.test_results.models.test_result_app_links import TestResultAppLinks
from typing import Optional, Set
from typing_extensions import Self

class SipServerTestResult(BaseModel):
    """
    SipServerTestResult
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Data point date UTC (ISO date-time format).", alias="date")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="roundId")
    links: Optional[TestResultAppLinks] = Field(default=None, alias="_links")
    start_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="startTime")
    end_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the end time of the round", alias="endTime")
    server_ip: Optional[StrictStr] = Field(default=None, description="Target agent IP address", alias="serverIp")
    agent: Optional[Agent] = None
    availability: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="availability of the service")
    connect_time: Optional[StrictInt] = Field(default=None, description="Time required to establish a TCP connection to the server in milliseconds, only available when TCP is configured as protocol", alias="connectTime")
    dns_time: Optional[StrictInt] = Field(default=None, description="Time required to resolve DNS in milliseconds", alias="dnsTime")
    invite_time: Optional[StrictInt] = Field(default=None, description="Time to complete INVITE in milliseconds", alias="inviteTime")
    options_time: Optional[StrictInt] = Field(default=None, description="Time to complete OPTIONS in milliseconds", alias="optionsTime")
    num_redirects: Optional[StrictInt] = Field(default=None, description="Number of redirects", alias="numRedirects")
    options_request: Optional[StrictStr] = Field(default=None, description="Entire OPTIONS request", alias="optionsRequest")
    options_response: Optional[StrictStr] = Field(default=None, description="Entire OPTIONS response", alias="optionsResponse")
    register_time: Optional[StrictInt] = Field(default=None, description="Time to complete REGISTER in milliseconds", alias="registerTime")
    response_code: Optional[StrictInt] = Field(default=None, description="SIP server response code", alias="responseCode")
    response_time: Optional[StrictInt] = Field(default=None, description="Time to first byte", alias="responseTime")
    total_time: Optional[StrictInt] = Field(default=None, description="Total time", alias="totalTime")
    wait_time: Optional[StrictInt] = Field(default=None, description="Time elapsed between completion of request and first byte of response", alias="waitTime")
    error_type: Optional[SipServerErrorType] = Field(default=None, alias="errorType")
    problem_detail: Optional[StrictStr] = Field(default=None, description="Error details, if an error was encountered", alias="problemDetail")
    __properties: ClassVar[List[str]] = ["date", "roundId", "_links", "startTime", "endTime", "serverIp", "agent", "availability", "connectTime", "dnsTime", "inviteTime", "optionsTime", "numRedirects", "optionsRequest", "optionsResponse", "registerTime", "responseCode", "responseTime", "totalTime", "waitTime", "errorType", "problemDetail"]

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
        """Create an instance of SipServerTestResult from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "var_date",
            "round_id",
            "start_time",
            "end_time",
            "server_ip",
            "availability",
            "connect_time",
            "dns_time",
            "invite_time",
            "options_time",
            "num_redirects",
            "options_request",
            "options_response",
            "register_time",
            "response_code",
            "response_time",
            "total_time",
            "wait_time",
            "problem_detail",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent
        if self.agent:
            _dict['agent'] = self.agent.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SipServerTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "roundId": obj.get("roundId"),
            "_links": TestResultAppLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "serverIp": obj.get("serverIp"),
            "agent": Agent.from_dict(obj["agent"]) if obj.get("agent") is not None else None,
            "availability": obj.get("availability"),
            "connectTime": obj.get("connectTime"),
            "dnsTime": obj.get("dnsTime"),
            "inviteTime": obj.get("inviteTime"),
            "optionsTime": obj.get("optionsTime"),
            "numRedirects": obj.get("numRedirects"),
            "optionsRequest": obj.get("optionsRequest"),
            "optionsResponse": obj.get("optionsResponse"),
            "registerTime": obj.get("registerTime"),
            "responseCode": obj.get("responseCode"),
            "responseTime": obj.get("responseTime"),
            "totalTime": obj.get("totalTime"),
            "waitTime": obj.get("waitTime"),
            "errorType": obj.get("errorType"),
            "problemDetail": obj.get("problemDetail")
        })
        return _obj


