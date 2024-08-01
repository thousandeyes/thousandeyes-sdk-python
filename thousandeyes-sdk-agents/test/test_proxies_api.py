# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.agents.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.agents.api.proxies_api import ProxiesApi


class TestProxiesApi(unittest.TestCase):
    """ProxiesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProxiesApi()

    def tearDown(self) -> None:
        pass

    def test_get_agents_proxies_models_validation(self) -> None:
        """Test case for get_agents_proxies request and response models"""

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
                  "agentProxies" : [ {
                    "password" : "**********",
                    "isLocalConfigured" : true,
                    "name" : "Test Proxy - Auth Type - BASIC",
                    "location" : "proxy.thousandeyes.com:3128",
                    "lastModified" : "2022-07-17T22:00:54Z",
                    "authType" : "basic",
                    "type" : "static",
                    "aid" : "1234",
                    "bypassList" : [ "10.0.0.0/16", "*.thousandeyes.com" ],
                    "user" : "user1",
                    "proxyId" : "281474976710706"
                  }, {
                    "password" : "**********",
                    "isLocalConfigured" : true,
                    "name" : "Test Proxy - Auth Type - BASIC",
                    "location" : "proxy.thousandeyes.com:3128",
                    "lastModified" : "2022-07-17T22:00:54Z",
                    "authType" : "basic",
                    "type" : "static",
                    "aid" : "1234",
                    "bypassList" : [ "10.0.0.0/16", "*.thousandeyes.com" ],
                    "user" : "user1",
                    "proxyId" : "281474976710706"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.agents.models.AgentProxies.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
