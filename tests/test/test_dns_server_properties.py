# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.dns_server_properties import DnsServerProperties

class TestDnsServerProperties(unittest.TestCase):
    """DnsServerProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsServerProperties:
        """Test DnsServerProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsServerProperties`
        """
        model = DnsServerProperties()
        if include_optional:
            return DnsServerProperties(
                bandwidth_measurements = True,
                dns_servers = [
                    tests.models.test_dns_server.TestDnsServer(
                        server_id = '1447', 
                        server_name = 'dns-example.net', )
                    ],
                dns_transport_protocol = 'udp',
                domain = 'www.thousandeyes.com',
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                protocol = 'tcp',
                recursive_queries = True,
                ipv6_policy = 'use-agent-policy',
                fixed_packet_rate = 50,
                dns_query_class = 'in',
                type = 'dns-server'
            )
        else:
            return DnsServerProperties(
                dns_servers = [
                    tests.models.test_dns_server.TestDnsServer(
                        server_id = '1447', 
                        server_name = 'dns-example.net', )
                    ],
                domain = 'www.thousandeyes.com',
        )
        """

    def testDnsServerProperties(self):
        """Test DnsServerProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
