# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.bgp_tests import BgpTests

class TestBgpTests(unittest.TestCase):
    """BgpTests unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BgpTests:
        """Test BgpTests
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BgpTests`
        """
        model = BgpTests()
        if include_optional:
            return BgpTests(
                tests = [
                    null
                    ]
            )
        else:
            return BgpTests(
        )
        """

    def testBgpTests(self):
        """Test BgpTests"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
