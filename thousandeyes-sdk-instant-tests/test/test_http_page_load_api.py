# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.instant_tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.instant_tests.api.http_page_load_api import HTTPPageLoadApi


class TestHTTPPageLoadApi(unittest.TestCase):
    """HTTPPageLoadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HTTPPageLoadApi()

    def tearDown(self) -> None:
        pass

    def test_create_page_load_instant_test_models_validation(self) -> None:
        """Test case for create_page_load_instant_test request and response models"""
        request_body_json = """
                {
                  "clientCertificate" : "-----BEGIN PRIVATE KEY-----\\nMIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL\\n-----END PRIVATE KEY-----\\n-----BEGIN CERTIFICATE-----\\nMIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL\\n-----END CERTIFICATE-----\\n",
                  "mtuMeasurements" : false,
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
                  "dnsOverride" : "8.8.8.8",
                  "bandwidthMeasurements" : true,
                  "probeMode" : "auto",
                  "includeHeaders" : true,
                  "type" : "page-load",
                  "oAuth" : {
                    "configId" : "123321123",
                    "testUrl" : "https://api.thousandeyes.com/v7/status",
                    "requestMethod" : "get",
                    "postBody" : "client_id: ************",
                    "headers" : "Authorization: Basic ************",
                    "authType" : "none",
                    "username" : "user123",
                    "password" : "*******"
                  },
                  "password" : "password",
                  "protocol" : "tcp",
                  "followRedirects" : true,
                  "contentRegex" : "(regex)+",
                  "pageLoadingStrategy" : "normal",
                  "testName" : "ThousandEyes Test",
                  "allowMicAndCamera" : false,
                  "browserLanguage" : "en-US",
                  "verifyCertificate" : false,
                  "overrideAgentProxy" : false,
                  "liveShare" : false,
                  "agentInterfaces" : {
                    "agentId" : "2954",
                    "ipAddress" : "192.1.1.0"
                  },
                  "labels" : [ "9842", "1283" ],
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "emulatedDeviceId" : "2",
                  "sharedWithAccounts" : [ "1234", "12345" ],
                  "overrideProxyId" : "281474976710706",
                  "sslVersion" : "Auto",
                  "useNtlm" : false,
                  "downloadLimit" : 2048,
                  "description" : "ThousandEyes Test",
                  "httpTimeLimit" : 5,
                  "blockDomains" : "domain.com/",
                  "allowGeolocation" : false,
                  "allowUnsafeLegacyRenegotiation" : true,
                  "fixedPacketRate" : 50,
                  "httpVersion" : 2,
                  "collectProxyNetworkData" : false,
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "authType" : "none",
                  "customHeaders" : {
                    "root" : {
                      "header1" : "value1"
                    },
                    "domains" : {
                      "domain1.com" : {
                        "header2" : "value2"
                      }
                    },
                    "all" : {
                      "header3" : "value3"
                    }
                  },
                  "pageLoadTargetTime" : 10,
                  "numPathTraces" : 3,
                  "savedEvent" : true,
                  "userAgent" : "curl",
                  "pageLoadTimeLimit" : 10,
                  "networkMeasurements" : true,
                  "url" : "www.thousandeyes.com",
                  "agents" : [ {
                    "agentId" : "125",
                    "sourceIpAddress" : "1.1.1.1"
                  }, {
                    "agentId" : "125",
                    "sourceIpAddress" : "1.1.1.1"
                  } ],
                  "createdDate" : "2022-07-17T22:00:54Z",
                  "disableScreenshot" : false,
                  "createdBy" : "user@user.com",
                  "testId" : "281474976710706",
                  "desiredStatusCode" : "200",
                  "httpTargetTime" : 100,
                  "sslVersionId" : "0",
                  "username" : "username"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.instant_tests.models.PageLoadInstantTestRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "clientCertificate" : "-----BEGIN PRIVATE KEY-----\\nMIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL\\n-----END PRIVATE KEY-----\\n-----BEGIN CERTIFICATE-----\\nMIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL\\n-----END CERTIFICATE-----\\n",
                  "mtuMeasurements" : false,
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
                  "dnsOverride" : "8.8.8.8",
                  "bandwidthMeasurements" : true,
                  "probeMode" : "auto",
                  "includeHeaders" : true,
                  "type" : "page-load",
                  "oAuth" : {
                    "configId" : "123321123",
                    "testUrl" : "https://api.thousandeyes.com/v7/status",
                    "requestMethod" : "get",
                    "postBody" : "client_id: ************",
                    "headers" : "Authorization: Basic ************",
                    "authType" : "none",
                    "username" : "user123",
                    "password" : "*******"
                  },
                  "password" : "password",
                  "protocol" : "tcp",
                  "followRedirects" : true,
                  "contentRegex" : "(regex)+",
                  "pageLoadingStrategy" : "normal",
                  "testName" : "ThousandEyes Test",
                  "allowMicAndCamera" : false,
                  "browserLanguage" : "en-US",
                  "verifyCertificate" : false,
                  "overrideAgentProxy" : false,
                  "liveShare" : false,
                  "agentInterfaces" : {
                    "agentId" : "2954",
                    "ipAddress" : "192.1.1.0"
                  },
                  "labels" : [ {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  }, {
                    "labelId" : "961",
                    "name" : "Artem label",
                    "isBuiltin" : false
                  } ],
                  "modifiedDate" : "2022-07-17T22:00:54Z",
                  "emulatedDeviceId" : "2",
                  "sharedWithAccounts" : [ {
                    "name" : "Account name",
                    "aid" : "1234"
                  }, {
                    "name" : "Account name",
                    "aid" : "1234"
                  } ],
                  "overrideProxyId" : "281474976710706",
                  "sslVersion" : "Auto",
                  "useNtlm" : false,
                  "downloadLimit" : 2048,
                  "description" : "ThousandEyes Test",
                  "httpTimeLimit" : 5,
                  "blockDomains" : "domain.com/",
                  "allowGeolocation" : false,
                  "allowUnsafeLegacyRenegotiation" : true,
                  "fixedPacketRate" : 50,
                  "httpVersion" : 2,
                  "collectProxyNetworkData" : false,
                  "pathTraceMode" : "classic",
                  "modifiedBy" : "user@user.com",
                  "authType" : "none",
                  "customHeaders" : {
                    "root" : {
                      "header1" : "value1"
                    },
                    "domains" : {
                      "domain1.com" : {
                        "header2" : "value2"
                      }
                    },
                    "all" : {
                      "header3" : "value3"
                    }
                  },
                  "pageLoadTargetTime" : 10,
                  "numPathTraces" : 3,
                  "savedEvent" : true,
                  "userAgent" : "curl",
                  "pageLoadTimeLimit" : 10,
                  "networkMeasurements" : true,
                  "url" : "www.thousandeyes.com",
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
                  "disableScreenshot" : false,
                  "createdBy" : "user@user.com",
                  "testId" : "281474976710706",
                  "desiredStatusCode" : "200",
                  "httpTargetTime" : 100,
                  "sslVersionId" : "0",
                  "username" : "username"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.instant_tests.models.PageLoadInstantTest.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
