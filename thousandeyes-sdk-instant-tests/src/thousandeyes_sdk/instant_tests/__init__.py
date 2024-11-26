# coding: utf-8

# flake8: noqa

"""
    Instant Tests API

    The Instant Tests API operations lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import apis into sdk package
from thousandeyes_sdk.instant_tests.api.api_instant_tests_api import APIInstantTestsApi
from thousandeyes_sdk.instant_tests.api.agent_to_agent_instant_tests_api import AgentToAgentInstantTestsApi
from thousandeyes_sdk.instant_tests.api.agent_to_server_instant_tests_api import AgentToServerInstantTestsApi
from thousandeyes_sdk.instant_tests.api.dnssec_instant_tests_api import DNSSECInstantTestsApi
from thousandeyes_sdk.instant_tests.api.dns_server_instant_tests_api import DNSServerInstantTestsApi
from thousandeyes_sdk.instant_tests.api.dns_trace_instant_tests_api import DNSTraceInstantTestsApi
from thousandeyes_sdk.instant_tests.api.ftp_server_instant_tests_api import FTPServerInstantTestsApi
from thousandeyes_sdk.instant_tests.api.http_page_load_instant_tests_api import HTTPPageLoadInstantTestsApi
from thousandeyes_sdk.instant_tests.api.http_server_instant_tests_api import HTTPServerInstantTestsApi
from thousandeyes_sdk.instant_tests.api.instant_tests_api import InstantTestsApi
from thousandeyes_sdk.instant_tests.api.sip_server_instant_tests_api import SIPServerInstantTestsApi
from thousandeyes_sdk.instant_tests.api.voice_instant_tests_api import VoiceInstantTestsApi
from thousandeyes_sdk.instant_tests.api.web_transaction_instant_tests_api import WebTransactionInstantTestsApi


# import models into sdk package
from thousandeyes_sdk.instant_tests.models.agent_base import AgentBase
from thousandeyes_sdk.instant_tests.models.agent_interfaces import AgentInterfaces
from thousandeyes_sdk.instant_tests.models.agent_response import AgentResponse
from thousandeyes_sdk.instant_tests.models.agent_to_agent_instant_test import AgentToAgentInstantTest
from thousandeyes_sdk.instant_tests.models.agent_to_agent_instant_test_request import AgentToAgentInstantTestRequest
from thousandeyes_sdk.instant_tests.models.agent_to_agent_instant_test_response import AgentToAgentInstantTestResponse
from thousandeyes_sdk.instant_tests.models.agent_to_agent_properties import AgentToAgentProperties
from thousandeyes_sdk.instant_tests.models.agent_to_agent_test_protocol import AgentToAgentTestProtocol
from thousandeyes_sdk.instant_tests.models.agent_to_server_instant_test import AgentToServerInstantTest
from thousandeyes_sdk.instant_tests.models.agent_to_server_instant_test_request import AgentToServerInstantTestRequest
from thousandeyes_sdk.instant_tests.models.agent_to_server_instant_test_response import AgentToServerInstantTestResponse
from thousandeyes_sdk.instant_tests.models.agent_to_server_properties import AgentToServerProperties
from thousandeyes_sdk.instant_tests.models.api_client_authentication import ApiClientAuthentication
from thousandeyes_sdk.instant_tests.models.api_instant_test import ApiInstantTest
from thousandeyes_sdk.instant_tests.models.api_instant_test_request import ApiInstantTestRequest
from thousandeyes_sdk.instant_tests.models.api_instant_test_response import ApiInstantTestResponse
from thousandeyes_sdk.instant_tests.models.api_predefined_variable import ApiPredefinedVariable
from thousandeyes_sdk.instant_tests.models.api_properties import ApiProperties
from thousandeyes_sdk.instant_tests.models.api_request import ApiRequest
from thousandeyes_sdk.instant_tests.models.api_request_assertion import ApiRequestAssertion
from thousandeyes_sdk.instant_tests.models.api_request_assertion_name import ApiRequestAssertionName
from thousandeyes_sdk.instant_tests.models.api_request_assertion_operator import ApiRequestAssertionOperator
from thousandeyes_sdk.instant_tests.models.api_request_auth_type import ApiRequestAuthType
from thousandeyes_sdk.instant_tests.models.api_request_header import ApiRequestHeader
from thousandeyes_sdk.instant_tests.models.api_request_method import ApiRequestMethod
from thousandeyes_sdk.instant_tests.models.api_request_variable import ApiRequestVariable
from thousandeyes_sdk.instant_tests.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType
from thousandeyes_sdk.instant_tests.models.dns_query_class import DnsQueryClass
from thousandeyes_sdk.instant_tests.models.dns_sec_instant_test import DnsSecInstantTest
from thousandeyes_sdk.instant_tests.models.dns_sec_instant_test_request import DnsSecInstantTestRequest
from thousandeyes_sdk.instant_tests.models.dns_sec_instant_test_response import DnsSecInstantTestResponse
from thousandeyes_sdk.instant_tests.models.dns_sec_properties import DnsSecProperties
from thousandeyes_sdk.instant_tests.models.dns_server_instant_test import DnsServerInstantTest
from thousandeyes_sdk.instant_tests.models.dns_server_instant_test_request import DnsServerInstantTestRequest
from thousandeyes_sdk.instant_tests.models.dns_server_instant_test_response import DnsServerInstantTestResponse
from thousandeyes_sdk.instant_tests.models.dns_server_properties import DnsServerProperties
from thousandeyes_sdk.instant_tests.models.dns_servers_request import DnsServersRequest
from thousandeyes_sdk.instant_tests.models.dns_trace_instant_test import DnsTraceInstantTest
from thousandeyes_sdk.instant_tests.models.dns_trace_instant_test_request import DnsTraceInstantTestRequest
from thousandeyes_sdk.instant_tests.models.dns_trace_instant_test_response import DnsTraceInstantTestResponse
from thousandeyes_sdk.instant_tests.models.dns_trace_properties import DnsTraceProperties
from thousandeyes_sdk.instant_tests.models.error import Error
from thousandeyes_sdk.instant_tests.models.expand_instant_test_options import ExpandInstantTestOptions
from thousandeyes_sdk.instant_tests.models.ftp_server_instant_test import FtpServerInstantTest
from thousandeyes_sdk.instant_tests.models.ftp_server_instant_test_request import FtpServerInstantTestRequest
from thousandeyes_sdk.instant_tests.models.ftp_server_instant_test_response import FtpServerInstantTestResponse
from thousandeyes_sdk.instant_tests.models.ftp_server_properties import FtpServerProperties
from thousandeyes_sdk.instant_tests.models.ftp_server_request_type import FtpServerRequestType
from thousandeyes_sdk.instant_tests.models.http_server_base_properties import HttpServerBaseProperties
from thousandeyes_sdk.instant_tests.models.http_server_instant_test import HttpServerInstantTest
from thousandeyes_sdk.instant_tests.models.http_server_instant_test_request import HttpServerInstantTestRequest
from thousandeyes_sdk.instant_tests.models.http_server_instant_test_response import HttpServerInstantTestResponse
from thousandeyes_sdk.instant_tests.models.http_server_properties import HttpServerProperties
from thousandeyes_sdk.instant_tests.models.instant_test import InstantTest
from thousandeyes_sdk.instant_tests.models.instant_test_request import InstantTestRequest
from thousandeyes_sdk.instant_tests.models.link import Link
from thousandeyes_sdk.instant_tests.models.o_auth import OAuth
from thousandeyes_sdk.instant_tests.models.page_load_instant_test import PageLoadInstantTest
from thousandeyes_sdk.instant_tests.models.page_load_instant_test_request import PageLoadInstantTestRequest
from thousandeyes_sdk.instant_tests.models.page_load_instant_test_response import PageLoadInstantTestResponse
from thousandeyes_sdk.instant_tests.models.page_load_properties import PageLoadProperties
from thousandeyes_sdk.instant_tests.models.request_method import RequestMethod
from thousandeyes_sdk.instant_tests.models.shared_with_account import SharedWithAccount
from thousandeyes_sdk.instant_tests.models.simple_agent import SimpleAgent
from thousandeyes_sdk.instant_tests.models.sip_server_instant_test import SipServerInstantTest
from thousandeyes_sdk.instant_tests.models.sip_server_instant_test_request import SipServerInstantTestRequest
from thousandeyes_sdk.instant_tests.models.sip_server_instant_test_response import SipServerInstantTestResponse
from thousandeyes_sdk.instant_tests.models.sip_server_properties import SipServerProperties
from thousandeyes_sdk.instant_tests.models.sip_test_protocol import SipTestProtocol
from thousandeyes_sdk.instant_tests.models.test_agent import TestAgent
from thousandeyes_sdk.instant_tests.models.test_auth_type import TestAuthType
from thousandeyes_sdk.instant_tests.models.test_custom_headers import TestCustomHeaders
from thousandeyes_sdk.instant_tests.models.test_direction import TestDirection
from thousandeyes_sdk.instant_tests.models.test_dns_server import TestDnsServer
from thousandeyes_sdk.instant_tests.models.test_dns_transport_protocol import TestDnsTransportProtocol
from thousandeyes_sdk.instant_tests.models.test_dscp_id import TestDscpId
from thousandeyes_sdk.instant_tests.models.test_ipv6_policy import TestIpv6Policy
from thousandeyes_sdk.instant_tests.models.test_label import TestLabel
from thousandeyes_sdk.instant_tests.models.test_links import TestLinks
from thousandeyes_sdk.instant_tests.models.test_page_loading_strategy import TestPageLoadingStrategy
from thousandeyes_sdk.instant_tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.instant_tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.instant_tests.models.test_protocol import TestProtocol
from thousandeyes_sdk.instant_tests.models.test_self_link import TestSelfLink
from thousandeyes_sdk.instant_tests.models.test_sip_credentials import TestSipCredentials
from thousandeyes_sdk.instant_tests.models.test_ssl_version_id import TestSslVersionId
from thousandeyes_sdk.instant_tests.models.test_type import TestType
from thousandeyes_sdk.instant_tests.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.instant_tests.models.unexpanded_instant_test import UnexpandedInstantTest
from thousandeyes_sdk.instant_tests.models.validation_error import ValidationError
from thousandeyes_sdk.instant_tests.models.validation_error_item import ValidationErrorItem
from thousandeyes_sdk.instant_tests.models.voice_instant_test import VoiceInstantTest
from thousandeyes_sdk.instant_tests.models.voice_instant_test_request import VoiceInstantTestRequest
from thousandeyes_sdk.instant_tests.models.voice_instant_test_response import VoiceInstantTestResponse
from thousandeyes_sdk.instant_tests.models.voice_properties import VoiceProperties
from thousandeyes_sdk.instant_tests.models.web_transaction_instant_test import WebTransactionInstantTest
from thousandeyes_sdk.instant_tests.models.web_transaction_instant_test_request import WebTransactionInstantTestRequest
from thousandeyes_sdk.instant_tests.models.web_transaction_instant_test_response import WebTransactionInstantTestResponse
from thousandeyes_sdk.instant_tests.models.web_transaction_properties import WebTransactionProperties
