# coding: utf-8

# flake8: noqa
"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.endpoint_test_results.models.alert_direction import AlertDirection
from thousandeyes_sdk.endpoint_test_results.models.alert_rounds_violation_mode import AlertRoundsViolationMode
from thousandeyes_sdk.endpoint_test_results.models.alert_rule import AlertRule
from thousandeyes_sdk.endpoint_test_results.models.alert_type import AlertType
from thousandeyes_sdk.endpoint_test_results.models.application_score_quality import ApplicationScoreQuality
from thousandeyes_sdk.endpoint_test_results.models.asn_details import AsnDetails
from thousandeyes_sdk.endpoint_test_results.models.conditional_operator import ConditionalOperator
from thousandeyes_sdk.endpoint_test_results.models.cpu_utilization import CpuUtilization
from thousandeyes_sdk.endpoint_test_results.models.dynamic_base_test_result import DynamicBaseTestResult
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test import DynamicTest
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_links import DynamicTestLinks
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_self_link import DynamicTestSelfLink
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_webex import DynamicTestWebex
from thousandeyes_sdk.endpoint_test_results.models.dynamic_tests_data_round_search import DynamicTestsDataRoundSearch
from thousandeyes_sdk.endpoint_test_results.models.dynamic_tests_data_search_filter import DynamicTestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_browser import EndpointBrowser
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_data_point_score import EndpointHttpDataPointScore
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_server_base_test import EndpointHttpServerBaseTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_server_test import EndpointHttpServerTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request import EndpointNetworkTopologyResultRequest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request_filter import EndpointNetworkTopologyResultRequestFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_ping_data_point_score import EndpointPingDataPointScore
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test import EndpointRealUserTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_base import EndpointRealUserTestBase
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_detail import EndpointRealUserTestDetail
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_detail_results import EndpointRealUserTestDetailResults
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_result_request_filter import EndpointRealUserTestResultRequestFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_results import EndpointRealUserTestResults
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_results_request import EndpointRealUserTestResultsRequest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_result_request_filter import EndpointResultRequestFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_scheduled_test import EndpointScheduledTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_scheduled_test_type import EndpointScheduledTestType
from thousandeyes_sdk.endpoint_test_results.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test import EndpointTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_auth_type import EndpointTestAuthType
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_links import EndpointTestLinks
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_self_link import EndpointTestSelfLink
from thousandeyes_sdk.endpoint_test_results.models.error import Error
from thousandeyes_sdk.endpoint_test_results.models.ethernet_profile import EthernetProfile
from thousandeyes_sdk.endpoint_test_results.models.expand import Expand
from thousandeyes_sdk.endpoint_test_results.models.gateway_network_ping import GatewayNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.hop import Hop
from thousandeyes_sdk.endpoint_test_results.models.http_error_type import HttpErrorType
from thousandeyes_sdk.endpoint_test_results.models.http_test_result import HttpTestResult
from thousandeyes_sdk.endpoint_test_results.models.http_test_result_headers import HttpTestResultHeaders
from thousandeyes_sdk.endpoint_test_results.models.http_test_results import HttpTestResults
from thousandeyes_sdk.endpoint_test_results.models.interface_hardware_type import InterfaceHardwareType
from thousandeyes_sdk.endpoint_test_results.models.link import Link
from thousandeyes_sdk.endpoint_test_results.models.local_network_result import LocalNetworkResult
from thousandeyes_sdk.endpoint_test_results.models.local_network_results import LocalNetworkResults
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_detail_results import LocalNetworkTopologyDetailResults
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_result import LocalNetworkTopologyResult
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_result_base import LocalNetworkTopologyResultBase
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_results import LocalNetworkTopologyResults
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_network_test_results import MultiTestIdNetworkTestResults
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_tests_data_rounds_search import MultiTestIdTestsDataRoundsSearch
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_tests_data_search_filter import MultiTestIdTestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.network_dynamic_test_result import NetworkDynamicTestResult
from thousandeyes_sdk.endpoint_test_results.models.network_dynamic_test_results import NetworkDynamicTestResults
from thousandeyes_sdk.endpoint_test_results.models.network_interface import NetworkInterface
from thousandeyes_sdk.endpoint_test_results.models.network_metrics import NetworkMetrics
from thousandeyes_sdk.endpoint_test_results.models.network_ping import NetworkPing
from thousandeyes_sdk.endpoint_test_results.models.network_profile import NetworkProfile
from thousandeyes_sdk.endpoint_test_results.models.network_proxy import NetworkProxy
from thousandeyes_sdk.endpoint_test_results.models.network_proxy_profile import NetworkProxyProfile
from thousandeyes_sdk.endpoint_test_results.models.network_test_result import NetworkTestResult
from thousandeyes_sdk.endpoint_test_results.models.network_test_results import NetworkTestResults
from thousandeyes_sdk.endpoint_test_results.models.network_topology_type import NetworkTopologyType
from thousandeyes_sdk.endpoint_test_results.models.network_wireless_profile import NetworkWirelessProfile
from thousandeyes_sdk.endpoint_test_results.models.pagination_next_and_self_link import PaginationNextAndSelfLink
from thousandeyes_sdk.endpoint_test_results.models.pagination_next_link import PaginationNextLink
from thousandeyes_sdk.endpoint_test_results.models.path_vis_base_test_result import PathVisBaseTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_dynamic_test_result import PathVisDetailDynamicTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_dynamic_test_results import PathVisDetailDynamicTestResults
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_test_result import PathVisDetailTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_test_results import PathVisDetailTestResults
from thousandeyes_sdk.endpoint_test_results.models.path_vis_dynamic_test_result import PathVisDynamicTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_dynamic_test_results import PathVisDynamicTestResults
from thousandeyes_sdk.endpoint_test_results.models.path_vis_endpoint import PathVisEndpoint
from thousandeyes_sdk.endpoint_test_results.models.path_vis_hop import PathVisHop
from thousandeyes_sdk.endpoint_test_results.models.path_vis_route import PathVisRoute
from thousandeyes_sdk.endpoint_test_results.models.path_vis_test_result import PathVisTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_test_results import PathVisTestResults
from thousandeyes_sdk.endpoint_test_results.models.physical_memory_used_bytes import PhysicalMemoryUsedBytes
from thousandeyes_sdk.endpoint_test_results.models.platform import Platform
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_coordinates import RealUserTestCoordinates
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_network import RealUserTestNetwork
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_network_result import RealUserTestNetworkResult
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_network_results import RealUserTestNetworkResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page import RealUserTestPage
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page_detail_result import RealUserTestPageDetailResult
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page_result import RealUserTestPageResult
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page_results import RealUserTestPageResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page_timings import RealUserTestPageTimings
from thousandeyes_sdk.endpoint_test_results.models.self_links import SelfLinks
from thousandeyes_sdk.endpoint_test_results.models.severity import Severity
from thousandeyes_sdk.endpoint_test_results.models.sort_order import SortOrder
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from thousandeyes_sdk.endpoint_test_results.models.target_network_ping import TargetNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.target_profile import TargetProfile
from thousandeyes_sdk.endpoint_test_results.models.target_traceroute import TargetTraceroute
from thousandeyes_sdk.endpoint_test_results.models.tcp_connect import TcpConnect
from thousandeyes_sdk.endpoint_test_results.models.test_interval import TestInterval
from thousandeyes_sdk.endpoint_test_results.models.test_label import TestLabel
from thousandeyes_sdk.endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.test_protocol import TestProtocol
from thousandeyes_sdk.endpoint_test_results.models.test_result import TestResult
from thousandeyes_sdk.endpoint_test_results.models.test_ssl_version_id import TestSslVersionId
from thousandeyes_sdk.endpoint_test_results.models.tests_data_rounds_search import TestsDataRoundsSearch
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_filter import TestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_sort import TestsDataSearchSort
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_sort_key import TestsDataSearchSortKey
from thousandeyes_sdk.endpoint_test_results.models.tests_data_threshold_filter import TestsDataThresholdFilter
from thousandeyes_sdk.endpoint_test_results.models.tests_data_threshold_filters import TestsDataThresholdFilters
from thousandeyes_sdk.endpoint_test_results.models.threshold_filter_name import ThresholdFilterName
from thousandeyes_sdk.endpoint_test_results.models.threshold_filter_operator import ThresholdFilterOperator
from thousandeyes_sdk.endpoint_test_results.models.traceroute import Traceroute
from thousandeyes_sdk.endpoint_test_results.models.traceroute_hop import TracerouteHop
from thousandeyes_sdk.endpoint_test_results.models.trigger import Trigger
from thousandeyes_sdk.endpoint_test_results.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.endpoint_test_results.models.validation_error import ValidationError
from thousandeyes_sdk.endpoint_test_results.models.validation_error_item import ValidationErrorItem
from thousandeyes_sdk.endpoint_test_results.models.vpn_network_ping import VpnNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.vpn_profile import VpnProfile
from thousandeyes_sdk.endpoint_test_results.models.vpn_traceroute import VpnTraceroute
from thousandeyes_sdk.endpoint_test_results.models.vpn_type import VpnType
