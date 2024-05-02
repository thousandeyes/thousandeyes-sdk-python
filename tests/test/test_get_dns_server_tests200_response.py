# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.get_dns_server_tests200_response import GetDNSServerTests200Response

class TestGetDNSServerTests200Response(unittest.TestCase):
    """GetDNSServerTests200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDNSServerTests200Response:
        """Test GetDNSServerTests200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDNSServerTests200Response`
        """
        model = GetDNSServerTests200Response()
        if include_optional:
            return GetDNSServerTests200Response(
                tests = [
                    null
                    ],
                links = tests.models.self_links__links.SelfLinks__links(
                    self = tests.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return GetDNSServerTests200Response(
        )
        """

    def testGetDNSServerTests200Response(self):
        """Test GetDNSServerTests200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
