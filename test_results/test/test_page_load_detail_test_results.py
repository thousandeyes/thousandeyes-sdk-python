# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.page_load_detail_test_results import PageLoadDetailTestResults

class TestPageLoadDetailTestResults(unittest.TestCase):
    """PageLoadDetailTestResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageLoadDetailTestResults:
        """Test PageLoadDetailTestResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageLoadDetailTestResults`
        """
        model = PageLoadDetailTestResults()
        if include_optional:
            return PageLoadDetailTestResults(
                results = [
                    null
                    ],
                test = { }
            )
        else:
            return PageLoadDetailTestResults(
        )
        """

    def testPageLoadDetailTestResults(self):
        """Test PageLoadDetailTestResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
