# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.instant_tests.models.http_server_properties import HttpServerProperties

class TestHttpServerProperties(unittest.TestCase):
    """HttpServerProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpServerProperties:
        """Test HttpServerProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpServerProperties`
        """
        model = HttpServerProperties()
        if include_optional:
            return HttpServerProperties(
                auth_type = 'none',
                bandwidth_measurements = True,
                client_certificate = '-----BEGIN PRIVATE KEY-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
-----END CERTIFICATE-----
',
                content_regex = '(regex)+',
                headers = ["header1: value1","header2: value2"],
                custom_headers = {"root":{"header1":"value1"},"domains":{"domain1.com":{"header2":"value2"}},"all":{"header3":"value3"}},
                desired_status_code = '200',
                download_limit = 2048,
                dns_override = '8.8.8.8',
                http_target_time = 100,
                http_time_limit = 5,
                http_version = 1,
                include_headers = True,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                password = 'password',
                path_trace_mode = 'classic',
                post_body = '{ "example" : "value"}',
                probe_mode = 'auto',
                protocol = 'tcp',
                ssl_version = 'Auto',
                ssl_version_id = '0',
                url = 'www.thousandeyes.com',
                use_ntlm = False,
                user_agent = 'curl',
                username = 'username',
                verify_certificate = True,
                allow_unsafe_legacy_renegotiation = True,
                ipv6_policy = 'use-agent-policy',
                follow_redirects = True,
                fixed_packet_rate = 50,
                type = 'http-server'
            )
        else:
            return HttpServerProperties(
                url = 'www.thousandeyes.com',
        )
        """

    def testHttpServerProperties(self):
        """Test HttpServerProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
