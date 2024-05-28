# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.instant_tests.models.page_load_instant_test import PageLoadInstantTest

class TestPageLoadInstantTest(unittest.TestCase):
    """PageLoadInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageLoadInstantTest:
        """Test PageLoadInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageLoadInstantTest`
        """
        model = PageLoadInstantTest()
        if include_optional:
            return PageLoadInstantTest(
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'page-load',
                links = thousandeyes_sdk.instant_tests.models.test_links.TestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ],
                shared_with_accounts = [
                    thousandeyes_sdk.instant_tests.models.shared_with_account.SharedWithAccount(
                        aid = '1234', 
                        name = 'Account name', )
                    ],
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
                custom_headers = {"root":{"header1":"value1"},"domains":{"domain1.com":{"header2":"value2"}},"all":{"header3":"value3"}},
                desired_status_code = '200',
                emulated_device_id = '2',
                follow_redirects = True,
                http_target_time = 100,
                http_time_limit = 5,
                http_version = 1,
                include_headers = True,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                page_load_target_time = 10,
                page_load_time_limit = 5,
                password = 'password',
                path_trace_mode = 'classic',
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
                block_domains = 'domain.com/',
                disable_screenshot = True,
                allow_mic_and_camera = True,
                allow_geolocation = True,
                browser_language = 'en-US',
                page_loading_strategy = 'normal',
                fixed_packet_rate = 50,
                agents = [
                    null
                    ]
            )
        else:
            return PageLoadInstantTest(
                url = 'www.thousandeyes.com',
        )
        """

    def testPageLoadInstantTest(self):
        """Test PageLoadInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()