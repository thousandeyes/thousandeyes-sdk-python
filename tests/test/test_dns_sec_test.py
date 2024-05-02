# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.dns_sec_test import DnsSecTest

class TestDnsSecTest(unittest.TestCase):
    """DnsSecTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsSecTest:
        """Test DnsSecTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsSecTest`
        """
        model = DnsSecTest()
        if include_optional:
            return DnsSecTest(
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
                type = 'dnssec',
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
                domain = 'www.thousandeyes.com',
                dns_query_class = 'in',
                agents = [
                    null
                    ]
            )
        else:
            return DnsSecTest(
                interval = 120,
                domain = 'www.thousandeyes.com',
        )
        """

    def testDnsSecTest(self):
        """Test DnsSecTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
