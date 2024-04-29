# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_agents.models.pagination_next_and_self_link_links import PaginationNextAndSelfLinkLinks

class TestPaginationNextAndSelfLinkLinks(unittest.TestCase):
    """PaginationNextAndSelfLinkLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationNextAndSelfLinkLinks:
        """Test PaginationNextAndSelfLinkLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationNextAndSelfLinkLinks`
        """
        model = PaginationNextAndSelfLinkLinks()
        if include_optional:
            return PaginationNextAndSelfLinkLinks(
                next = endpoint_agents.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', ),
                var_self = endpoint_agents.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', )
            )
        else:
            return PaginationNextAndSelfLinkLinks(
        )
        """

    def testPaginationNextAndSelfLinkLinks(self):
        """Test PaginationNextAndSelfLinkLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()