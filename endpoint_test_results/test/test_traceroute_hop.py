# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.traceroute_hop import TracerouteHop

class TestTracerouteHop(unittest.TestCase):
    """TracerouteHop unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TracerouteHop:
        """Test TracerouteHop
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TracerouteHop`
        """
        model = TracerouteHop()
        if include_optional:
            return TracerouteHop(
                hop = 1,
                ip_address = '196.40.106.237',
                prefix = '196.40.96.0/20',
                asn = 34779,
                delay = 5,
                mpls = ["L=301472,E=0,S=1,T=1"],
                name = '89-210-88-65.access.t-2.net'
            )
        else:
            return TracerouteHop(
        )
        """

    def testTracerouteHop(self):
        """Test TracerouteHop"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
