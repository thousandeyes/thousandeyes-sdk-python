# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.instant_tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.instant_tests.api.sip_server_api import SIPServerApi


class TestSIPServerApi(unittest.TestCase):
    """SIPServerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SIPServerApi()

    def tearDown(self) -> None:
        pass

    def test_create_sip_server_instant_test_models_validation(self) -> None:
        """Test case for create_sip_server_instant_test request and response models"""
        request_body_json = """
                {
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
                  "registerEnabled" : false,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "sip-server",
                  "fixedPacketRate" : 50,
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "targetSipCredentials" : {
                    "password" : "password",
                    "protocol" : "tcp",
                    "port" : 49153,
                    "sipRegistrar" : "voice.thousandeyes.com",
                    "authUser" : "username",
                    "user" : "username"
                  },
                  "testName" : "ThousandEyes Test",
                  "sipTargetTime" : 1000,
                  "numPathTraces" : 3,
                  "optionsRegex" : "[\\"a-z\\"]",
                  "liveShare" : false,
                  "savedEvent" : true,
                  "networkMeasurements" : true,
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
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "sipTimeLimit" : 5,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ "1234", "12345" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.instant_tests.models.SipServerInstantTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
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
                  "registerEnabled" : false,
                  "description" : "ThousandEyes Test",
                  "probeMode" : "auto",
                  "type" : "sip-server",
                  "authUser" : "username",
                  "fixedPacketRate" : 50,
                  "password" : "password",
                  "protocol" : "tcp",
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "testName" : "ThousandEyes Test",
                  "sipTargetTime" : 1000,
                  "numPathTraces" : 3,
                  "optionsRegex" : "[\\"a-z\\"]",
                  "liveShare" : false,
                  "savedEvent" : true,
                  "sipRegistrar" : "voice.thousandeyes.com",
                  "networkMeasurements" : true,
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
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "sipTimeLimit" : 5,
                  "testId" : "281474976710706",
                  "sharedWithAccounts" : [ {
                    "name" : "Account name",
                    "aid" : "1234"
                  }, {
                    "name" : "Account name",
                    "aid" : "1234"
                  } ],
                  "user" : "username"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.instant_tests.models.SipServerInstantTestResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
