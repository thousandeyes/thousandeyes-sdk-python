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
from thousandeyes_sdk.endpoint_tests.api.http_server_endpoint_scheduled_tests_api import HTTPServerEndpointScheduledTestsApi


class TestHTTPServerEndpointScheduledTestsApi(unittest.TestCase):
    """HTTPServerEndpointScheduledTestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HTTPServerEndpointScheduledTestsApi()

    def tearDown(self) -> None:
        pass

    def test_create_http_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for create_http_server_endpoint_scheduled_test request and response models"""
        request_body_json = """
                {
                  "verifyCertificate" : true,
                  "agentSelectorType" : "all-agents",
                  "maxMachines" : 25,
                  "httpTimeLimit" : 5000,
                  "networkMeasurements" : true,
                  "endpointAgentLabels" : [ "567", "214" ],
                  "tcpProbeMode" : "auto",
                  "url" : "url",
                  "agents" : [ "0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1", "66eec0f1-72b4-4755-aa83-3aed61d17f3c" ],
                  "protocol" : "icmp",
                  "password" : "password",
                  "port" : 443,
                  "targetResponseTime" : 1000,
                  "interval" : 60,
                  "authType" : "none",
                  "hasPathTraceInSession" : true,
                  "testName" : "Test name",
                  "username" : "username",
                  "sslVersionId" : "0"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointHttpServerTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
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
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointHttpServerTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_http_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for delete_http_server_endpoint_scheduled_test request and response models"""


    def test_get_http_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for get_http_server_endpoint_scheduled_test request and response models"""

        response_body_json = """
                {
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
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointHttpServerTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_http_server_endpoint_scheduled_tests_models_validation(self) -> None:
        """Test case for get_http_server_endpoint_scheduled_tests request and response models"""

        response_body_json = """
                {
                  "tests" : [ {
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
                  }, {
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
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointHttpServerTests.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_http_server_endpoint_scheduled_test_models_validation(self) -> None:
        """Test case for update_http_server_endpoint_scheduled_test request and response models"""
        request_body_json = """
                {
                  "protocol" : "icmp",
                  "isEnabled" : true,
                  "interval" : 60,
                  "tcpProbeMode" : "auto",
                  "url" : "www.thousandeyes.com",
                  "testName" : "Test name"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointHttpTestUpdate.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
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
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_tests.models.EndpointHttpServerTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
