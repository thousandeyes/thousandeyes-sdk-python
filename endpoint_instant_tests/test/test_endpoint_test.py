# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_instant_tests.models.endpoint_test import EndpointTest

class TestEndpointTest(unittest.TestCase):
    """EndpointTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointTest:
        """Test EndpointTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointTest`
        """
        model = EndpointTest()
        if include_optional:
            return EndpointTest(
                aid = '1234',
                links = endpoint_instant_tests.models.endpoint_test_links.EndpointTestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/network/filter"},{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/pathvis"}], ),
                agent_selector_config = endpoint_instant_tests.models.endpoint_agent_selector_config.EndpointAgentSelectorConfig(),
                created_date = '2022-07-17T22:00:54Z',
                interval = 120,
                is_enabled = True,
                is_saved_event = False,
                has_path_trace_in_session = True,
                modified_date = '2022-07-17T22:00:54Z',
                network_measurements = True,
                port = 80,
                protocol = 'icmp',
                server = 'www.example.com',
                test_id = '281474976710706',
                test_name = 'Test name',
                type = 'agent-to-server',
                tcp_probe_mode = 'auto',
                alert_rules = [
                    endpoint_instant_tests.models.alert_rule.AlertRule(
                        rule_id = '127094', 
                        rule_name = 'The End of the Internet', 
                        expression = '((hops((hopDelay >= 100 ms))))', 
                        direction = 'to-target', 
                        is_default = True, 
                        alert_type = 'http-server', 
                        minimum_sources = 10, 
                        minimum_sources_pct = 99, 
                        rounds_violating_mode = 'exact', 
                        rounds_violating_out_of = 5, 
                        rounds_violating_required = 2, 
                        severity = 'major', )
                    ]
            )
        else:
            return EndpointTest(
                type = 'agent-to-server',
        )
        """

    def testEndpointTest(self):
        """Test EndpointTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()