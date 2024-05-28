# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.path_vis_base_test_result import PathVisBaseTestResult

class TestPathVisBaseTestResult(unittest.TestCase):
    """PathVisBaseTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PathVisBaseTestResult:
        """Test PathVisBaseTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PathVisBaseTestResult`
        """
        model = PathVisBaseTestResult()
        if include_optional:
            return PathVisBaseTestResult(
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800,
                links = None,
                start_time = 1384309800,
                end_time = 1384309800,
                agent = thousandeyes_sdk.test_results.models.agent.Agent(
                    agent_id = '281474976710706', 
                    agent_name = 'thousandeyes-stg-va-254', 
                    country_id = 'US', 
                    location = 'San Francisco Bay Area', ),
                server = 'www.google.com:443',
                server_ip = '172.217.170.68',
                source_ip = '196.40.106.237',
                source_prefix = '196.40.96.0/20',
                target_is_proxy = True,
                direction = 'to-target'
            )
        else:
            return PathVisBaseTestResult(
        )
        """

    def testPathVisBaseTestResult(self):
        """Test PathVisBaseTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()