# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.dashboard_snapshot_id import DashboardSnapshotId

class TestDashboardSnapshotId(unittest.TestCase):
    """DashboardSnapshotId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardSnapshotId:
        """Test DashboardSnapshotId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardSnapshotId`
        """
        model = DashboardSnapshotId()
        if include_optional:
            return DashboardSnapshotId(
                snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c'
            )
        else:
            return DashboardSnapshotId(
        )
        """

    def testDashboardSnapshotId(self):
        """Test DashboardSnapshotId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()