# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.tests.models.api_test import ApiTest

class TestApiTest(unittest.TestCase):
    """ApiTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiTest:
        """Test ApiTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiTest`
        """
        model = ApiTest()
        if include_optional:
            return ApiTest(
                interval = 120,
                alerts_enabled = True,
                enabled = True,
                alert_rules = [
                    thousandeyes_sdk.tests.models.alert_rule.AlertRule(
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
                    ],
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'api',
                links = thousandeyes_sdk.tests.models.test_links.TestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ],
                shared_with_accounts = [
                    thousandeyes_sdk.tests.models.shared_with_account.SharedWithAccount(
                        aid = '1234', 
                        name = 'Account name', )
                    ],
                follow_redirects = True,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                path_trace_mode = 'classic',
                predefined_variables = [
                    thousandeyes_sdk.tests.models.api_predefined_variable.ApiPredefinedVariable(
                        name = 'myUsername', 
                        value = 'ThousandEyesAccountUserName', )
                    ],
                probe_mode = 'auto',
                protocol = 'tcp',
                requests = [
                    thousandeyes_sdk.tests.models.api_request.ApiRequest(
                        assertions = [
                            thousandeyes_sdk.tests.models.api_request_assertion.ApiRequestAssertion(
                                name = 'status-code', 
                                operator = 'is', 
                                value = '200', )
                            ], 
                        auth_type = 'none', 
                        bearer_token = 'abcd-1234-...', 
                        body = '', 
                        collect_api_response = 'true', 
                        headers = [
                            thousandeyes_sdk.tests.models.api_request_header.ApiRequestHeader(
                                key = 'x-custom-header', 
                                value = 'keep-alive', )
                            ], 
                        method = 'get', 
                        name = 'Step 1', 
                        password = 'basic_pw123', 
                        url = 'https://api.thousandeyes.com/v7/status', 
                        username = 'ThousandEyesUserName', 
                        variables = [
                            thousandeyes_sdk.tests.models.api_request_variable.ApiRequestVariable(
                                value = 'tests[0].name', )
                            ], 
                        wait_time_ms = 0, )
                    ],
                ssl_version_id = '0',
                target_time = 1,
                time_limit = 5,
                url = 'www.thousandeyes.com',
                agents = [
                    null
                    ],
                credentials = ["3247","1051"],
                bgp_measurements = True,
                use_public_bgp = True,
                monitors = [
                    thousandeyes_sdk.tests.models.monitor.Monitor(
                        country_id = 'GB', 
                        monitor_id = '1234', 
                        ip_address = '4.69.184.193', 
                        network = 'Level 3 Communications, Inc. (AS 3356)', 
                        monitor_type = 'public', 
                        monitor_name = 'Seattle, WA', )
                    ]
            )
        else:
            return ApiTest(
                interval = 120,
                requests = [
                    thousandeyes_sdk.tests.models.api_request.ApiRequest(
                        assertions = [
                            thousandeyes_sdk.tests.models.api_request_assertion.ApiRequestAssertion(
                                name = 'status-code', 
                                operator = 'is', 
                                value = '200', )
                            ], 
                        auth_type = 'none', 
                        bearer_token = 'abcd-1234-...', 
                        body = '', 
                        collect_api_response = 'true', 
                        headers = [
                            thousandeyes_sdk.tests.models.api_request_header.ApiRequestHeader(
                                key = 'x-custom-header', 
                                value = 'keep-alive', )
                            ], 
                        method = 'get', 
                        name = 'Step 1', 
                        password = 'basic_pw123', 
                        url = 'https://api.thousandeyes.com/v7/status', 
                        username = 'ThousandEyesUserName', 
                        variables = [
                            thousandeyes_sdk.tests.models.api_request_variable.ApiRequestVariable(
                                value = 'tests[0].name', )
                            ], 
                        wait_time_ms = 0, )
                    ],
                url = 'www.thousandeyes.com',
        )
        """

    def testApiTest(self):
        """Test ApiTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()