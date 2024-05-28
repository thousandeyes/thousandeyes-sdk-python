# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_test_results.models.network_proxy_profile import NetworkProxyProfile

class TestNetworkProxyProfile(unittest.TestCase):
    """NetworkProxyProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkProxyProfile:
        """Test NetworkProxyProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkProxyProfile`
        """
        model = NetworkProxyProfile()
        if include_optional:
            return NetworkProxyProfile(
                method = 'System',
                proxies = [
                    thousandeyes_sdk.endpoint_test_results.models.network_proxy.NetworkProxy(
                        bypass = '*.local;169.254/16', 
                        proxy = '<direct>', )
                    ]
            )
        else:
            return NetworkProxyProfile(
        )
        """

    def testNetworkProxyProfile(self):
        """Test NetworkProxyProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()