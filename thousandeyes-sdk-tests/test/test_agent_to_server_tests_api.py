# coding: utf-8

"""
    Tests API

    This API allows you to list, create, edit, and delete Network and Application Synthetics tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.tests.api.agent_to_server_tests_api import AgentToServerTestsApi


class TestAgentToServerTestsApi(unittest.TestCase):
    """AgentToServerTestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AgentToServerTestsApi()

    def tearDown(self) -> None:
        pass

    def test_create_agent_to_server_test_models_validation(self) -> None:
        """Test case for create_agent_to_server_test request and response models"""
        request_body_json = """
                {
                  "server" : "www.thousandeyes.com:80",
                  "mtuMeasurements" : false,
                  "ipv6Policy" : "use-agent-policy",
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                  "alertRules" : [ "344753", "212697" ],
                  "bandwidthMeasurements" : true,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "agent-to-server",
                  "usePublicBgp" : true,
                  "enabled" : true,
                  "dscpId" : "0",
                  "fixedPacketRate" : 25,
                  "protocol" : "tcp",
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "alertsEnabled" : true,
                  "testName" : "ThousandEyes Test",
                  "numPathTraces" : 3,
                  "bgpMeasurements" : true,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "networkMeasurements" : false,
                  "labels" : [ "9842", "1283" ],
                  "agents" : [ {
                    "agentId" : "125",
                    "sourceIpAddress" : "1.1.1.1"
                  }, {
                    "agentId" : "125",
                    "sourceIpAddress" : "1.1.1.1"
                  } ],
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "createdBy" : "user@user.com",
                  "randomizedStartTime" : false,
                  "port" : 443,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 60,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ "1234", "12345" ],
                  "pingPayloadSize" : 112,
                  "continuousMode" : false,
                  "monitors" : [ "17410", "5" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tests.models.AgentToServerTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "server" : "www.thousandeyes.com:80",
                  "mtuMeasurements" : false,
                  "ipv6Policy" : "use-agent-policy",
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                  "alertRules" : [ {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  }, {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  } ],
                  "bandwidthMeasurements" : true,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "agent-to-server",
                  "usePublicBgp" : true,
                  "enabled" : true,
                  "dscpId" : "0",
                  "fixedPacketRate" : 25,
                  "protocol" : "tcp",
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "alertsEnabled" : true,
                  "testName" : "ThousandEyes Test",
                  "numPathTraces" : 3,
                  "bgpMeasurements" : true,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "networkMeasurements" : false,
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "agents" : [ {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  }, {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  } ],
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "createdBy" : "user@user.com",
                  "randomizedStartTime" : false,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 60,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ {
                    "name" : "Account name",
                    "aid" : "1234"
                  }, {
                    "name" : "Account name",
                    "aid" : "1234"
                  } ],
                  "pingPayloadSize" : 112,
                  "continuousMode" : false,
                  "monitors" : [ {
                    "monitorType" : "public",
                    "monitorId" : "1234",
                    "monitorName" : "Seattle, WA",
                    "ipAddress" : "4.69.184.193",
                    "countryId" : "GB",
                    "network" : "Level 3 Communications, Inc. (AS 3356)"
                  }, {
                    "monitorType" : "public",
                    "monitorId" : "1234",
                    "monitorName" : "Seattle, WA",
                    "ipAddress" : "4.69.184.193",
                    "countryId" : "GB",
                    "network" : "Level 3 Communications, Inc. (AS 3356)"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.tests.models.AgentToServerTestResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_agent_to_server_test_models_validation(self) -> None:
        """Test case for delete_agent_to_server_test request and response models"""


    def test_get_agent_to_server_test_models_validation(self) -> None:
        """Test case for get_agent_to_server_test request and response models"""

        response_body_json = """
                {
                  "server" : "www.thousandeyes.com:80",
                  "mtuMeasurements" : false,
                  "ipv6Policy" : "use-agent-policy",
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                  "alertRules" : [ {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  }, {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  } ],
                  "bandwidthMeasurements" : true,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "agent-to-server",
                  "usePublicBgp" : true,
                  "enabled" : true,
                  "dscpId" : "0",
                  "fixedPacketRate" : 25,
                  "protocol" : "tcp",
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "alertsEnabled" : true,
                  "testName" : "ThousandEyes Test",
                  "numPathTraces" : 3,
                  "bgpMeasurements" : true,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "networkMeasurements" : false,
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "agents" : [ {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  }, {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  } ],
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "createdBy" : "user@user.com",
                  "randomizedStartTime" : false,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 60,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ {
                    "name" : "Account name",
                    "aid" : "1234"
                  }, {
                    "name" : "Account name",
                    "aid" : "1234"
                  } ],
                  "pingPayloadSize" : 112,
                  "continuousMode" : false,
                  "monitors" : [ {
                    "monitorType" : "public",
                    "monitorId" : "1234",
                    "monitorName" : "Seattle, WA",
                    "ipAddress" : "4.69.184.193",
                    "countryId" : "GB",
                    "network" : "Level 3 Communications, Inc. (AS 3356)"
                  }, {
                    "monitorType" : "public",
                    "monitorId" : "1234",
                    "monitorName" : "Seattle, WA",
                    "ipAddress" : "4.69.184.193",
                    "countryId" : "GB",
                    "network" : "Level 3 Communications, Inc. (AS 3356)"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.tests.models.AgentToServerTestResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_agent_to_server_tests_models_validation(self) -> None:
        """Test case for get_agent_to_server_tests request and response models"""

        response_body_json = """
                {
                  "tests" : [ {
                    "server" : "www.thousandeyes.com:80",
                    "mtuMeasurements" : false,
                    "ipv6Policy" : "use-agent-policy",
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                    "bandwidthMeasurements" : true,
                    "description" : "ThousandEyes Test",
                    "probeMode" : "auto",
                    "type" : "agent-to-server",
                    "usePublicBgp" : true,
                    "enabled" : true,
                    "dscpId" : "0",
                    "fixedPacketRate" : 25,
                    "protocol" : "tcp",
                    "dscp" : "Best Effort (DSCP 0)",
                    "pathTraceMode" : "classic",
                    "modifiedBy" : "user@user.com",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test",
                    "numPathTraces" : 3,
                    "bgpMeasurements" : true,
                    "liveShare" : false,
                    "savedEvent" : true,
                    "networkMeasurements" : false,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "randomizedStartTime" : false,
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "testId" : "281474976710706",
                    "pingPayloadSize" : 112,
                    "continuousMode" : false
                  }, {
                    "server" : "www.thousandeyes.com:80",
                    "mtuMeasurements" : false,
                    "ipv6Policy" : "use-agent-policy",
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                    "bandwidthMeasurements" : true,
                    "description" : "ThousandEyes Test",
                    "probeMode" : "auto",
                    "type" : "agent-to-server",
                    "usePublicBgp" : true,
                    "enabled" : true,
                    "dscpId" : "0",
                    "fixedPacketRate" : 25,
                    "protocol" : "tcp",
                    "dscp" : "Best Effort (DSCP 0)",
                    "pathTraceMode" : "classic",
                    "modifiedBy" : "user@user.com",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test",
                    "numPathTraces" : 3,
                    "bgpMeasurements" : true,
                    "liveShare" : false,
                    "savedEvent" : true,
                    "networkMeasurements" : false,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "randomizedStartTime" : false,
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "testId" : "281474976710706",
                    "pingPayloadSize" : 112,
                    "continuousMode" : false
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
        response_from_json = thousandeyes_sdk.tests.models.AgentToServerTests.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_agent_to_server_test_models_validation(self) -> None:
        """Test case for update_agent_to_server_test request and response models"""
        request_body_json = """
                {
                  "server" : "www.thousandeyes.com:80",
                  "mtuMeasurements" : false,
                  "ipv6Policy" : "use-agent-policy",
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                  "alertRules" : [ "344753", "212697" ],
                  "bandwidthMeasurements" : true,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "agent-to-server",
                  "usePublicBgp" : true,
                  "enabled" : true,
                  "dscpId" : "0",
                  "fixedPacketRate" : 25,
                  "protocol" : "tcp",
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "alertsEnabled" : true,
                  "testName" : "ThousandEyes Test",
                  "numPathTraces" : 3,
                  "bgpMeasurements" : true,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "networkMeasurements" : false,
                  "labels" : [ "9842", "1283" ],
                  "agents" : [ {
                    "agentId" : "125",
                    "sourceIpAddress" : "1.1.1.1"
                  }, {
                    "agentId" : "125",
                    "sourceIpAddress" : "1.1.1.1"
                  } ],
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "createdBy" : "user@user.com",
                  "randomizedStartTime" : false,
                  "port" : 443,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 60,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ "1234", "12345" ],
                  "pingPayloadSize" : 112,
                  "continuousMode" : false,
                  "monitors" : [ "17410", "5" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tests.models.AgentToServerTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "server" : "www.thousandeyes.com:80",
                  "mtuMeasurements" : false,
                  "ipv6Policy" : "use-agent-policy",
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
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
                  "alertRules" : [ {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  }, {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  } ],
                  "bandwidthMeasurements" : true,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "agent-to-server",
                  "usePublicBgp" : true,
                  "enabled" : true,
                  "dscpId" : "0",
                  "fixedPacketRate" : 25,
                  "protocol" : "tcp",
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "alertsEnabled" : true,
                  "testName" : "ThousandEyes Test",
                  "numPathTraces" : 3,
                  "bgpMeasurements" : true,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "networkMeasurements" : false,
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "agents" : [ {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  }, {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  } ],
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "createdBy" : "user@user.com",
                  "randomizedStartTime" : false,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 60,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ {
                    "name" : "Account name",
                    "aid" : "1234"
                  }, {
                    "name" : "Account name",
                    "aid" : "1234"
                  } ],
                  "pingPayloadSize" : 112,
                  "continuousMode" : false,
                  "monitors" : [ {
                    "monitorType" : "public",
                    "monitorId" : "1234",
                    "monitorName" : "Seattle, WA",
                    "ipAddress" : "4.69.184.193",
                    "countryId" : "GB",
                    "network" : "Level 3 Communications, Inc. (AS 3356)"
                  }, {
                    "monitorType" : "public",
                    "monitorId" : "1234",
                    "monitorName" : "Seattle, WA",
                    "ipAddress" : "4.69.184.193",
                    "countryId" : "GB",
                    "network" : "Level 3 Communications, Inc. (AS 3356)"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.tests.models.AgentToServerTestResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
