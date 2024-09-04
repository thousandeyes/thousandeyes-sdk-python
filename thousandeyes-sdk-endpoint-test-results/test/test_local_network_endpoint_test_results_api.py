# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.endpoint_test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.endpoint_test_results.api.local_network_endpoint_test_results_api import LocalNetworkEndpointTestResultsApi


class TestLocalNetworkEndpointTestResultsApi(unittest.TestCase):
    """LocalNetworkEndpointTestResultsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LocalNetworkEndpointTestResultsApi()

    def tearDown(self) -> None:
        pass

    def test_filter_local_networks_test_results_topologies_models_validation(self) -> None:
        """Test case for filter_local_networks_test_results_topologies request and response models"""
        request_body_json = """
                {
                  "searchFilters" : {
                    "agentId" : [ "3fde6422-f119-40e1-ae32-d08a1243c038", "236e6f18-9637-4a2f-b15f-7aa6a29c9fce" ],
                    "bssid" : [ "8c:68:c8:a5:0a:8c", "0c:51:01:e4:3e:d0" ],
                    "location" : [ "San Francisco Bay Area", "Germany" ],
                    "connection" : [ "wireless", "wireless" ],
                    "vpnTarget" : [ "78.153.54.204", "78.153.54.206" ],
                    "networkId" : [ "660b34109d12", "660b34109d15" ],
                    "type" : [ "vpn", "proxy" ],
                    "ssid" : [ "wifi-name", "other-room-wifi" ],
                    "platform" : [ "mac", "mac" ],
                    "gateway" : [ "78.153.54.204", "78.153.54.206" ],
                    "proxyTarget" : [ "78.153.54.204", "78.153.54.206" ]
                  }
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_test_results.models.EndpointNetworkTopologyResultRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "endDate" : "2022-07-18T22:00:54Z",
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "systemMetrics" : {
                      "cpuUtilization" : {
                        "min" : 0.22,
                        "median" : 0.61,
                        "max" : 0.75,
                        "mean" : 0.55,
                        "count" : 150,
                        "stdDev" : 0.01
                      },
                      "physicalMemoryTotalBytes" : 1024,
                      "startTimeMs" : 1581508857327,
                      "physicalMemoryUsedBytes" : {
                        "min" : 1.2,
                        "median" : 1.85,
                        "max" : 2.5,
                        "mean" : 1.77,
                        "count" : 155,
                        "stdDev" : 0.25
                      },
                      "endTimeMs" : 1581508867333
                    },
                    "isIcmpBlocked" : true,
                    "tcpConnect" : {
                      "rtt" : 77.777,
                      "errorCode" : "ERR_TIMED_OUT",
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    },
                    "icmpPing" : {
                      "maxRtt" : 66,
                      "pktsReceived" : 10,
                      "avgRtt" : 7,
                      "meanDevRtt" : 11,
                      "minRtt" : 1,
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "pktsSent" : 10
                    },
                    "type" : "vpn",
                    "networkTopologyId" : "00160:54c3a4b180c6:1490536500:c7a58c49",
                    "roundId" : 1384309800,
                    "targetPort" : 80,
                    "target" : "10.0.2.2"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "systemMetrics" : {
                      "cpuUtilization" : {
                        "min" : 0.22,
                        "median" : 0.61,
                        "max" : 0.75,
                        "mean" : 0.55,
                        "count" : 150,
                        "stdDev" : 0.01
                      },
                      "physicalMemoryTotalBytes" : 1024,
                      "startTimeMs" : 1581508857327,
                      "physicalMemoryUsedBytes" : {
                        "min" : 1.2,
                        "median" : 1.85,
                        "max" : 2.5,
                        "mean" : 1.77,
                        "count" : 155,
                        "stdDev" : 0.25
                      },
                      "endTimeMs" : 1581508867333
                    },
                    "isIcmpBlocked" : true,
                    "tcpConnect" : {
                      "rtt" : 77.777,
                      "errorCode" : "ERR_TIMED_OUT",
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    },
                    "icmpPing" : {
                      "maxRtt" : 66,
                      "pktsReceived" : 10,
                      "avgRtt" : 7,
                      "meanDevRtt" : 11,
                      "minRtt" : 1,
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "pktsSent" : 10
                    },
                    "type" : "vpn",
                    "networkTopologyId" : "00160:54c3a4b180c6:1490536500:c7a58c49",
                    "roundId" : 1384309800,
                    "targetPort" : 80,
                    "target" : "10.0.2.2"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_test_results.models.LocalNetworkTopologyResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_local_networks_test_results_models_validation(self) -> None:
        """Test case for get_local_networks_test_results request and response models"""

        response_body_json = """
                {
                  "localNetworks" : [ {
                    "publicIpRange" : "178.216.56.0-178.216.63.255",
                    "networkName" : "10.5.51.0 (in 178.216.56.0/21)",
                    "networkId" : "006c4fa7a054",
                    "localPrefix" : "10.5.51.0"
                  }, {
                    "publicIpRange" : "178.216.56.0-178.216.63.255",
                    "networkName" : "10.5.51.0 (in 178.216.56.0/21)",
                    "networkId" : "006c4fa7a054",
                    "localPrefix" : "10.5.51.0"
                  } ],
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_test_results.models.LocalNetworkResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_local_networks_test_results_topology_models_validation(self) -> None:
        """Test case for get_local_networks_test_results_topology request and response models"""

        response_body_json = """
                {
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "isIcmpBlocked" : true,
                    "tcpConnect" : {
                      "rtt" : 77.777,
                      "errorCode" : "ERR_TIMED_OUT",
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    },
                    "coordinates" : {
                      "latitude" : 46.0552778,
                      "location" : "Slovenia",
                      "longitude" : 14.5144444
                    },
                    "icmpTraceroutes" : [ {
                      "destination" : "13.32.22.232",
                      "hops" : [ {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      }, {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      } ],
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "internalErrors" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    }, {
                      "destination" : "13.32.22.232",
                      "hops" : [ {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      }, {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      } ],
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "internalErrors" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    } ],
                    "type" : "vpn",
                    "targetPort" : 80,
                    "target" : "10.0.2.2",
                    "systemMetrics" : {
                      "cpuUtilization" : {
                        "min" : 0.22,
                        "median" : 0.61,
                        "max" : 0.75,
                        "mean" : 0.55,
                        "count" : 150,
                        "stdDev" : 0.01
                      },
                      "physicalMemoryTotalBytes" : 1024,
                      "startTimeMs" : 1581508857327,
                      "physicalMemoryUsedBytes" : {
                        "min" : 1.2,
                        "median" : 1.85,
                        "max" : 2.5,
                        "mean" : 1.77,
                        "count" : 155,
                        "stdDev" : 0.25
                      },
                      "endTimeMs" : 1581508867333
                    },
                    "icmpTraceroute" : {
                      "destination" : "13.32.22.232",
                      "hops" : [ {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      }, {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      } ],
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "internalErrors" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    },
                    "networkProfile" : {
                      "previousInterface" : {
                        "publicIpAddress" : "84.255.241.1",
                        "publicIpRange" : "84.255.241.0-84.255.241.255",
                        "ipAddress" : "10.0.0.13",
                        "hardwareType" : "wireless",
                        "localPrefix" : "10.0.0.0",
                        "interfaceName" : "en0",
                        "subnetMask" : "255.255.255.0",
                        "dnsServers" : [ "8.8.8.8", "8.8.8.4" ]
                      },
                      "ethernetProfile" : {
                        "linkSpeed" : 860
                      },
                      "publicIpAddress" : "84.255.241.1",
                      "publicIpRange" : "84.255.241.0-84.255.241.255",
                      "ipAddress" : "10.0.0.13",
                      "hardwareType" : "wireless",
                      "localPrefix" : "10.0.0.0",
                      "proxyProfile" : {
                        "method" : "System",
                        "proxies" : [ {
                          "bypass" : "*.local;169.254/16",
                          "proxy" : "<direct>"
                        }, {
                          "bypass" : "*.local;169.254/16",
                          "proxy" : "<direct>"
                        } ]
                      },
                      "subnetMask" : "255.255.255.0",
                      "error" : "An operation timed out.",
                      "wirelessProfile" : {
                        "rssi" : -38,
                        "bssid" : "4c:ba:ba:f4:fa:fa",
                        "vendor" : "Cisco",
                        "txRate" : 130,
                        "channel" : 1,
                        "noise" : -95,
                        "phyMode" : "802.11n",
                        "ssid" : "Internet for the masses",
                        "quality" : 100
                      },
                      "interfaceName" : "en0",
                      "dnsServers" : [ "8.8.8.8", "8.8.8.4" ],
                      "gateway" : "10.0.0.1"
                    },
                    "icmpPing" : {
                      "maxRtt" : 66,
                      "pktsReceived" : 10,
                      "avgRtt" : 7,
                      "meanDevRtt" : 11,
                      "minRtt" : 1,
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "pktsSent" : 10
                    },
                    "networkTopologyId" : "00160:54c3a4b180c6:1490536500:c7a58c49",
                    "roundId" : 1384309800
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "isIcmpBlocked" : true,
                    "tcpConnect" : {
                      "rtt" : 77.777,
                      "errorCode" : "ERR_TIMED_OUT",
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    },
                    "coordinates" : {
                      "latitude" : 46.0552778,
                      "location" : "Slovenia",
                      "longitude" : 14.5144444
                    },
                    "icmpTraceroutes" : [ {
                      "destination" : "13.32.22.232",
                      "hops" : [ {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      }, {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      } ],
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "internalErrors" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    }, {
                      "destination" : "13.32.22.232",
                      "hops" : [ {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      }, {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      } ],
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "internalErrors" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    } ],
                    "type" : "vpn",
                    "targetPort" : 80,
                    "target" : "10.0.2.2",
                    "systemMetrics" : {
                      "cpuUtilization" : {
                        "min" : 0.22,
                        "median" : 0.61,
                        "max" : 0.75,
                        "mean" : 0.55,
                        "count" : 150,
                        "stdDev" : 0.01
                      },
                      "physicalMemoryTotalBytes" : 1024,
                      "startTimeMs" : 1581508857327,
                      "physicalMemoryUsedBytes" : {
                        "min" : 1.2,
                        "median" : 1.85,
                        "max" : 2.5,
                        "mean" : 1.77,
                        "count" : 155,
                        "stdDev" : 0.25
                      },
                      "endTimeMs" : 1581508867333
                    },
                    "icmpTraceroute" : {
                      "destination" : "13.32.22.232",
                      "hops" : [ {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      }, {
                        "delay" : 5,
                        "prefix" : "196.40.96.0/20",
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "name" : "89-210-88-65.access.t-2.net",
                        "mpls" : [ "L=301472,E=0,S=1,T=1" ],
                        "asn" : 34779
                      } ],
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "internalErrors" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ]
                    },
                    "networkProfile" : {
                      "previousInterface" : {
                        "publicIpAddress" : "84.255.241.1",
                        "publicIpRange" : "84.255.241.0-84.255.241.255",
                        "ipAddress" : "10.0.0.13",
                        "hardwareType" : "wireless",
                        "localPrefix" : "10.0.0.0",
                        "interfaceName" : "en0",
                        "subnetMask" : "255.255.255.0",
                        "dnsServers" : [ "8.8.8.8", "8.8.8.4" ]
                      },
                      "ethernetProfile" : {
                        "linkSpeed" : 860
                      },
                      "publicIpAddress" : "84.255.241.1",
                      "publicIpRange" : "84.255.241.0-84.255.241.255",
                      "ipAddress" : "10.0.0.13",
                      "hardwareType" : "wireless",
                      "localPrefix" : "10.0.0.0",
                      "proxyProfile" : {
                        "method" : "System",
                        "proxies" : [ {
                          "bypass" : "*.local;169.254/16",
                          "proxy" : "<direct>"
                        }, {
                          "bypass" : "*.local;169.254/16",
                          "proxy" : "<direct>"
                        } ]
                      },
                      "subnetMask" : "255.255.255.0",
                      "error" : "An operation timed out.",
                      "wirelessProfile" : {
                        "rssi" : -38,
                        "bssid" : "4c:ba:ba:f4:fa:fa",
                        "vendor" : "Cisco",
                        "txRate" : 130,
                        "channel" : 1,
                        "noise" : -95,
                        "phyMode" : "802.11n",
                        "ssid" : "Internet for the masses",
                        "quality" : 100
                      },
                      "interfaceName" : "en0",
                      "dnsServers" : [ "8.8.8.8", "8.8.8.4" ],
                      "gateway" : "10.0.0.1"
                    },
                    "icmpPing" : {
                      "maxRtt" : 66,
                      "pktsReceived" : 10,
                      "avgRtt" : 7,
                      "meanDevRtt" : 11,
                      "minRtt" : 1,
                      "error" : "An operation timed out.",
                      "infoFlags" : [ "TE_INFO_ICMP_BLOCKED_BY_FIREWALL" ],
                      "pktsSent" : 10
                    },
                    "networkTopologyId" : "00160:54c3a4b180c6:1490536500:c7a58c49",
                    "roundId" : 1384309800
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_test_results.models.LocalNetworkTopologyDetailResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
