# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_test_results.models.vpn_traceroute import VpnTraceroute

class TestVpnTraceroute(unittest.TestCase):
    """VpnTraceroute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VpnTraceroute:
        """Test VpnTraceroute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VpnTraceroute`
        """
        model = VpnTraceroute()
        if include_optional:
            return VpnTraceroute(
                destination = '13.32.22.232',
                error = 'An operation timed out.',
                info_flags = ["TE_INFO_ICMP_BLOCKED_BY_FIREWALL"],
                internal_errors = ["TE_INFO_ICMP_BLOCKED_BY_FIREWALL"],
                hops = [
                    null
                    ]
            )
        else:
            return VpnTraceroute(
        )
        """

    def testVpnTraceroute(self):
        """Test VpnTraceroute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
