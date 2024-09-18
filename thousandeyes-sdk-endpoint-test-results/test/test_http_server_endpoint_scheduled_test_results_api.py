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
from thousandeyes_sdk.endpoint_test_results.api.http_server_endpoint_scheduled_test_results_api import HTTPServerEndpointScheduledTestResultsApi


class TestHTTPServerEndpointScheduledTestResultsApi(unittest.TestCase):
    """HTTPServerEndpointScheduledTestResultsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HTTPServerEndpointScheduledTestResultsApi()

    def tearDown(self) -> None:
        pass

    def test_get_http_server_scheduled_test_results_models_validation(self) -> None:
        """Test case for get_http_server_scheduled_test_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "server" : "www.example.com",
                    "isSavedEvent" : false,
                    "sslVersion" : "Auto",
                    "useNtlm" : false,
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/network/filter"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/pathvis"
                      } ],
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
                    "httpTimeLimit" : 5000,
                    "type" : "http-server",
                    "protocol" : "icmp",
                    "httpVersion" : 2,
                    "followRedirects" : true,
                    "authType" : "none",
                    "testName" : "Test name",
                    "verifyCertificate" : true,
                    "networkMeasurements" : true,
                    "tcpProbeMode" : "auto",
                    "url" : "https://example.com:443",
                    "labels" : [ {
                      "labelId" : "961",
                      "name" : "Artem label",
                      "isBuiltin" : false
                    }, {
                      "labelId" : "961",
                      "name" : "Artem label",
                      "isBuiltin" : false
                    } ],
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "port" : 443,
                    "isEnabled" : true,
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "testId" : "281474976710706",
                    "aid" : "1234",
                    "agentSelectorConfig" : {
                      "agentSelectorType" : "all-agents",
                      "maxMachines" : 25
                    },
                    "hasPathTraceInSession" : true,
                    "httpTargetTime" : 100,
                    "username" : "username",
                    "sslVersionId" : "0"
                  },
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
                    },
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
                    "originalTargetProfile" : {
                      "protocol" : "tcp",
                      "remotePort" : 80,
                      "remoteIpAddress" : "120.98.134.7"
                    },
                    "headers" : {
                      "requestHeaders" : "GET / HTTP/1.1\\r\\nHost: www.thousandeyes.com\\r\\nUser-Agent: curl/7.58.0-DEV\\r\\nAccept: */*\\r\\nAccept-Encoding: deflate, gzip\\r\\nX-ThousandEyes-Agent: yes\\r\\n",
                      "responseHeaders" : "HTTP/1.1 200 OK\\r\\nContent-Type: text/html;charset=UTF-8\\r\\nContent-Length: 9993\\r\\nConnection: keep-alive\\r\\nDate: Mon, 04 May 2020 16:13:00 GMT\\r\\nServer: Apache\\r\\nContent-Language: en-US\\r\\nContent-Encoding: gzip\\r\\nX-Frame-Options: sameorigin\\r\\nCache-Control: max-age=600, must-revalidate\\r\\nStrict-Transport-Security: max-age=31536000\\r\\nX-Content-Type-Options: nosniff\\r\\nX-XSS-Protection: 1; mode=block\\r\\nVary: Accept-Encoding\\r\\nX-Cache: Hit from cloudfront\\r\\nVia: 1.1 7ba3caf71ae7a52dd411d1a543e80cd8.cloudfront.net (CloudFront)\\r\\nX-Amz-Cf-Pop: SFO5-C3\\r\\nX-Amz-Cf-Id: w4h42tkoJD-rEpkRDZUvnQBmy26GVGe6pUsuRr1Dphf7oajYbjXaOA==\\r\\nAge: 132\\r\\n"
                    },
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "redirectTime" : 10,
                    "numRedirects" : 0,
                    "vpnProfile" : {
                      "vpnClientNetworkRange" : [ "9.88.37.27", "9.88.37.27" ],
                      "vpnGatewayAddress" : "120.98.134.7",
                      "vpnType" : "cisco-anyconnect",
                      "vpnClientAddresses" : [ "184.81.113.85", "13.129.91.62" ]
                    },
                    "errorType" : "connect",
                    "responseTime" : 14,
                    "totalTime" : 15,
                    "responseCode" : 200,
                    "receiveTime" : 1,
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
                    "connectTime" : 2,
                    "dnsTime" : 0,
                    "serverIp" : "193.2.1.88",
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
                    "testId" : "584739201",
                    "sslTime" : 9,
                    "aid" : "1234",
                    "roundId" : 1384309800,
                    "waitTime" : 3,
                    "errorDetails" : "errorDetails",
                    "wireSize" : 9993
                  }, {
                    "originalTargetProfile" : {
                      "protocol" : "tcp",
                      "remotePort" : 80,
                      "remoteIpAddress" : "120.98.134.7"
                    },
                    "headers" : {
                      "requestHeaders" : "GET / HTTP/1.1\\r\\nHost: www.thousandeyes.com\\r\\nUser-Agent: curl/7.58.0-DEV\\r\\nAccept: */*\\r\\nAccept-Encoding: deflate, gzip\\r\\nX-ThousandEyes-Agent: yes\\r\\n",
                      "responseHeaders" : "HTTP/1.1 200 OK\\r\\nContent-Type: text/html;charset=UTF-8\\r\\nContent-Length: 9993\\r\\nConnection: keep-alive\\r\\nDate: Mon, 04 May 2020 16:13:00 GMT\\r\\nServer: Apache\\r\\nContent-Language: en-US\\r\\nContent-Encoding: gzip\\r\\nX-Frame-Options: sameorigin\\r\\nCache-Control: max-age=600, must-revalidate\\r\\nStrict-Transport-Security: max-age=31536000\\r\\nX-Content-Type-Options: nosniff\\r\\nX-XSS-Protection: 1; mode=block\\r\\nVary: Accept-Encoding\\r\\nX-Cache: Hit from cloudfront\\r\\nVia: 1.1 7ba3caf71ae7a52dd411d1a543e80cd8.cloudfront.net (CloudFront)\\r\\nX-Amz-Cf-Pop: SFO5-C3\\r\\nX-Amz-Cf-Id: w4h42tkoJD-rEpkRDZUvnQBmy26GVGe6pUsuRr1Dphf7oajYbjXaOA==\\r\\nAge: 132\\r\\n"
                    },
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "redirectTime" : 10,
                    "numRedirects" : 0,
                    "vpnProfile" : {
                      "vpnClientNetworkRange" : [ "9.88.37.27", "9.88.37.27" ],
                      "vpnGatewayAddress" : "120.98.134.7",
                      "vpnType" : "cisco-anyconnect",
                      "vpnClientAddresses" : [ "184.81.113.85", "13.129.91.62" ]
                    },
                    "errorType" : "connect",
                    "responseTime" : 14,
                    "totalTime" : 15,
                    "responseCode" : 200,
                    "receiveTime" : 1,
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
                    "connectTime" : 2,
                    "dnsTime" : 0,
                    "serverIp" : "193.2.1.88",
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
                    "testId" : "584739201",
                    "sslTime" : 9,
                    "aid" : "1234",
                    "roundId" : 1384309800,
                    "waitTime" : 3,
                    "errorDetails" : "errorDetails",
                    "wireSize" : 9993
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_test_results.models.HttpEndpointTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_multi_test_filtered_http_server_scheduled_test_results_models_validation(self) -> None:
        """Test case for get_multi_test_filtered_http_server_scheduled_test_results request and response models"""
        request_body_json = """
                {
                  "searchSort" : [ {
                    "sort" : "round-id",
                    "order" : "desc"
                  }, {
                    "sort" : "round-id",
                    "order" : "desc"
                  } ],
                  "searchFilters" : {
                    "agentId" : [ "52455b09-ff1b-4849-8194-99026cc890e0", "52455b09-ff1b-4849-8194-99026cc890e0" ],
                    "testId" : [ "5", "5" ]
                  },
                  "thresholdFilter" : {
                    "conditionalOperator" : "and",
                    "filters" : [ {
                      "name" : "response-time",
                      "value" : 10.0,
                      "operator" : "gte"
                    }, {
                      "name" : "response-time",
                      "value" : 10.0,
                      "operator" : "gte"
                    } ]
                  }
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_test_results.models.HttpEndpointTestsDataRoundsSearch.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "totalHits" : 12,
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
                    },
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
                    "originalTargetProfile" : {
                      "protocol" : "tcp",
                      "remotePort" : 80,
                      "remoteIpAddress" : "120.98.134.7"
                    },
                    "headers" : {
                      "requestHeaders" : "GET / HTTP/1.1\\r\\nHost: www.thousandeyes.com\\r\\nUser-Agent: curl/7.58.0-DEV\\r\\nAccept: */*\\r\\nAccept-Encoding: deflate, gzip\\r\\nX-ThousandEyes-Agent: yes\\r\\n",
                      "responseHeaders" : "HTTP/1.1 200 OK\\r\\nContent-Type: text/html;charset=UTF-8\\r\\nContent-Length: 9993\\r\\nConnection: keep-alive\\r\\nDate: Mon, 04 May 2020 16:13:00 GMT\\r\\nServer: Apache\\r\\nContent-Language: en-US\\r\\nContent-Encoding: gzip\\r\\nX-Frame-Options: sameorigin\\r\\nCache-Control: max-age=600, must-revalidate\\r\\nStrict-Transport-Security: max-age=31536000\\r\\nX-Content-Type-Options: nosniff\\r\\nX-XSS-Protection: 1; mode=block\\r\\nVary: Accept-Encoding\\r\\nX-Cache: Hit from cloudfront\\r\\nVia: 1.1 7ba3caf71ae7a52dd411d1a543e80cd8.cloudfront.net (CloudFront)\\r\\nX-Amz-Cf-Pop: SFO5-C3\\r\\nX-Amz-Cf-Id: w4h42tkoJD-rEpkRDZUvnQBmy26GVGe6pUsuRr1Dphf7oajYbjXaOA==\\r\\nAge: 132\\r\\n"
                    },
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "redirectTime" : 10,
                    "numRedirects" : 0,
                    "vpnProfile" : {
                      "vpnClientNetworkRange" : [ "9.88.37.27", "9.88.37.27" ],
                      "vpnGatewayAddress" : "120.98.134.7",
                      "vpnType" : "cisco-anyconnect",
                      "vpnClientAddresses" : [ "184.81.113.85", "13.129.91.62" ]
                    },
                    "errorType" : "connect",
                    "responseTime" : 14,
                    "totalTime" : 15,
                    "responseCode" : 200,
                    "receiveTime" : 1,
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
                    "connectTime" : 2,
                    "dnsTime" : 0,
                    "serverIp" : "193.2.1.88",
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
                    "testId" : "584739201",
                    "sslTime" : 9,
                    "aid" : "1234",
                    "roundId" : 1384309800,
                    "waitTime" : 3,
                    "errorDetails" : "errorDetails",
                    "wireSize" : 9993
                  }, {
                    "originalTargetProfile" : {
                      "protocol" : "tcp",
                      "remotePort" : 80,
                      "remoteIpAddress" : "120.98.134.7"
                    },
                    "headers" : {
                      "requestHeaders" : "GET / HTTP/1.1\\r\\nHost: www.thousandeyes.com\\r\\nUser-Agent: curl/7.58.0-DEV\\r\\nAccept: */*\\r\\nAccept-Encoding: deflate, gzip\\r\\nX-ThousandEyes-Agent: yes\\r\\n",
                      "responseHeaders" : "HTTP/1.1 200 OK\\r\\nContent-Type: text/html;charset=UTF-8\\r\\nContent-Length: 9993\\r\\nConnection: keep-alive\\r\\nDate: Mon, 04 May 2020 16:13:00 GMT\\r\\nServer: Apache\\r\\nContent-Language: en-US\\r\\nContent-Encoding: gzip\\r\\nX-Frame-Options: sameorigin\\r\\nCache-Control: max-age=600, must-revalidate\\r\\nStrict-Transport-Security: max-age=31536000\\r\\nX-Content-Type-Options: nosniff\\r\\nX-XSS-Protection: 1; mode=block\\r\\nVary: Accept-Encoding\\r\\nX-Cache: Hit from cloudfront\\r\\nVia: 1.1 7ba3caf71ae7a52dd411d1a543e80cd8.cloudfront.net (CloudFront)\\r\\nX-Amz-Cf-Pop: SFO5-C3\\r\\nX-Amz-Cf-Id: w4h42tkoJD-rEpkRDZUvnQBmy26GVGe6pUsuRr1Dphf7oajYbjXaOA==\\r\\nAge: 132\\r\\n"
                    },
                    "agentId" : "861b7557-cd57-4bbb-b648-00bddf88ef49",
                    "redirectTime" : 10,
                    "numRedirects" : 0,
                    "vpnProfile" : {
                      "vpnClientNetworkRange" : [ "9.88.37.27", "9.88.37.27" ],
                      "vpnGatewayAddress" : "120.98.134.7",
                      "vpnType" : "cisco-anyconnect",
                      "vpnClientAddresses" : [ "184.81.113.85", "13.129.91.62" ]
                    },
                    "errorType" : "connect",
                    "responseTime" : 14,
                    "totalTime" : 15,
                    "responseCode" : 200,
                    "receiveTime" : 1,
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
                    "connectTime" : 2,
                    "dnsTime" : 0,
                    "serverIp" : "193.2.1.88",
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
                    "testId" : "584739201",
                    "sslTime" : 9,
                    "aid" : "1234",
                    "roundId" : 1384309800,
                    "waitTime" : 3,
                    "errorDetails" : "errorDetails",
                    "wireSize" : 9993
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_test_results.models.HttpMultiEndpointTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
