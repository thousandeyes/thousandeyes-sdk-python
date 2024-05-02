# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_tests.models.dynamic_test_request import DynamicTestRequest

class TestDynamicTestRequest(unittest.TestCase):
    """DynamicTestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DynamicTestRequest:
        """Test DynamicTestRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DynamicTestRequest`
        """
        model = DynamicTestRequest()
        if include_optional:
            return DynamicTestRequest(
                aid = '1234',
                links = endpoint_tests.models.dynamic_test_links.DynamicTestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"},{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"}], ),
                agent_selector_config = endpoint_tests.models.endpoint_agent_selector_config.EndpointAgentSelectorConfig(),
                application = 'webex',
                created_date = '2022-07-17T22:00:54Z',
                interval = 120,
                is_enabled = True,
                has_path_trace_in_session = True,
                has_ping = True,
                has_traceroute = True,
                modified_date = '2022-07-17T22:00:54Z',
                network_measurements = True,
                protocol = 'icmp',
                tcp_probe_mode = 'auto',
                test_id = '281474976710706',
                test_name = 'Test name',
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ],
                agent_selector_type = 'all-agents',
                agents = ["0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1","66eec0f1-72b4-4755-aa83-3aed61d17f3c"],
                endpoint_agent_labels = ["567","214"],
                max_machines = 250
            )
        else:
            return DynamicTestRequest(
        )
        """

    def testDynamicTestRequest(self):
        """Test DynamicTestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
