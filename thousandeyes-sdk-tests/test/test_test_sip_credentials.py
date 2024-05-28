# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.tests.models.test_sip_credentials import TestSipCredentials

class TestTestSipCredentials(unittest.TestCase):
    """TestSipCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestSipCredentials:
        """Test TestSipCredentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestSipCredentials`
        """
        model = TestSipCredentials()
        if include_optional:
            return TestSipCredentials(
                auth_user = 'username',
                password = 'password',
                port = 1,
                protocol = 'tcp',
                sip_registrar = 'voice.thousandeyes.com',
                user = 'username'
            )
        else:
            return TestSipCredentials(
                port = 1,
        )
        """

    def testTestSipCredentials(self):
        """Test TestSipCredentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()