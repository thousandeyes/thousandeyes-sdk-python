# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_http_server_instant_test import EndpointHttpServerInstantTest

class TestEndpointHttpServerInstantTest(unittest.TestCase):
    """EndpointHttpServerInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointHttpServerInstantTest:
        """Test EndpointHttpServerInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointHttpServerInstantTest`
        """
        model = EndpointHttpServerInstantTest()
        if include_optional:
            return EndpointHttpServerInstantTest(
                agent_selector_type = 'all-agents',
                agents = ["0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1","66eec0f1-72b4-4755-aa83-3aed61d17f3c"],
                has_ping = True,
                has_traceroute = True,
                endpoint_agent_labels = ["567","214"],
                max_machines = 10,
                port = 80,
                test_name = 'Test name',
                auth_type = 'none',
                has_path_trace_in_session = True,
                http_time_limit = 5000,
                protocol = 'icmp',
                url = 'www.example.com',
                username = 'username',
                ssl_version_id = '0',
                tcp_probe_mode = 'auto',
                verify_certificate = False,
                target_response_time = 1000,
                password = 'password'
            )
        else:
            return EndpointHttpServerInstantTest(
                agent_selector_type = 'all-agents',
                max_machines = 10,
                test_name = 'Test name',
                http_time_limit = 5000,
                url = 'www.example.com',
                ssl_version_id = '0',
                verify_certificate = False,
                target_response_time = 1000,
        )
        """

    def testEndpointHttpServerInstantTest(self):
        """Test EndpointHttpServerInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
