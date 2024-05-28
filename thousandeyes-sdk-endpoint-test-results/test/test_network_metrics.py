# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_test_results.models.network_metrics import NetworkMetrics

class TestNetworkMetrics(unittest.TestCase):
    """NetworkMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkMetrics:
        """Test NetworkMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkMetrics`
        """
        model = NetworkMetrics()
        if include_optional:
            return NetworkMetrics(
                jitter = 46,
                latency = 150,
                loss = 0.1,
                target = '54.208.6.220'
            )
        else:
            return NetworkMetrics(
        )
        """

    def testNetworkMetrics(self):
        """Test NetworkMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()