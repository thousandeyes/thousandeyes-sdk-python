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
from thousandeyes_sdk.endpoint_tests.api.agent_to_server_endpoint_dynamic_tests_api import AgentToServerEndpointDynamicTestsApi


class TestAgentToServerEndpointDynamicTestsApi(unittest.TestCase):
    """AgentToServerEndpointDynamicTestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AgentToServerEndpointDynamicTestsApi()

    def tearDown(self) -> None:
        pass

    def test_create_agent_to_server_endpoint_dynamic_test_models_validation(self) -> None:
        """Test case for create_agent_to_server_endpoint_dynamic_test request and response models"""
        request_body_json = """
                {
                  "protocol" : "icmp",
                  "application" : "webex",
                  "agentSelectorType" : "all-agents",
                  "maxMachines" : 25,
                  "interval" : 60,
                  "hasPathTraceInSession" : true,
                  "endpointAgentLabels" : [ "567", "214" ],
                  "tcpProbeMode" : "auto",
                  "agents" : [ "0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1", "66eec0f1-72b4-4755-aa83-3aed61d17f3c" ],
                  "testName" : "Test name"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_tests.models.DynamicTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "hasPing" : true,
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"
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
                  "networkMeasurements" : true,
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
                  "application" : "webex",
                  "hasTraceroute" : true,
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
                  "testName" : "Test name"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.DynamicTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_agent_to_server_endpoint_dynamic_test_models_validation(self) -> None:
        """Test case for delete_agent_to_server_endpoint_dynamic_test request and response models"""


    def test_get_agent_to_server_endpoint_dynamic_test_models_validation(self) -> None:
        """Test case for get_agent_to_server_endpoint_dynamic_test request and response models"""

        response_body_json = """
                {
                  "hasPing" : true,
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"
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
                  "networkMeasurements" : true,
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
                  "application" : "webex",
                  "hasTraceroute" : true,
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
                  "testName" : "Test name"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.DynamicTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_agent_to_server_endpoint_dynamic_tests_models_validation(self) -> None:
        """Test case for get_agent_to_server_endpoint_dynamic_tests request and response models"""

        response_body_json = """
                {
                  "tests" : [ {
                    "hasPing" : true,
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"
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
                    "networkMeasurements" : true,
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
                    "application" : "webex",
                    "hasTraceroute" : true,
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
                    "testName" : "Test name"
                  }, {
                    "hasPing" : true,
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"
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
                    "networkMeasurements" : true,
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
                    "application" : "webex",
                    "hasTraceroute" : true,
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
        response_from_json = thousandeyes_sdk.endpoint_tests.models.DynamicTests.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_agent_to_server_endpoint_dynamic_test_models_validation(self) -> None:
        """Test case for update_agent_to_server_endpoint_dynamic_test request and response models"""
        request_body_json = """
                {
                  "protocol" : "icmp",
                  "application" : "webex",
                  "isEnabled" : true,
                  "interval" : 60,
                  "tcpProbeMode" : "auto",
                  "testName" : "Test name"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointDynamicTestUpdate.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "hasPing" : true,
                  "_links" : {
                    "testResults" : [ {
                      "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"
                    }, {
                      "href" : "https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"
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
                  "networkMeasurements" : true,
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
                  "application" : "webex",
                  "hasTraceroute" : true,
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
                  "testName" : "Test name"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.DynamicTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
