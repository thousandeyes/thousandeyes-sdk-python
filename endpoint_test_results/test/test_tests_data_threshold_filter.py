# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.tests_data_threshold_filter import TestsDataThresholdFilter

class TestTestsDataThresholdFilter(unittest.TestCase):
    """TestsDataThresholdFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestsDataThresholdFilter:
        """Test TestsDataThresholdFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestsDataThresholdFilter`
        """
        model = TestsDataThresholdFilter()
        if include_optional:
            return TestsDataThresholdFilter(
                name = 'loss',
                value = 1.337,
                operator = 'gte'
            )
        else:
            return TestsDataThresholdFilter(
        )
        """

    def testTestsDataThresholdFilter(self):
        """Test TestsDataThresholdFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
