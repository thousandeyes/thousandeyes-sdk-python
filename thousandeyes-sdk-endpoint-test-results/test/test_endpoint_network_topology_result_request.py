# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request import EndpointNetworkTopologyResultRequest

class TestEndpointNetworkTopologyResultRequest(unittest.TestCase):
    """EndpointNetworkTopologyResultRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointNetworkTopologyResultRequest:
        """Test EndpointNetworkTopologyResultRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointNetworkTopologyResultRequest`
        """
        model = EndpointNetworkTopologyResultRequest()
        if include_optional:
            return EndpointNetworkTopologyResultRequest(
                search_filters = None
            )
        else:
            return EndpointNetworkTopologyResultRequest(
        )
        """

    def testEndpointNetworkTopologyResultRequest(self):
        """Test EndpointNetworkTopologyResultRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()