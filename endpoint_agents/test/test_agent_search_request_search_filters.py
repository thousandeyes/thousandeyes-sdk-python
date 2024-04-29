# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_agents.models.agent_search_request_search_filters import AgentSearchRequestSearchFilters

class TestAgentSearchRequestSearchFilters(unittest.TestCase):
    """AgentSearchRequestSearchFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentSearchRequestSearchFilters:
        """Test AgentSearchRequestSearchFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentSearchRequestSearchFilters`
        """
        model = AgentSearchRequestSearchFilters()
        if include_optional:
            return AgentSearchRequestSearchFilters(
                id = [
                    '5d0764ac-7e42-4ec8-a0d4-39fc53edccba'
                    ],
                agent_name = [
                    'myagent-1234'
                    ],
                computer_name = [
                    'DESKTOP-45AE8'
                    ],
                username = ["picard"],
                platform = [
                    'mac'
                    ],
                os_version = [
                    'Version 10.15.2'
                    ],
                location_country_iso = [
                    'FR'
                    ],
                location_subdivision1_code = [
                    'ENG'
                    ],
                location_city = [
                    'Paris'
                    ]
            )
        else:
            return AgentSearchRequestSearchFilters(
        )
        """

    def testAgentSearchRequestSearchFilters(self):
        """Test AgentSearchRequestSearchFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()