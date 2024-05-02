# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.ftp_server_test import FtpServerTest

class TestFtpServerTest(unittest.TestCase):
    """FtpServerTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FtpServerTest:
        """Test FtpServerTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FtpServerTest`
        """
        model = FtpServerTest()
        if include_optional:
            return FtpServerTest(
                interval = 120,
                alerts_enabled = True,
                enabled = True,
                alert_rules = [
                    tests.models.alert_rule.AlertRule(
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
                type = 'ftp-server',
                links = tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ],
                shared_with_accounts = [
                    tests.models.shared_with_account.SharedWithAccount(
                        aid = '1234', 
                        name = 'Account name', )
                    ],
                bandwidth_measurements = True,
                download_limit = 1048576,
                ftp_target_time = 1000,
                ftp_time_limit = 10,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                password = 'password',
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                protocol = 'tcp',
                request_type = 'download',
                url = 'www.thousandeyes.com',
                use_active_ftp = True,
                use_explicit_ftps = False,
                username = 'username',
                fixed_packet_rate = 50,
                ipv6_policy = 'use-agent-policy',
                agents = [
                    null
                    ],
                bgp_measurements = True,
                use_public_bgp = True,
                monitors = [
                    tests.models.monitor.Monitor(
                        country_id = 'GB', 
                        monitor_id = '1234', 
                        ip_address = '4.69.184.193', 
                        network = 'Level 3 Communications, Inc. (AS 3356)', 
                        monitor_type = 'public', 
                        monitor_name = 'Seattle, WA', )
                    ]
            )
        else:
            return FtpServerTest(
                interval = 120,
                password = 'password',
                request_type = 'download',
                url = 'www.thousandeyes.com',
                username = 'username',
        )
        """

    def testFtpServerTest(self):
        """Test FtpServerTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
