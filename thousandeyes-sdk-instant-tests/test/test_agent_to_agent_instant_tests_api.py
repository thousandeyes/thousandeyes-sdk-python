# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API operations lets you create and run new instant tests. You will need to be an Account Admin.  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.instant_tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.instant_tests.api.agent_to_agent_instant_tests_api import AgentToAgentInstantTestsApi


class TestAgentToAgentInstantTestsApi(unittest.TestCase):
    """AgentToAgentInstantTestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AgentToAgentInstantTestsApi()

    def tearDown(self) -> None:
        pass

    def test_create_agent_to_agent_instant_test_models_validation(self) -> None:
        """Test case for create_agent_to_agent_instant_test request and response models"""
        request_body_json = """
                {
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
                  "description" : "ThousandEyes Test",
                  "type" : "agent-to-agent",
                  "mss" : 100,
                  "dscpId" : "0",
                  "protocol" : "tcp",
                  "fixedPacketRate" : 50,
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "throughputRate" : 10,
                  "modifiedBy" : "user@user.com",
                  "testName" : "ThousandEyes Test",
                  "direction" : "to-target",
                  "throughputMeasurements" : false,
                  "numPathTraces" : 3,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "throughputDuration" : 10000,
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
                  "port" : 49153,
                  "randomizedStartTime" : false,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "targetAgentId" : "2954",
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ "1234", "12345" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.instant_tests.models.AgentToAgentInstantTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
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
                  "description" : "ThousandEyes Test",
                  "type" : "agent-to-agent",
                  "mss" : 100,
                  "dscpId" : "0",
                  "protocol" : "tcp",
                  "fixedPacketRate" : 50,
                  "dscp" : "Best Effort (DSCP 0)",
                  "pathTraceMode" : "classic",
                  "throughputRate" : 10,
                  "modifiedBy" : "user@user.com",
                  "testName" : "ThousandEyes Test",
                  "direction" : "to-target",
                  "throughputMeasurements" : false,
                  "numPathTraces" : 3,
                  "liveShare" : false,
                  "savedEvent" : true,
                  "throughputDuration" : 10000,
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
                  "port" : 49153,
                  "randomizedStartTime" : false,
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "targetAgentId" : "2954",
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ {
                    "name" : "Account name",
                    "aid" : "1234"
                  }, {
                    "name" : "Account name",
                    "aid" : "1234"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.instant_tests.models.AgentToAgentInstantTestResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
