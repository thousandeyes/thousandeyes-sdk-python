# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DashboardMetric(str, Enum):
    """
    Indicates the specific metric in the report, determined by the layer, test type, and metric values.
    """

    """
    allowed enum values
    """
    ONE_WAY_NET_LOSS_TO_TARGET = 'ONE_WAY_NET_LOSS_TO_TARGET'
    ONE_WAY_NET_LATENCY_TO_TARGET = 'ONE_WAY_NET_LATENCY_TO_TARGET'
    ONE_WAY_NET_JITTER_TO_TARGET = 'ONE_WAY_NET_JITTER_TO_TARGET'
    ONE_WAY_NET_THROUGHPUT_TO_TARGET = 'ONE_WAY_NET_THROUGHPUT_TO_TARGET'
    ONE_WAY_NET_ERROR_TO_TARGET = 'ONE_WAY_NET_ERROR_TO_TARGET'
    ONE_WAY_NET_LOSS_FROM_TARGET = 'ONE_WAY_NET_LOSS_FROM_TARGET'
    ONE_WAY_NET_LATENCY_FROM_TARGET = 'ONE_WAY_NET_LATENCY_FROM_TARGET'
    ONE_WAY_NET_JITTER_FROM_TARGET = 'ONE_WAY_NET_JITTER_FROM_TARGET'
    ONE_WAY_NET_THROUGHPUT_FROM_TARGET = 'ONE_WAY_NET_THROUGHPUT_FROM_TARGET'
    ONE_WAY_NET_ERROR_FROM_TARGET = 'ONE_WAY_NET_ERROR_FROM_TARGET'
    ONE_WAY_NET_LOSS_BIDIRECTIONAL = 'ONE_WAY_NET_LOSS_BIDIRECTIONAL'
    ONE_WAY_NET_LATENCY_BIDIRECTIONAL = 'ONE_WAY_NET_LATENCY_BIDIRECTIONAL'
    ONE_WAY_NET_JITTER_BIDIRECTIONAL = 'ONE_WAY_NET_JITTER_BIDIRECTIONAL'
    ONE_WAY_NET_THROUGHPUT_BIDIRECTIONAL = 'ONE_WAY_NET_THROUGHPUT_BIDIRECTIONAL'
    ONE_WAY_NET_ERROR_BIDIRECTIONAL = 'ONE_WAY_NET_ERROR_BIDIRECTIONAL'
    NET_LOSS = 'NET_LOSS'
    NET_LATENCY = 'NET_LATENCY'
    NET_JITTER = 'NET_JITTER'
    NET_BANDWIDTH = 'NET_BANDWIDTH'
    NET_CAPACITY = 'NET_CAPACITY'
    PROXY_NET_LOSS = 'PROXY_NET_LOSS'
    PROXY_NET_LATENCY = 'PROXY_NET_LATENCY'
    PROXY_NET_JITTER = 'PROXY_NET_JITTER'
    WEB_AVAILABILITY = 'WEB_AVAILABILITY'
    WEB_THROUGHPUT = 'WEB_THROUGHPUT'
    WEB_DNS = 'WEB_DNS'
    WEB_CONNECT = 'WEB_CONNECT'
    WEB_SSL = 'WEB_SSL'
    WEB_WAIT = 'WEB_WAIT'
    WEB_TTFB = 'WEB_TTFB'
    WEB_RECEIVE = 'WEB_RECEIVE'
    WEB_REDIRECT = 'WEB_REDIRECT'
    WEB_FETCH = 'WEB_FETCH'
    WEB_AUTHENTICATION_ERROR_COUNT = 'WEB_AUTHENTICATION_ERROR_COUNT'
    WEB_DNS_ERROR_COUNT = 'WEB_DNS_ERROR_COUNT'
    WEB_CONNECT_ERROR_COUNT = 'WEB_CONNECT_ERROR_COUNT'
    WEB_SSL_ERROR_COUNT = 'WEB_SSL_ERROR_COUNT'
    WEB_SEND_ERROR_COUNT = 'WEB_SEND_ERROR_COUNT'
    WEB_RECEIVE_ERROR_COUNT = 'WEB_RECEIVE_ERROR_COUNT'
    WEB_HTTP_ERROR_COUNT = 'WEB_HTTP_ERROR_COUNT'
    WEB_CONTENT_ERROR_COUNT = 'WEB_CONTENT_ERROR_COUNT'
    WEB_TOTAL_ERROR_COUNT = 'WEB_TOTAL_ERROR_COUNT'
    FTP_AVAILABILITY = 'FTP_AVAILABILITY'
    FTP_THROUGHPUT = 'FTP_THROUGHPUT'
    FTP_DNS = 'FTP_DNS'
    FTP_CONNECT = 'FTP_CONNECT'
    FTP_SSL = 'FTP_SSL'
    FTP_NEGOTIATION = 'FTP_NEGOTIATION'
    FTP_WAIT = 'FTP_WAIT'
    FTP_TTFB = 'FTP_TTFB'
    FTP_TRANSFER = 'FTP_TRANSFER'
    FTP_TOTAL = 'FTP_TOTAL'
    FTP_DNS_ERROR_COUNT = 'FTP_DNS_ERROR_COUNT'
    FTP_CONNECT_ERROR_COUNT = 'FTP_CONNECT_ERROR_COUNT'
    FTP_SSL_ERROR_COUNT = 'FTP_SSL_ERROR_COUNT'
    FTP_NEGOTIATION_ERROR_COUNT = 'FTP_NEGOTIATION_ERROR_COUNT'
    FTP_TRANSFER_ERROR_COUNT = 'FTP_TRANSFER_ERROR_COUNT'
    FTP_FTP_ERROR_COUNT = 'FTP_FTP_ERROR_COUNT'
    FTP_CONTENT_ERROR_COUNT = 'FTP_CONTENT_ERROR_COUNT'
    FTP_TOTAL_ERROR_COUNT = 'FTP_TOTAL_ERROR_COUNT'
    WEB_PAGE_LOAD_DOM_TIME = 'WEB_PAGE_LOAD_DOM_TIME'
    WEB_PAGE_LOAD = 'WEB_PAGE_LOAD'
    WEB_PAGE_TTFB = 'WEB_PAGE_TTFB'
    WEB_PAGE_COMPONENT_COUNT = 'WEB_PAGE_COMPONENT_COUNT'
    WEB_PAGE_ERROR_COUNT = 'WEB_PAGE_ERROR_COUNT'
    WEB_PAGE_LOAD_COMPLETION_RATE = 'WEB_PAGE_LOAD_COMPLETION_RATE'
    CLASSIC_TRANSACTION_TIME = 'CLASSIC_TRANSACTION_TIME'
    CLASSIC_TRANSACTION_COMPLETION = 'CLASSIC_TRANSACTION_COMPLETION'
    CLASSIC_TRANSACTION_STEP_TIME = 'CLASSIC_TRANSACTION_STEP_TIME'
    CLASSIC_TRANSACTION_PAGE_TIME = 'CLASSIC_TRANSACTION_PAGE_TIME'
    TRANSACTION_MARKER_TIME_DECOMPOSED = 'TRANSACTION_MARKER_TIME_DECOMPOSED'
    TRANSACTION_PAGE_LOAD_TIME_DECOMPOSED = 'TRANSACTION_PAGE_LOAD_TIME_DECOMPOSED'
    TRANSACTION_PAGE_TIME_DECOMPOSED = 'TRANSACTION_PAGE_TIME_DECOMPOSED'
    TRANSACTION_PAGE_LOAD_DOM_TIME_DECOMPOSED = 'TRANSACTION_PAGE_LOAD_DOM_TIME_DECOMPOSED'
    TRANSACTION_TIME = 'TRANSACTION_TIME'
    TRANSACTION_TIMEOUT = 'TRANSACTION_TIMEOUT'
    TRANSACTION_ASSERT_ERROR = 'TRANSACTION_ASSERT_ERROR'
    TRANSACTION_OTHER_ERROR = 'TRANSACTION_OTHER_ERROR'
    TRANSACTION_PAGE_ERROR = 'TRANSACTION_PAGE_ERROR'
    TRANSACTION_COMPLETION = 'TRANSACTION_COMPLETION'
    TRANSACTION_ERROR = 'TRANSACTION_ERROR'
    TRANSACTION_MARKER_TIME = 'TRANSACTION_MARKER_TIME'
    TRANSACTION_PAGE_TIME = 'TRANSACTION_PAGE_TIME'
    TRANSACTION_PAGE_LOAD_TIME = 'TRANSACTION_PAGE_LOAD_TIME'
    TRANSACTION_PAGE_LOAD_DOM_TIME = 'TRANSACTION_PAGE_LOAD_DOM_TIME'
    API_TRANSACTION_TIME = 'API_TRANSACTION_TIME'
    API_REQUEST_CALL_TIME = 'API_REQUEST_CALL_TIME'
    API_REQUEST_DNS_TIME = 'API_REQUEST_DNS_TIME'
    API_REQUEST_CONNECT_TIME = 'API_REQUEST_CONNECT_TIME'
    API_REQUEST_SSL_TIME = 'API_REQUEST_SSL_TIME'
    API_REQUEST_SEND_TIME = 'API_REQUEST_SEND_TIME'
    API_REQUEST_WAIT_TIME = 'API_REQUEST_WAIT_TIME'
    API_REQUEST_BLOCK_TIME = 'API_REQUEST_BLOCK_TIME'
    API_REQUEST_RECEIVE_TIME = 'API_REQUEST_RECEIVE_TIME'
    API_REQUEST_ASSERT_ERROR_COUNT = 'API_REQUEST_ASSERT_ERROR_COUNT'
    API_REQUEST_COMPLETION = 'API_REQUEST_COMPLETION'
    API_REQUEST_OTHER_ERROR_COUNT = 'API_REQUEST_OTHER_ERROR_COUNT'
    VOIP_DISCARDS = 'VOIP_DISCARDS'
    VOIP_LATENCY = 'VOIP_LATENCY'
    VOIP_LOSS = 'VOIP_LOSS'
    VOIP_MOS = 'VOIP_MOS'
    VOIP_PDV = 'VOIP_PDV'
    SIP_AVAILABILITY = 'SIP_AVAILABILITY'
    SIP_DNS = 'SIP_DNS'
    SIP_CONNECT = 'SIP_CONNECT'
    SIP_REDIRECT = 'SIP_REDIRECT'
    SIP_REGISTER = 'SIP_REGISTER'
    SIP_OPTIONS = 'SIP_OPTIONS'
    SIP_INVITE = 'SIP_INVITE'
    SIP_WAIT = 'SIP_WAIT'
    SIP_RESPONSE_TIME = 'SIP_RESPONSE_TIME'
    SIP_TOTAL_TIME = 'SIP_TOTAL_TIME'
    SIP_DNS_ERROR_COUNT = 'SIP_DNS_ERROR_COUNT'
    SIP_CONNECT_ERROR_COUNT = 'SIP_CONNECT_ERROR_COUNT'
    SIP_REGISTER_ERROR_COUNT = 'SIP_REGISTER_ERROR_COUNT'
    SIP_OPTIONS_ERROR_COUNT = 'SIP_OPTIONS_ERROR_COUNT'
    SIP_INVITE_ERROR_COUNT = 'SIP_INVITE_ERROR_COUNT'
    SIP_TOTAL_ERROR_COUNT = 'SIP_TOTAL_ERROR_COUNT'
    DNS_SERVER_AVAILABILITY = 'DNS_SERVER_AVAILABILITY'
    DNS_SERVER_TIME = 'DNS_SERVER_TIME'
    DNS_TRACE_AVAILABILITY = 'DNS_TRACE_AVAILABILITY'
    DNS_TRACE_QUERY_COUNT = 'DNS_TRACE_QUERY_COUNT'
    DNS_TRACE_QUERY_TIME = 'DNS_TRACE_QUERY_TIME'
    DNSSEC_VALIDITY = 'DNSSEC_VALIDITY'
    DNSP_AVAILABILITY = 'DNSP_AVAILABILITY'
    DNSP_TIME = 'DNSP_TIME'
    DNSP_SERVER_TIME = 'DNSP_SERVER_TIME'
    BGP_REACHABILITY = 'BGP_REACHABILITY'
    BGP_PATH_CHANGES = 'BGP_PATH_CHANGES'
    ALERT_COUNT = 'ALERT_COUNT'
    ALERT_COUNT_AGENT = 'ALERT_COUNT_AGENT'
    ALERT_COUNT_BGP = 'ALERT_COUNT_BGP'
    ALERT_COUNT_DNSP = 'ALERT_COUNT_DNSP'
    ENDPOINT_SAMPLE_COUNT = 'ENDPOINT_SAMPLE_COUNT'
    ENDPOINT_NET_LOSS = 'ENDPOINT_NET_LOSS'
    ENDPOINT_NET_LATENCY = 'ENDPOINT_NET_LATENCY'
    ENDPOINT_NET_JITTER = 'ENDPOINT_NET_JITTER'
    ENDPOINT_NET_CONNECT_FAILURES = 'ENDPOINT_NET_CONNECT_FAILURES'
    ENDPOINT_NET_CPU_LOAD_PERCENT = 'ENDPOINT_NET_CPU_LOAD_PERCENT'
    ENDPOINT_NET_MEMORY_LOAD_PERCENT = 'ENDPOINT_NET_MEMORY_LOAD_PERCENT'
    ENDPOINT_NET_VPN_LOSS = 'ENDPOINT_NET_VPN_LOSS'
    ENDPOINT_NET_VPN_LATENCY = 'ENDPOINT_NET_VPN_LATENCY'
    ENDPOINT_PAGE_COUNT = 'ENDPOINT_PAGE_COUNT'
    ENDPOINT_WEB_COMPLETION = 'ENDPOINT_WEB_COMPLETION'
    ENDPOINT_WEB_RESPONSE_TIME = 'ENDPOINT_WEB_RESPONSE_TIME'
    ENDPOINT_WEB_PAGE_LOAD = 'ENDPOINT_WEB_PAGE_LOAD'
    ENDPOINT_WEB_PAGE_LOAD_DOM_TIME = 'ENDPOINT_WEB_PAGE_LOAD_DOM_TIME'
    ENDPOINT_WEB_EXPERIENCE_SCORE = 'ENDPOINT_WEB_EXPERIENCE_SCORE'
    ENDPOINT_WEB_BROWSER_ERROR_COUNT = 'ENDPOINT_WEB_BROWSER_ERROR_COUNT'
    ENDPOINT_GATEWAY_PROBE_COUNT = 'ENDPOINT_GATEWAY_PROBE_COUNT'
    ENDPOINT_GATEWAY_COMBINED_TRANSMISSION_RATE = 'ENDPOINT_GATEWAY_COMBINED_TRANSMISSION_RATE'
    ENDPOINT_GATEWAY_SIGNAL_QUALITY = 'ENDPOINT_GATEWAY_SIGNAL_QUALITY'
    ENDPOINT_GATEWAY_LOSS = 'ENDPOINT_GATEWAY_LOSS'
    ENDPOINT_GATEWAY_LATENCY = 'ENDPOINT_GATEWAY_LATENCY'
    ENDPOINT_GATEWAY_AGENT_SCORE = 'ENDPOINT_GATEWAY_AGENT_SCORE'
    ENDPOINT_GATEWAY_SCORE = 'ENDPOINT_GATEWAY_SCORE'
    ENDPOINT_GATEWAY_CONNECTION_SCORE = 'ENDPOINT_GATEWAY_CONNECTION_SCORE'
    ENDPOINT_GATEWAY_PROXY_LOSS = 'ENDPOINT_GATEWAY_PROXY_LOSS'
    ENDPOINT_GATEWAY_PROXY_LATENCY = 'ENDPOINT_GATEWAY_PROXY_LATENCY'
    ENDPOINT_GATEWAY_PROXY_SCORE = 'ENDPOINT_GATEWAY_PROXY_SCORE'
    ENDPOINT_GATEWAY_VPN_LOSS = 'ENDPOINT_GATEWAY_VPN_LOSS'
    ENDPOINT_GATEWAY_VPN_LATENCY = 'ENDPOINT_GATEWAY_VPN_LATENCY'
    ENDPOINT_GATEWAY_VPN_SCORE = 'ENDPOINT_GATEWAY_VPN_SCORE'
    ENDPOINT_GATEWAY_DNS_LOSS = 'ENDPOINT_GATEWAY_DNS_LOSS'
    ENDPOINT_GATEWAY_DNS_LATENCY = 'ENDPOINT_GATEWAY_DNS_LATENCY'
    ENDPOINT_GATEWAY_DNS_TIME = 'ENDPOINT_GATEWAY_DNS_TIME'
    ENDPOINT_GATEWAY_CPU_LOAD_PERCENT = 'ENDPOINT_GATEWAY_CPU_LOAD_PERCENT'
    ENDPOINT_GATEWAY_MEMORY_LOAD_PERCENT = 'ENDPOINT_GATEWAY_MEMORY_LOAD_PERCENT'
    EYEBROW_GATEWAY_WIRELESS_CHANNEL_SWAP_EVENTS = 'EYEBROW_GATEWAY_WIRELESS_CHANNEL_SWAP_EVENTS'
    EYEBROW_GATEWAY_WIRELESS_RETRANSMISSION_RATE = 'EYEBROW_GATEWAY_WIRELESS_RETRANSMISSION_RATE'
    EYEBROW_GATEWAY_WIRELESS_ROAMING_EVENTS = 'EYEBROW_GATEWAY_WIRELESS_ROAMING_EVENTS'
    EYEBROW_GATEWAY_WIRELESS_SIGNAL_QUALITY = 'EYEBROW_GATEWAY_WIRELESS_SIGNAL_QUALITY'
    EYEBROW_GATEWAY_WIRELESS_THROUGHPUT = 'EYEBROW_GATEWAY_WIRELESS_THROUGHPUT'
    ENDPOINT_AST_TEST_NET_LOSS = 'ENDPOINT_AST_TEST_NET_LOSS'
    ENDPOINT_AST_TEST_NET_JITTER = 'ENDPOINT_AST_TEST_NET_JITTER'
    ENDPOINT_AST_TEST_NET_LATENCY = 'ENDPOINT_AST_TEST_NET_LATENCY'
    ENDPOINT_AST_TEST_NET_CPU_LOAD_PERCENT = 'ENDPOINT_AST_TEST_NET_CPU_LOAD_PERCENT'
    ENDPOINT_AST_TEST_NET_MEMORY_LOAD_PERCENT = 'ENDPOINT_AST_TEST_NET_MEMORY_LOAD_PERCENT'
    ENDPOINT_AST_TEST_VPN_LOSS = 'ENDPOINT_AST_TEST_VPN_LOSS'
    ENDPOINT_AST_TEST_VPN_LATENCY = 'ENDPOINT_AST_TEST_VPN_LATENCY'
    ENDPOINT_AST_TEST_TCP_CONNECTION_ERROR_COUNT = 'ENDPOINT_AST_TEST_TCP_CONNECTION_ERROR_COUNT'
    ENDPOINT_AST_TEST_APPLICATION_SCORE = 'ENDPOINT_AST_TEST_APPLICATION_SCORE'
    ENDPOINT_GATEWAY_WIRELESS_CHANNEL_SWAP_EVENTS = 'ENDPOINT_GATEWAY_WIRELESS_CHANNEL_SWAP_EVENTS'
    ENDPOINT_GATEWAY_WIRELESS_RETRANSMISSION_RATE = 'ENDPOINT_GATEWAY_WIRELESS_RETRANSMISSION_RATE'
    ENDPOINT_GATEWAY_WIRELESS_ROAMING_EVENTS = 'ENDPOINT_GATEWAY_WIRELESS_ROAMING_EVENTS'
    ENDPOINT_GATEWAY_WIRELESS_SIGNAL_QUALITY = 'ENDPOINT_GATEWAY_WIRELESS_SIGNAL_QUALITY'
    ENDPOINT_GATEWAY_WIRELESS_THROUGHPUT = 'ENDPOINT_GATEWAY_WIRELESS_THROUGHPUT'
    ENDPOINT_TEST_NET_LOSS = 'ENDPOINT_TEST_NET_LOSS'
    ENDPOINT_TEST_NET_JITTER = 'ENDPOINT_TEST_NET_JITTER'
    ENDPOINT_TEST_NET_LATENCY = 'ENDPOINT_TEST_NET_LATENCY'
    ENDPOINT_TEST_NET_CPU_LOAD_PERCENT = 'ENDPOINT_TEST_NET_CPU_LOAD_PERCENT'
    ENDPOINT_TEST_NET_MEMORY_LOAD_PERCENT = 'ENDPOINT_TEST_NET_MEMORY_LOAD_PERCENT'
    ENDPOINT_TEST_VPN_LOSS = 'ENDPOINT_TEST_VPN_LOSS'
    ENDPOINT_TEST_VPN_LATENCY = 'ENDPOINT_TEST_VPN_LATENCY'
    ENDPOINT_TEST_TCP_CONNECTION_ERROR_COUNT = 'ENDPOINT_TEST_TCP_CONNECTION_ERROR_COUNT'
    ENDPOINT_TEST_APPLICATION_SCORE = 'ENDPOINT_TEST_APPLICATION_SCORE'
    ENDPOINT_TEST_HTTP_AVAILABILITY = 'ENDPOINT_TEST_HTTP_AVAILABILITY'
    ENDPOINT_TEST_HTTP_WAIT = 'ENDPOINT_TEST_HTTP_WAIT'
    ENDPOINT_TEST_HTTP_SSL = 'ENDPOINT_TEST_HTTP_SSL'
    ENDPOINT_TEST_HTTP_CONNECT = 'ENDPOINT_TEST_HTTP_CONNECT'
    ENDPOINT_TEST_HTTP_DNS_LOOKUP = 'ENDPOINT_TEST_HTTP_DNS_LOOKUP'
    ENDPOINT_TEST_HTTP_RESPONSE_TIME = 'ENDPOINT_TEST_HTTP_RESPONSE_TIME'
    ENDPOINT_TEST_HTTP_THROUGHPUT = 'ENDPOINT_TEST_HTTP_THROUGHPUT'
    ENDPOINT_TEST_HTTP_APPLICATION_SCORE = 'ENDPOINT_TEST_HTTP_APPLICATION_SCORE'
    DEVICE_AVAILABILITY = 'DEVICE_AVAILABILITY'
    DEVICE_THROUGHPUT_INPUT = 'DEVICE_THROUGHPUT_INPUT'
    DEVICE_THROUGHPUT_OUTPUT = 'DEVICE_THROUGHPUT_OUTPUT'
    DEVICE_DISCARDS_INPUT = 'DEVICE_DISCARDS_INPUT'
    DEVICE_DISCARDS_OUTPUT = 'DEVICE_DISCARDS_OUTPUT'
    DEVICE_ERRORS_INPUT = 'DEVICE_ERRORS_INPUT'
    DEVICE_ERRORS_OUTPUT = 'DEVICE_ERRORS_OUTPUT'
    DEVICE_DISCARDS_AND_ERRORS_INPUT = 'DEVICE_DISCARDS_AND_ERRORS_INPUT'
    DEVICE_DISCARDS_AND_ERRORS_OUTPUT = 'DEVICE_DISCARDS_AND_ERRORS_OUTPUT'
    DEVICE_INTERFACES_UP = 'DEVICE_INTERFACES_UP'
    DEVICE_INTERFACES_WITH_STATE_CHANGES = 'DEVICE_INTERFACES_WITH_STATE_CHANGES'
    NETWORK_OUTAGES_OUTAGES = 'NETWORK_OUTAGES_OUTAGES'
    NETWORK_OUTAGES_LOCATIONS = 'NETWORK_OUTAGES_LOCATIONS'
    NETWORK_OUTAGES_INTERFACES = 'NETWORK_OUTAGES_INTERFACES'
    NETWORK_OUTAGES_AFFECTED_TESTS = 'NETWORK_OUTAGES_AFFECTED_TESTS'
    APPLICATION_OUTAGES_AFFECTED_TESTS = 'APPLICATION_OUTAGES_AFFECTED_TESTS'
    APPLICATION_OUTAGES_SERVERS = 'APPLICATION_OUTAGES_SERVERS'
    APPLICATION_OUTAGES_LOCATIONS = 'APPLICATION_OUTAGES_LOCATIONS'
    APPLICATION_OUTAGES_OUTAGES = 'APPLICATION_OUTAGES_OUTAGES'
    APPDYNAMICS_SERVICE_HEALTH = 'APPDYNAMICS_SERVICE_HEALTH'
    CLOUD_NATIVE_MONITORING_MINUS_ACCEPTED_TOTAL_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-ACCEPTED_TOTAL_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_ACCEPTED_OUTBOUND_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-ACCEPTED_OUTBOUND_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_ACCEPTED_INBOUND_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-ACCEPTED_INBOUND_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_ACCEPTED_INTERNAL_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-ACCEPTED_INTERNAL_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_REJECTED_TOTAL_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-REJECTED_TOTAL_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_REJECTED_OUTBOUND_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-REJECTED_OUTBOUND_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_REJECTED_INBOUND_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-REJECTED_INBOUND_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_REJECTED_INTERNAL_THROUGHPUT = 'CLOUD_NATIVE_MONITORING-REJECTED_INTERNAL_THROUGHPUT'
    CLOUD_NATIVE_MONITORING_MINUS_TOTAL_CONNECTION_RATE = 'CLOUD_NATIVE_MONITORING-TOTAL_CONNECTION_RATE'
    CLOUD_NATIVE_MONITORING_MINUS_CONNECTION_RATE = 'CLOUD_NATIVE_MONITORING-CONNECTION_RATE'
    CLOUD_NATIVE_MONITORING_MINUS_INTERNAL_CONNECTION_RATE = 'CLOUD_NATIVE_MONITORING-INTERNAL_CONNECTION_RATE'
    CLOUD_NATIVE_MONITORING_MINUS_ALL_EVENTS = 'CLOUD_NATIVE_MONITORING-ALL_EVENTS'
    CLOUD_NATIVE_MONITORING_MINUS_CONFIGURATION_CHANGE_EVENTS = 'CLOUD_NATIVE_MONITORING-CONFIGURATION_CHANGE_EVENTS'
    CLOUD_NATIVE_MONITORING_MINUS_AUTOSCALING_EVENTS = 'CLOUD_NATIVE_MONITORING-AUTOSCALING_EVENTS'
    TRAFFIC_INSIGHTS_MONITORING_MINUS_TOTAL_THROUGHPUT = 'TRAFFIC_INSIGHTS_MONITORING-TOTAL_THROUGHPUT'
    TRAFFIC_INSIGHTS_MONITORING_MINUS_DOWNSTREAM_THROUGHPUT = 'TRAFFIC_INSIGHTS_MONITORING-DOWNSTREAM_THROUGHPUT'
    TRAFFIC_INSIGHTS_MONITORING_MINUS_UPSTREAM_THROUGHPUT = 'TRAFFIC_INSIGHTS_MONITORING-UPSTREAM_THROUGHPUT'
    TRAFFIC_INSIGHTS_MONITORING_MINUS_CONNECTION_RATE = 'TRAFFIC_INSIGHTS_MONITORING-CONNECTION_RATE'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DashboardMetric from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

