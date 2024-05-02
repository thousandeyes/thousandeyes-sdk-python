# coding: utf-8

"""
    Credentials API

    Manage credentials for transaction tests using the Credentials API.  The following permissions are required to access Credentials API endpoints:  * `Settings Tests Read` for read operations. * `Settings Tests Update` for write operations. * `View sensitive data in web transaction scripts` to view the encrypted value property of credentials. * `Settings Tests Create Transaction (Tx) Tests` to create credentials.  For more information about credentials, see [Working With Secure Credentials](https://docs.thousandeyes.com/product-documentation/browser-synthetics/transaction-tests/getting-started/working-with-secure-credentials). 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from credentials.models.credentials import Credentials

class TestCredentials(unittest.TestCase):
    """Credentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Credentials:
        """Test Credentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Credentials`
        """
        model = Credentials()
        if include_optional:
            return Credentials(
                credentials = [
                    null
                    ]
            )
        else:
            return Credentials(
        )
        """

    def testCredentials(self):
        """Test Credentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
