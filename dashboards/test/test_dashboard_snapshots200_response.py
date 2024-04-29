# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.dashboard_snapshots200_response import DashboardSnapshots200Response

class TestDashboardSnapshots200Response(unittest.TestCase):
    """DashboardSnapshots200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardSnapshots200Response:
        """Test DashboardSnapshots200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardSnapshots200Response`
        """
        model = DashboardSnapshots200Response()
        if include_optional:
            return DashboardSnapshots200Response(
                pages = { },
                dashboard_snapshots = [
                    null
                    ],
                links = dashboards.models.pagination_links__links.PaginationLinks__links(
                    previous = dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    next = dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    self = , )
            )
        else:
            return DashboardSnapshots200Response(
        )
        """

    def testDashboardSnapshots200Response(self):
        """Test DashboardSnapshots200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()