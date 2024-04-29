# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agents.models.enterprise_agent_data import EnterpriseAgentData

class TestEnterpriseAgentData(unittest.TestCase):
    """EnterpriseAgentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnterpriseAgentData:
        """Test EnterpriseAgentData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnterpriseAgentData`
        """
        model = EnterpriseAgentData()
        if include_optional:
            return EnterpriseAgentData(
                cluster_members = [
                    null
                    ],
                utilization = 25,
                account_groups = [
                    agents.models.account_group.AccountGroup()
                    ],
                ipv6_policy = 'force-ipv4',
                error_details = [
                    agents.models.error_detail.ErrorDetail(
                        code = 'agent-version-outdated', 
                        description = 'Agent Version 0.1.1 (latest: 1.0.0)', )
                    ],
                hostname = 'thousandeyes.com',
                last_seen = '2022-07-17T22:00:54Z',
                agent_state = 'online',
                keep_browser_cache = True,
                created_date = '2022-07-17T22:00:54Z',
                target_for_tests = '1.1.1.1',
                local_resolution_prefixes = [
                    '10.2.3.3/24'
                    ],
                interface_ip_mappings = [
                    agents.models.interface_ip_mapping.InterfaceIpMapping(
                        interface_name = 'wlp4s0', 
                        ip_addresses = ["73.252.207.219","2601:646:300:3ae0::b977"], )
                    ]
            )
        else:
            return EnterpriseAgentData(
        )
        """

    def testEnterpriseAgentData(self):
        """Test EnterpriseAgentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()