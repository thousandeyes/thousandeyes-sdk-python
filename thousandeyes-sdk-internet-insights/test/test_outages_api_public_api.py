# coding: utf-8

"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows.  For more information about Internet Insights, see the [Internet Insights](https://docs.thousandeyes.com/product-documentation/internet-insights). 

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.internet_insights.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.internet_insights.api.outages_api_public_api import OutagesAPIPublicApi


class TestOutagesAPIPublicApi(unittest.TestCase):
    """OutagesAPIPublicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OutagesAPIPublicApi()

    def tearDown(self) -> None:
        pass

    def test_filter_outages_models_validation(self) -> None:
        """Test case for filter_outages request and response models"""
        request_body_json = """
                {
                  "startDate" : "2022-03-01T01:30:00Z",
                  "endDate" : "2022-03-01T23:30:15Z",
                  "outageScope" : "all",
                  "providerName" : [ "Telia", "Amazon" ],
                  "interfaceNetwork" : [ "Telianet", "Cloudflare" ],
                  "applicationName" : [ "slack", "facebook" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.internet_insights.models.ApiOutageFilter.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

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
                  "outages" : [ {
                    "affectedInterfacesCount" : 1,
                    "endDate" : "2022-03-01T23:31:11Z",
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
                    "affectedLocationsCount" : 1,
                    "endRoundId" : 1646177700,
                    "affectedTestsCount" : 1,
                    "type" : "app",
                    "providerType" : "SAAS",
                    "duration" : 214,
                    "startRoundId" : 1646177400,
                    "name" : "Google",
                    "id" : "xxxxxxxxxxxxxxxxxx1",
                    "affectedServersCount" : 2,
                    "asn" : 19994,
                    "providerName" : "Google",
                    "startDate" : "2022-03-01T23:31:11Z"
                  }, {
                    "affectedInterfacesCount" : 1,
                    "endDate" : "2022-03-01T23:31:11Z",
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
                    "affectedLocationsCount" : 1,
                    "endRoundId" : 1646177700,
                    "affectedTestsCount" : 1,
                    "type" : "app",
                    "providerType" : "SAAS",
                    "duration" : 214,
                    "startRoundId" : 1646177400,
                    "name" : "Google",
                    "id" : "xxxxxxxxxxxxxxxxxx1",
                    "affectedServersCount" : 2,
                    "asn" : 19994,
                    "providerName" : "Google",
                    "startDate" : "2022-03-01T23:31:11Z"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.internet_insights.models.ApiOutagesResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_app_outage_models_validation(self) -> None:
        """Test case for get_app_outage request and response models"""

        response_body_json = """
                {
                  "affectedDomains" : [ "amazon.com", "amazon.com" ],
                  "affectedTests" : [ {
                    "name" : "amazon-test2",
                    "id" : 5
                  }, {
                    "name" : "amazon-test2",
                    "id" : 5
                  } ],
                  "endDate" : "2023-01-27T20:53:51.256Z",
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
                  "endRoundId" : 1674852600,
                  "providerType" : "SAAS",
                  "duration" : 180,
                  "startRoundId" : 1674852600,
                  "affectedAgents" : [ {
                    "name" : "London, England",
                    "id" : 11
                  }, {
                    "name" : "London, England",
                    "id" : 11
                  } ],
                  "id" : "0CC4C4209887126DE42E92252FB43962CBB3193147F318EA",
                  "providerName" : "Amazon Web Services",
                  "applicationName" : "Amazon Web Services",
                  "startDate" : "2023-01-27T20:50:51.256Z",
                  "errors" : [ "HTTP_SERVER_TIMEOUT", "HTTP_SERVER_TIMEOUT" ],
                  "affectedLocations" : [ {
                    "location" : "Chicago, Illinois, US",
                    "affectedServers" : [ {
                      "prefix" : "123.176.185.0/23",
                      "domain" : "amazon.com"
                    }, {
                      "prefix" : "123.176.185.0/23",
                      "domain" : "amazon.com"
                    } ]
                  }, {
                    "location" : "Chicago, Illinois, US",
                    "affectedServers" : [ {
                      "prefix" : "123.176.185.0/23",
                      "domain" : "amazon.com"
                    }, {
                      "prefix" : "123.176.185.0/23",
                      "domain" : "amazon.com"
                    } ]
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.internet_insights.models.ApiApplicationOutageDetails.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_network_outage_models_validation(self) -> None:
        """Test case for get_network_outage request and response models"""

        response_body_json = """
                {
                  "affectedDomains" : [ "periodic-failure.com", "periodic-failure.com" ],
                  "affectedTests" : [ {
                    "name" : "amazon-test2",
                    "id" : 5
                  }, {
                    "name" : "amazon-test2",
                    "id" : 5
                  } ],
                  "endDate" : "2023-01-27T20:53:51.256Z",
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
                  "networkName" : "Rackspace Hosting",
                  "endRoundId" : 1674852600,
                  "providerType" : "IAAS",
                  "duration" : 180,
                  "startRoundId" : 1674852600,
                  "affectedAgents" : [ {
                    "name" : "London, England",
                    "id" : 11
                  }, {
                    "name" : "London, England",
                    "id" : 11
                  } ],
                  "id" : "8EF2760862C705783A2F8BCBAAABB44F28DBC670DBA3B610",
                  "asn" : 19994,
                  "providerName" : "Rackspace",
                  "startDate" : "2023-01-27T20:50:51.256Z",
                  "affectedLocations" : [ {
                    "affectedInterfaces" : [ "50.51.52.53", "50.51.52.53" ],
                    "location" : "Chicago, Illinois, US"
                  }, {
                    "affectedInterfaces" : [ "50.51.52.53", "50.51.52.53" ],
                    "location" : "Chicago, Illinois, US"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.internet_insights.models.ApiNetworkOutageDetails.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
