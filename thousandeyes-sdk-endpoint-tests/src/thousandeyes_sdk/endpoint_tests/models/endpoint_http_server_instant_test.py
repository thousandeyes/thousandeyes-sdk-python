# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_agent_selector_type import EndpointTestAgentSelectorType
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_auth_type import EndpointTestAuthType
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_tests.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_tests.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class EndpointHttpServerInstantTest(BaseModel):
    """
    EndpointHttpServerInstantTest
    """ # noqa: E501
    agent_selector_type: EndpointTestAgentSelectorType = Field(alias="agentSelectorType")
    agents: Optional[List[StrictStr]] = Field(default=None, description="List of endpoint agent IDs (obtained from `/endpoint/agents` endpoint). Required when `agentSelectorType` is set to `specific-agent`.")
    has_ping: Optional[StrictBool] = Field(default=True, description="Optional flag indicating if the test should run ping.", alias="hasPing")
    has_traceroute: Optional[StrictBool] = Field(default=True, description="Optional flag indicating if the test should run traceroute.", alias="hasTraceroute")
    endpoint_agent_labels: Optional[List[StrictStr]] = Field(default=None, description="List of endpoint agent label IDs (obtained from `/endpoint/labels` endpoint), required when `agentSelectorType` is set to `agent-labels`.", alias="endpointAgentLabels")
    max_machines: Annotated[int, Field(le=50000, strict=True, ge=1)] = Field(description="Maximum number of agents which can execute the test.", alias="maxMachines")
    port: Optional[StrictInt] = Field(default=None, description="Port number, if not specified, the port is selected based on a protocol (HTTP 80, HTTPS 443).")
    test_name: StrictStr = Field(description="Name of the test.", alias="testName")
    auth_type: Optional[EndpointTestAuthType] = Field(default=None, alias="authType")
    has_path_trace_in_session: Optional[StrictBool] = Field(default=None, description="Enables \"in session\" path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session.", alias="hasPathTraceInSession")
    http_time_limit: StrictInt = Field(description="Maximum amount of time in milliseconds the agents wait before a request times out.", alias="httpTimeLimit")
    protocol: Optional[EndpointTestProtocol] = None
    url: StrictStr = Field(description="Test target URL. Optionally, you can specify a protocol (http or https). If no protocol is provided, the default `https` protocol is used.")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    ssl_version_id: TestSslVersionId = Field(alias="sslVersionId")
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    verify_certificate: StrictBool = Field(description="Flag indicating if a certificate should be verified.", alias="verifyCertificate")
    target_response_time: StrictInt = Field(description="Response time target in milliseconds. Affects the colors of agents and legends on the view page. The value is compared with actual response time in order to determine the color scale (from green to red).", alias="targetResponseTime")
    password: Optional[StrictStr] = Field(default=None, description="Password for Basic/NTLM authentication.")
    __properties: ClassVar[List[str]] = ["agentSelectorType", "agents", "hasPing", "hasTraceroute", "endpointAgentLabels", "maxMachines", "port", "testName", "authType", "hasPathTraceInSession", "httpTimeLimit", "protocol", "url", "username", "sslVersionId", "tcpProbeMode", "verifyCertificate", "targetResponseTime", "password"]

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
        """Create an instance of EndpointHttpServerInstantTest from a JSON string"""
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
        """Create an instance of EndpointHttpServerInstantTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentSelectorType": obj.get("agentSelectorType"),
            "agents": obj.get("agents"),
            "hasPing": obj.get("hasPing") if obj.get("hasPing") is not None else True,
            "hasTraceroute": obj.get("hasTraceroute") if obj.get("hasTraceroute") is not None else True,
            "endpointAgentLabels": obj.get("endpointAgentLabels"),
            "maxMachines": obj.get("maxMachines"),
            "port": obj.get("port"),
            "testName": obj.get("testName"),
            "authType": obj.get("authType"),
            "hasPathTraceInSession": obj.get("hasPathTraceInSession"),
            "httpTimeLimit": obj.get("httpTimeLimit"),
            "protocol": obj.get("protocol"),
            "url": obj.get("url"),
            "username": obj.get("username"),
            "sslVersionId": obj.get("sslVersionId"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "verifyCertificate": obj.get("verifyCertificate"),
            "targetResponseTime": obj.get("targetResponseTime"),
            "password": obj.get("password")
        })
        return _obj


