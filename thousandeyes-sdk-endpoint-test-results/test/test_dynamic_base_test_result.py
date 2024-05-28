# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_test_results.models.dynamic_base_test_result import DynamicBaseTestResult

class TestDynamicBaseTestResult(unittest.TestCase):
    """DynamicBaseTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DynamicBaseTestResult:
        """Test DynamicBaseTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DynamicBaseTestResult`
        """
        model = DynamicBaseTestResult()
        if include_optional:
            return DynamicBaseTestResult(
                application = 'webex',
                webex = thousandeyes_sdk.endpoint_test_results.models.dynamic_test_webex.DynamicTestWebex(
                    conference_id = '225817074608419375', 
                    correlation_id = '22581707460321454', 
                    local_sip_session_id = '22581707460321454', 
                    remote_sip_session_id = '22581707460321454', )
            )
        else:
            return DynamicBaseTestResult(
        )
        """

    def testDynamicBaseTestResult(self):
        """Test DynamicBaseTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()