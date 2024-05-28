# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.dashboards.models.api_dashboard import ApiDashboard

class TestApiDashboard(unittest.TestCase):
    """ApiDashboard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDashboard:
        """Test ApiDashboard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDashboard`
        """
        model = ApiDashboard()
        if include_optional:
            return ApiDashboard(
                global_filter_id = '65babd9bb90bf55b17c96c8d',
                account_id = 1234,
                created_by = 1,
                modified_by = 1,
                modified_date = '2023-05-16 10:14:28',
                global_override = True,
                migrated_report = False,
                api_link = [
                    { }
                    ],
                dashboard_id = '5e1f7a99143ae6004fdc3bb4',
                title = 'HTTP Server Widgets',
                is_built_in = True,
                aid = '1234',
                dashboard_created_by = '1',
                dashboard_modified_by = '1',
                dashboard_modified_date = '2023-05-16T10:14:28Z',
                is_private = True,
                is_default_for_user = True,
                is_default_for_account = False,
                widgets = [
                    null
                    ],
                description = 'HTTP Server Widgets',
                default_timespan = None,
                is_global_override = True,
                is_migrated_report = False,
                links = thousandeyes_sdk.dashboards.models.dashboard_links.DashboardLinks(
                    self = thousandeyes_sdk.dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    snapshots = thousandeyes_sdk.dashboards.models.link.Link(
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
            return ApiDashboard(
        )
        """

    def testApiDashboard(self):
        """Test ApiDashboard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()