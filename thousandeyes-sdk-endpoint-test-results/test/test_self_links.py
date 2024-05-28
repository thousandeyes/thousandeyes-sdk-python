# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_test_results.models.self_links import SelfLinks

class TestSelfLinks(unittest.TestCase):
    """SelfLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelfLinks:
        """Test SelfLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelfLinks`
        """
        model = SelfLinks()
        if include_optional:
            return SelfLinks(
                var_self = thousandeyes_sdk.endpoint_test_results.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', )
            )
        else:
            return SelfLinks(
        )
        """

    def testSelfLinks(self):
        """Test SelfLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()