# coding: utf-8

"""
    BGP Monitors API

     Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.  When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.  For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility). 

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.bgp_monitors.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.bgp_monitors.api.list_bgp_monitors_api import ListBGPMonitorsApi


class TestListBGPMonitorsApi(unittest.TestCase):
    """ListBGPMonitorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ListBGPMonitorsApi()

    def tearDown(self) -> None:
        pass

    def test_get_bgp_monitors_models_validation(self) -> None:
        """Test case for get_bgp_monitors request and response models"""

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
        response_from_json = thousandeyes_sdk.bgp_monitors.models.Monitors.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
