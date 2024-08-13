# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.endpoint_tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.endpoint_tests.api.scheduled_tests_agent_to_server_api import ScheduledTestsAgentToServerApi


class TestScheduledTestsAgentToServerApi(unittest.TestCase):
    """ScheduledTestsAgentToServerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ScheduledTestsAgentToServerApi()

    def tearDown(self) -> None:
        pass

    def test_create_agent_to_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for create_agent_to_server_endpoint_scheduled_test request and response models"""
        request_body_json = """
                {
                  "protocol" : "icmp",
                  "hasPing" : true,
                  "port" : 80,
                  "agentSelectorType" : "all-agents",
                  "hasTraceroute" : true,
                  "maxMachines" : 10,
                  "serverName" : "www.example.com",
                  "interval" : 120,
                  "endpointAgentLabels" : [ "567", "214" ],
                  "agents" : [ "0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1", "66eec0f1-72b4-4755-aa83-3aed61d17f3c" ],
                  "testName" : "Test name"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointAgentToServerTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "server" : "www.example.com",
                  "isSavedEvent" : false,
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
                  "networkMeasurements" : true,
                  "type" : "agent-to-server",
                  "tcpProbeMode" : "auto",
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "protocol" : "icmp",
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "port" : 80,
                  "isEnabled" : true,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 120,
                  "testId" : "281474976710706",
                  "aid" : "1234",
                  "agentSelectorConfig" : {
                    "agentSelectorType" : "all-agents",
                    "maxMachines" : 10
                  },
                  "hasPathTraceInSession" : true,
                  "testName" : "Test name"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointAgentToServerTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_agent_to_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for delete_agent_to_server_endpoint_scheduled_test request and response models"""


    def test_get_agent_to_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for get_agent_to_server_endpoint_scheduled_test request and response models"""

        response_body_json = """
                {
                  "server" : "www.example.com",
                  "isSavedEvent" : false,
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
                  "networkMeasurements" : true,
                  "type" : "agent-to-server",
                  "tcpProbeMode" : "auto",
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "protocol" : "icmp",
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "port" : 80,
                  "isEnabled" : true,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 120,
                  "testId" : "281474976710706",
                  "aid" : "1234",
                  "agentSelectorConfig" : {
                    "agentSelectorType" : "all-agents",
                    "maxMachines" : 10
                  },
                  "hasPathTraceInSession" : true,
                  "testName" : "Test name"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointAgentToServerTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_agent_to_server_endpoint_scheduled_tests_models_validation(self) -> None:
        """Test case for get_agent_to_server_endpoint_scheduled_tests request and response models"""

        response_body_json = """
                {
                  "tests" : [ {
                    "server" : "www.example.com",
                    "isSavedEvent" : false,
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
                    "networkMeasurements" : true,
                    "type" : "agent-to-server",
                    "tcpProbeMode" : "auto",
                    "labels" : [ {
                      "labelId" : "961",
                      "name" : "Artem label",
                      "isBuiltin" : false
                    }, {
                      "labelId" : "961",
                      "name" : "Artem label",
                      "isBuiltin" : false
                    } ],
                    "protocol" : "icmp",
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "port" : 80,
                    "isEnabled" : true,
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "testId" : "281474976710706",
                    "aid" : "1234",
                    "agentSelectorConfig" : {
                      "agentSelectorType" : "all-agents",
                      "maxMachines" : 10
                    },
                    "hasPathTraceInSession" : true,
                    "testName" : "Test name"
                  }, {
                    "server" : "www.example.com",
                    "isSavedEvent" : false,
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
                    "networkMeasurements" : true,
                    "type" : "agent-to-server",
                    "tcpProbeMode" : "auto",
                    "labels" : [ {
                      "labelId" : "961",
                      "name" : "Artem label",
                      "isBuiltin" : false
                    }, {
                      "labelId" : "961",
                      "name" : "Artem label",
                      "isBuiltin" : false
                    } ],
                    "protocol" : "icmp",
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "port" : 80,
                    "isEnabled" : true,
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "testId" : "281474976710706",
                    "aid" : "1234",
                    "agentSelectorConfig" : {
                      "agentSelectorType" : "all-agents",
                      "maxMachines" : 10
                    },
                    "hasPathTraceInSession" : true,
                    "testName" : "Test name"
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
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointAgentToServerTests.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_agent_to_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for update_agent_to_server_endpoint_scheduled_test request and response models"""
        request_body_json = """
                {
                  "server" : "www.example.com",
                  "protocol" : "icmp",
                  "port" : 49153,
                  "isEnabled" : true,
                  "interval" : 120,
                  "tcpProbeMode" : "auto",
                  "testName" : "Test name"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointNetworkTestUpdate.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "server" : "www.example.com",
                  "isSavedEvent" : false,
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
                  "networkMeasurements" : true,
                  "type" : "agent-to-server",
                  "tcpProbeMode" : "auto",
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "protocol" : "icmp",
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "port" : 80,
                  "isEnabled" : true,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "interval" : 120,
                  "testId" : "281474976710706",
                  "aid" : "1234",
                  "agentSelectorConfig" : {
                    "agentSelectorType" : "all-agents",
                    "maxMachines" : 10
                  },
                  "hasPathTraceInSession" : true,
                  "testName" : "Test name"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointAgentToServerTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
