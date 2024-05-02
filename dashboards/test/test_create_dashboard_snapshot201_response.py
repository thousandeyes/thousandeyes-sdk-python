# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.create_dashboard_snapshot201_response import CreateDashboardSnapshot201Response

class TestCreateDashboardSnapshot201Response(unittest.TestCase):
    """CreateDashboardSnapshot201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateDashboardSnapshot201Response:
        """Test CreateDashboardSnapshot201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDashboardSnapshot201Response`
        """
        model = CreateDashboardSnapshot201Response()
        if include_optional:
            return CreateDashboardSnapshot201Response(
                snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c',
                links = dashboards.models.self_links__links.SelfLinks__links(
                    self = dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return CreateDashboardSnapshot201Response(
        )
        """

    def testCreateDashboardSnapshot201Response(self):
        """Test CreateDashboardSnapshot201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
