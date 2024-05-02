# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instant_tests.models.ftp_server_properties import FtpServerProperties

class TestFtpServerProperties(unittest.TestCase):
    """FtpServerProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FtpServerProperties:
        """Test FtpServerProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FtpServerProperties`
        """
        model = FtpServerProperties()
        if include_optional:
            return FtpServerProperties(
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
                type = 'ftp-server'
            )
        else:
            return FtpServerProperties(
                password = 'password',
                request_type = 'download',
                url = 'www.thousandeyes.com',
                username = 'username',
        )
        """

    def testFtpServerProperties(self):
        """Test FtpServerProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
