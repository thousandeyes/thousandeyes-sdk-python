# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.api_test_result import ApiTestResult

class TestApiTestResult(unittest.TestCase):
    """ApiTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiTestResult:
        """Test ApiTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiTestResult`
        """
        model = ApiTestResult()
        if include_optional:
            return ApiTestResult(
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800,
                links = None,
                agent = thousandeyes_sdk.test_results.models.agent.Agent(
                    agent_id = '281474976710706', 
                    agent_name = 'thousandeyes-stg-va-254', 
                    country_id = 'US', 
                    location = 'San Francisco Bay Area', ),
                api_transaction_time = 990.1,
                completion = 100.0,
                error_type = 'None',
                error_details = 'Connection error'
            )
        else:
            return ApiTestResult(
        )
        """

    def testApiTestResult(self):
        """Test ApiTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
