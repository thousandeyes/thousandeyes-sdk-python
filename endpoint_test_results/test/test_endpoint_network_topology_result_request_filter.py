# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.endpoint_network_topology_result_request_filter import EndpointNetworkTopologyResultRequestFilter

class TestEndpointNetworkTopologyResultRequestFilter(unittest.TestCase):
    """EndpointNetworkTopologyResultRequestFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointNetworkTopologyResultRequestFilter:
        """Test EndpointNetworkTopologyResultRequestFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointNetworkTopologyResultRequestFilter`
        """
        model = EndpointNetworkTopologyResultRequestFilter()
        if include_optional:
            return EndpointNetworkTopologyResultRequestFilter(
                location = [San Francisco Bay Area, Germany],
                connection = [
                    'wireless'
                    ],
                platform = [
                    'mac'
                    ],
                gateway = [78.153.54.204, 78.153.54.206],
                proxy_target = [78.153.54.204, 78.153.54.206],
                vpn_target = [78.153.54.204, 78.153.54.206],
                agent_id = [3fde6422-f119-40e1-ae32-d08a1243c038, 236e6f18-9637-4a2f-b15f-7aa6a29c9fce],
                network_id = [660b34109d12, 660b34109d15],
                ssid = [wifi-name, other-room-wifi],
                bssid = [8c:68:c8:a5:0a:8c, 0c:51:01:e4:3e:d0],
                type = ["vpn","proxy"]
            )
        else:
            return EndpointNetworkTopologyResultRequestFilter(
        )
        """

    def testEndpointNetworkTopologyResultRequestFilter(self):
        """Test EndpointNetworkTopologyResultRequestFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
