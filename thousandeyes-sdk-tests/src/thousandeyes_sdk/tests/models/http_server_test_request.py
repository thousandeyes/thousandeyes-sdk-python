# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.tests.models.agent_interfaces import AgentInterfaces
from thousandeyes_sdk.tests.models.o_auth import OAuth
from thousandeyes_sdk.tests.models.test_agent_request import TestAgentRequest
from thousandeyes_sdk.tests.models.test_auth_type import TestAuthType
from thousandeyes_sdk.tests.models.test_custom_headers import TestCustomHeaders
from thousandeyes_sdk.tests.models.test_interval import TestInterval
from thousandeyes_sdk.tests.models.test_ipv6_policy import TestIpv6Policy
from thousandeyes_sdk.tests.models.test_links import TestLinks
from thousandeyes_sdk.tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.tests.models.test_protocol import TestProtocol
from thousandeyes_sdk.tests.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class HttpServerTestRequest(BaseModel):
    """
    HttpServerTestRequest
    """ # noqa: E501
    interval: TestInterval
    alerts_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if alerts are enabled.", alias="alertsEnabled")
    enabled: Optional[StrictBool] = Field(default=True, description="Test is enabled.")
    alert_rules: Optional[List[StrictStr]] = Field(default=None, description="List of alert rules IDs to apply to the test (get `ruleId` from `/alerts/rules` endpoint. If `alertsEnabled` is set to `true` and `alertRules` is not included on test creation or update, applicable user default alert rules will be used)", alias="alertRules")
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
    labels: Optional[List[StrictStr]] = Field(default=None, description="Contains list of test label IDs (get `labelId` from `/labels` endpoint)")
    shared_with_accounts: Optional[List[StrictStr]] = Field(default=None, description="Contains list of account group IDs. Test is shared with the listed account groups (get `aid` from `/account-groups` endpoint)", alias="sharedWithAccounts")
    auth_type: Optional[TestAuthType] = Field(default=None, alias="authType")
    agent_interfaces: Optional[AgentInterfaces] = Field(default=None, alias="agentInterfaces")
    bandwidth_measurements: Optional[StrictBool] = Field(default=None, description="Set to `true` to enable bandwidth measurements, only applies to Enterprise agents assigned to the test.", alias="bandwidthMeasurements")
    client_certificate: Optional[StrictStr] = Field(default=None, description="String representation (containing newline characters) of client certificate, the private key must be placed first, then the certificate.", alias="clientCertificate")
    content_regex: Optional[StrictStr] = Field(default=None, description="Content regex, this field does not require escaping.", alias="contentRegex")
    custom_headers: Optional[TestCustomHeaders] = Field(default=None, alias="customHeaders")
    desired_status_code: Optional[StrictStr] = Field(default='200', description="Specify the HTTP status code value that indicates a successful response.", alias="desiredStatusCode")
    download_limit: Optional[StrictInt] = Field(default=None, description="Specifies maximum number of bytes to download from the target object.", alias="downloadLimit")
    dns_override: Optional[StrictStr] = Field(default=None, description="IP address to use for DNS override.", alias="dnsOverride")
    http_target_time: Optional[Annotated[int, Field(le=5000, strict=True, ge=100)]] = Field(default=None, description="Target time for HTTP server completion, specified in milliseconds.", alias="httpTargetTime")
    http_time_limit: Optional[Annotated[int, Field(le=60, strict=True, ge=5)]] = Field(default=5, description="HTTP time limit in seconds.", alias="httpTimeLimit")
    http_version: Optional[Annotated[int, Field(le=2, strict=True, ge=1)]] = Field(default=2, description="HTTP protocol version. Set to '2' to prefer HTTP/2, or '1' to use only HTTP/1.1.", alias="httpVersion")
    include_headers: Optional[StrictBool] = Field(default=True, description="Set to `true` to capture response headers for objects loaded by the test.", alias="includeHeaders")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    o_auth: Optional[OAuth] = Field(default=None, alias="oAuth")
    password: Optional[StrictStr] = Field(default=None, description="Password for Basic/NTLM authentication.")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    ssl_version: Optional[StrictStr] = Field(default=None, description="Reflects the verbose SSL protocol version used by a test.", alias="sslVersion")
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    url: StrictStr = Field(description="Target for the test.")
    use_ntlm: Optional[StrictBool] = Field(default=None, description="Set to true to use NTLM, false to use Basic Authentication. Requires username and password to be set.", alias="useNtlm")
    user_agent: Optional[StrictStr] = Field(default=None, description="User-agent string to be provided during the test.", alias="userAgent")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    verify_certificate: Optional[StrictBool] = Field(default=False, description="Ignore or acknowledge certificate errors. Set to false to ignore certificate errors.", alias="verifyCertificate")
    allow_unsafe_legacy_renegotiation: Optional[StrictBool] = Field(default=True, description="Allows TLS renegotiation with servers not supporting RFC 5746. Default Set to true to allow unsafe legacy renegotiation.", alias="allowUnsafeLegacyRenegotiation")
    follow_redirects: Optional[StrictBool] = Field(default=True, description="To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to `false`.", alias="followRedirects")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    override_agent_proxy: Optional[StrictBool] = Field(default=False, description="Flag indicating if a proxy other than the default should be used. To override the default proxy for agents, set to `true` and specify a value for `overrideProxyId`.", alias="overrideAgentProxy")
    override_proxy_id: Optional[StrictStr] = Field(default=None, description="ID of the proxy to be used if the default proxy is overridden.", alias="overrideProxyId")
    collect_proxy_network_data: Optional[StrictBool] = Field(default=False, description="Indicates whether network data to the proxy should be collected.", alias="collectProxyNetworkData")
    headers: Optional[List[StrictStr]] = Field(default=None, description="HTTP request headers used.")
    post_body: Optional[StrictStr] = Field(default=None, description="Enter the body for the HTTP POST request in this field. No special escaping is necessary. If the post body is provided with content, the `requestMethod` is automatically set to POST.", alias="postBody")
    ipv6_policy: Optional[TestIpv6Policy] = Field(default=None, alias="ipv6Policy")
    bgp_measurements: Optional[StrictBool] = Field(default=True, description="Set to `true` to enable bgp measurements.", alias="bgpMeasurements")
    use_public_bgp: Optional[StrictBool] = Field(default=True, description="Indicate if all available public BGP monitors should be used, when ommited defaults to `bgpMeasurements` value.", alias="usePublicBgp")
    monitors: Optional[List[StrictStr]] = Field(default=None, description="Contains list of BGP monitor IDs (get `monitorId` from `/monitors` endpoint)")
    agents: List[TestAgentRequest] = Field(description="Contains list of Agent IDs (get `agentId` from `/agents` endpoint).")
    __properties: ClassVar[List[str]] = ["interval", "alertsEnabled", "enabled", "alertRules", "createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "labels", "sharedWithAccounts", "authType", "agentInterfaces", "bandwidthMeasurements", "clientCertificate", "contentRegex", "customHeaders", "desiredStatusCode", "downloadLimit", "dnsOverride", "httpTargetTime", "httpTimeLimit", "httpVersion", "includeHeaders", "mtuMeasurements", "networkMeasurements", "numPathTraces", "oAuth", "password", "pathTraceMode", "probeMode", "protocol", "sslVersion", "sslVersionId", "url", "useNtlm", "userAgent", "username", "verifyCertificate", "allowUnsafeLegacyRenegotiation", "followRedirects", "fixedPacketRate", "overrideAgentProxy", "overrideProxyId", "collectProxyNetworkData", "headers", "postBody", "ipv6Policy", "bgpMeasurements", "usePublicBgp", "monitors", "agents"]

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
        """Create an instance of HttpServerTestRequest from a JSON string"""
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
            "ssl_version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent_interfaces
        if self.agent_interfaces:
            _dict['agentInterfaces'] = self.agent_interfaces.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_headers
        if self.custom_headers:
            _dict['customHeaders'] = self.custom_headers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of o_auth
        if self.o_auth:
            _dict['oAuth'] = self.o_auth.to_dict()
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
        """Create an instance of HttpServerTestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interval": obj.get("interval"),
            "alertsEnabled": obj.get("alertsEnabled"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "alertRules": obj.get("alertRules"),
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
            "authType": obj.get("authType"),
            "agentInterfaces": AgentInterfaces.from_dict(obj["agentInterfaces"]) if obj.get("agentInterfaces") is not None else None,
            "bandwidthMeasurements": obj.get("bandwidthMeasurements"),
            "clientCertificate": obj.get("clientCertificate"),
            "contentRegex": obj.get("contentRegex"),
            "customHeaders": TestCustomHeaders.from_dict(obj["customHeaders"]) if obj.get("customHeaders") is not None else None,
            "desiredStatusCode": obj.get("desiredStatusCode") if obj.get("desiredStatusCode") is not None else '200',
            "downloadLimit": obj.get("downloadLimit"),
            "dnsOverride": obj.get("dnsOverride"),
            "httpTargetTime": obj.get("httpTargetTime"),
            "httpTimeLimit": obj.get("httpTimeLimit") if obj.get("httpTimeLimit") is not None else 5,
            "httpVersion": obj.get("httpVersion") if obj.get("httpVersion") is not None else 2,
            "includeHeaders": obj.get("includeHeaders") if obj.get("includeHeaders") is not None else True,
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "oAuth": OAuth.from_dict(obj["oAuth"]) if obj.get("oAuth") is not None else None,
            "password": obj.get("password"),
            "pathTraceMode": obj.get("pathTraceMode"),
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "sslVersion": obj.get("sslVersion"),
            "sslVersionId": obj.get("sslVersionId"),
            "url": obj.get("url"),
            "useNtlm": obj.get("useNtlm"),
            "userAgent": obj.get("userAgent"),
            "username": obj.get("username"),
            "verifyCertificate": obj.get("verifyCertificate") if obj.get("verifyCertificate") is not None else False,
            "allowUnsafeLegacyRenegotiation": obj.get("allowUnsafeLegacyRenegotiation") if obj.get("allowUnsafeLegacyRenegotiation") is not None else True,
            "followRedirects": obj.get("followRedirects") if obj.get("followRedirects") is not None else True,
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "overrideAgentProxy": obj.get("overrideAgentProxy") if obj.get("overrideAgentProxy") is not None else False,
            "overrideProxyId": obj.get("overrideProxyId"),
            "collectProxyNetworkData": obj.get("collectProxyNetworkData") if obj.get("collectProxyNetworkData") is not None else False,
            "headers": obj.get("headers"),
            "postBody": obj.get("postBody"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "bgpMeasurements": obj.get("bgpMeasurements") if obj.get("bgpMeasurements") is not None else True,
            "usePublicBgp": obj.get("usePublicBgp") if obj.get("usePublicBgp") is not None else True,
            "monitors": obj.get("monitors"),
            "agents": [TestAgentRequest.from_dict(_item) for _item in obj["agents"]] if obj.get("agents") is not None else None
        })
        return _obj

