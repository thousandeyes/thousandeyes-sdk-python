# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_tests.models.endpoint_test_links import EndpointTestLinks

class TestEndpointTestLinks(unittest.TestCase):
    """EndpointTestLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointTestLinks:
        """Test EndpointTestLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointTestLinks`
        """
        model = EndpointTestLinks()
        if include_optional:
            return EndpointTestLinks(
                var_self = None,
                test_results = [{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/network/filter"},{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/pathvis"}]
            )
        else:
            return EndpointTestLinks(
        )
        """

    def testEndpointTestLinks(self):
        """Test EndpointTestLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()