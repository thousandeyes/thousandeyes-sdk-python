# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.rtp_stream_test_result import RtpStreamTestResult

class TestRtpStreamTestResult(unittest.TestCase):
    """RtpStreamTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RtpStreamTestResult:
        """Test RtpStreamTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RtpStreamTestResult`
        """
        model = RtpStreamTestResult()
        if include_optional:
            return RtpStreamTestResult(
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800,
                links = {appLink={href=https://app.thousandeyes.com/view/tests?__a=105&testId=195&roundId=1692916680&agentId=125}},
                start_time = 1384309800,
                end_time = 1384309800,
                agent = test_results.models.agent.Agent(
                    agent_id = '281474976710706', 
                    agent_name = 'thousandeyes-stg-va-254', 
                    country_id = 'US', 
                    location = 'San Francisco Bay Area', ),
                server_ip = '172.97.102.37',
                dscp = '46',
                dscp_name = 'EF (DSCP 46)',
                mos = 4.351024,
                codec_name = 'G.711 @ 64 Kbps',
                codec_max_mos = 4.41,
                loss = 0.0,
                discards = 0,
                latency = 103,
                pdv = 1,
                error_detail = 'Connection error'
            )
        else:
            return RtpStreamTestResult(
        )
        """

    def testRtpStreamTestResult(self):
        """Test RtpStreamTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
