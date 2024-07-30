# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.endpoint_agents.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.endpoint_agents.api.administrative_endpoints_api import AdministrativeEndpointsApi


class TestAdministrativeEndpointsApi(unittest.TestCase):
    """AdministrativeEndpointsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdministrativeEndpointsApi()

    def tearDown(self) -> None:
        pass

    def test_get_endpoint_agents_connection_string_models_validation(self) -> None:
        """Test case for get_endpoint_agents_connection_string request and response models"""

        response_body_json = """
                {
                  "connectionString" : "D2xZSLlqo64Xe2EnYisklA==",
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
        response_from_json = thousandeyes_sdk.endpoint_agents.models.ConnectionString.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
