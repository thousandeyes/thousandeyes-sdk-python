# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.snapshots.models.snapshot_response import SnapshotResponse

class TestSnapshotResponse(unittest.TestCase):
    """SnapshotResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotResponse:
        """Test SnapshotResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotResponse`
        """
        model = SnapshotResponse()
        if include_optional:
            return SnapshotResponse(
                id = 'wdiac',
                start_round_id = 1538784000,
                end_round_id = 1538787600,
                round_id = 1538784000,
                share_date = '2023-06-06T00:00Z',
                source_test_id = '281474976710706',
                test_id = '281474976710801',
                uid = '281474976810911',
                display_name = 'Snapshot created through API',
                extra_params = 'params',
                test = None,
                links = None
            )
        else:
            return SnapshotResponse(
        )
        """

    def testSnapshotResponse(self):
        """Test SnapshotResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()