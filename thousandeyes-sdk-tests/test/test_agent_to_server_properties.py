# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.tests.models.agent_to_server_properties import AgentToServerProperties

class TestAgentToServerProperties(unittest.TestCase):
    """AgentToServerProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentToServerProperties:
        """Test AgentToServerProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentToServerProperties`
        """
        model = AgentToServerProperties()
        if include_optional:
            return AgentToServerProperties(
                bandwidth_measurements = True,
                continuous_mode = False,
                fixed_packet_rate = 25,
                mtu_measurements = False,
                num_path_traces = 1,
                path_trace_mode = 'classic',
                port = 1,
                probe_mode = 'auto',
                protocol = 'tcp',
                server = 'www.thousandeyes.com',
                dscp = 'Best Effort (DSCP 0)',
                dscp_id = '0',
                ipv6_policy = 'use-agent-policy',
                ping_payload_size = 0,
                network_measurements = True,
                type = 'agent-to-server'
            )
        else:
            return AgentToServerProperties(
                server = 'www.thousandeyes.com',
        )
        """

    def testAgentToServerProperties(self):
        """Test AgentToServerProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
