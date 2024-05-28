# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.dashboards.models.dashboard_snapshot_response import DashboardSnapshotResponse

class TestDashboardSnapshotResponse(unittest.TestCase):
    """DashboardSnapshotResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardSnapshotResponse:
        """Test DashboardSnapshotResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardSnapshotResponse`
        """
        model = DashboardSnapshotResponse()
        if include_optional:
            return DashboardSnapshotResponse(
                snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c',
                links = thousandeyes_sdk.dashboards.models.self_links.SelfLinks(
                    self = thousandeyes_sdk.dashboards.models.link.Link(
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
            return DashboardSnapshotResponse(
        )
        """

    def testDashboardSnapshotResponse(self):
        """Test DashboardSnapshotResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()