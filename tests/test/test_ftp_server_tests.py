# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.ftp_server_tests import FtpServerTests

class TestFtpServerTests(unittest.TestCase):
    """FtpServerTests unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FtpServerTests:
        """Test FtpServerTests
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FtpServerTests`
        """
        model = FtpServerTests()
        if include_optional:
            return FtpServerTests(
                tests = [
                    null
                    ]
            )
        else:
            return FtpServerTests(
        )
        """

    def testFtpServerTests(self):
        """Test FtpServerTests"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
