# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.api_test_table_graphlets_data import ApiTestTableGraphletsData

class TestApiTestTableGraphletsData(unittest.TestCase):
    """ApiTestTableGraphletsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiTestTableGraphletsData:
        """Test ApiTestTableGraphletsData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiTestTableGraphletsData`
        """
        model = ApiTestTableGraphletsData()
        if include_optional:
            return ApiTestTableGraphletsData(
                metric = 'Availability',
                test_id = '68257',
                points = [
                    dashboards.models.api_graphlet_point.ApiGraphletPoint(
                        x = 1580403900, 
                        y = 128.249, )
                    ]
            )
        else:
            return ApiTestTableGraphletsData(
        )
        """

    def testApiTestTableGraphletsData(self):
        """Test ApiTestTableGraphletsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()