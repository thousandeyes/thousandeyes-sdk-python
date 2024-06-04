# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.test_results.api.network_bgp_test_metrics_api import NetworkBGPTestMetricsApi


class TestNetworkBGPTestMetricsApi(unittest.TestCase):
    """NetworkBGPTestMetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NetworkBGPTestMetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_test_bgp_results_models_validation(self) -> None:
        """Test case for get_test_bgp_results request and response models"""

        response_body_json = """
                {
                  "test" : {
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
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
                    "previous" : {
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
                    "date" : "2022-07-17T22:00:54Z",
                    "_links" : {
                      "appLink" : {
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
                    "prefix" : "99.128.0.0/11",
                    "monitor" : {
                      "monitorId" : "281474976710706",
                      "monitorName" : "Vancouver, Canada - Bell Canada (AS 6539)",
                      "countryId" : "US"
                    },
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "reachability" : 0.0,
                    "updates" : 0.0,
                    "pathChanges" : 0.0,
                    "roundId" : 1384309800,
                    "prefixId" : "215"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "_links" : {
                      "appLink" : {
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
                    "prefix" : "99.128.0.0/11",
                    "monitor" : {
                      "monitorId" : "281474976710706",
                      "monitorName" : "Vancouver, Canada - Bell Canada (AS 6539)",
                      "countryId" : "US"
                    },
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "reachability" : 0.0,
                    "updates" : 0.0,
                    "pathChanges" : 0.0,
                    "roundId" : 1384309800,
                    "prefixId" : "215"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.BgpTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_test_bgp_routes_prefix_round_results_models_validation(self) -> None:
        """Test case for get_test_bgp_routes_prefix_round_results request and response models"""

        response_body_json = """
                {
                  "test" : {
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
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
                    "_links" : {
                      "appLink" : {
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
                    "prefix" : "99.128.0.0/11",
                    "monitor" : {
                      "monitorId" : "281474976710706",
                      "monitorName" : "Vancouver, Canada - Bell Canada (AS 6539)",
                      "countryId" : "US"
                    },
                    "hops" : [ {
                      "asName" : "Telus Advanced Communications",
                      "asn" : 852
                    }, {
                      "asName" : "Telus Advanced Communications",
                      "asn" : 852
                    } ],
                    "isActive" : true,
                    "roundId" : 1384309800,
                    "prefixId" : "215"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "_links" : {
                      "appLink" : {
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
                    "prefix" : "99.128.0.0/11",
                    "monitor" : {
                      "monitorId" : "281474976710706",
                      "monitorName" : "Vancouver, Canada - Bell Canada (AS 6539)",
                      "countryId" : "US"
                    },
                    "hops" : [ {
                      "asName" : "Telus Advanced Communications",
                      "asn" : 852
                    }, {
                      "asName" : "Telus Advanced Communications",
                      "asn" : 852
                    } ],
                    "isActive" : true,
                    "roundId" : 1384309800,
                    "prefixId" : "215"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.BgpTestRouteInformationResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
