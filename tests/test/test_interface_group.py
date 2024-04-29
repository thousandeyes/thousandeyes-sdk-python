# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.interface_group import InterfaceGroup

class TestInterfaceGroup(unittest.TestCase):
    """InterfaceGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceGroup:
        """Test InterfaceGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceGroup`
        """
        model = InterfaceGroup()
        if include_optional:
            return InterfaceGroup(
                aid = '1234',
                group_id = '281474976710706',
                group_name = 'PathVis Interface Group',
                ip_addresses = ["1.1.1.1","8.8.8.8"],
                rdns_regexes = ["aggr403b-1.iad3.rackspace.net","aggr403c-1.iad3.rackspace.net"]
            )
        else:
            return InterfaceGroup(
        )
        """

    def testInterfaceGroup(self):
        """Test InterfaceGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()