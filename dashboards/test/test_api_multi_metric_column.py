# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.api_multi_metric_column import ApiMultiMetricColumn

class TestApiMultiMetricColumn(unittest.TestCase):
    """ApiMultiMetricColumn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMultiMetricColumn:
        """Test ApiMultiMetricColumn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMultiMetricColumn`
        """
        model = ApiMultiMetricColumn()
        if include_optional:
            return ApiMultiMetricColumn(
                id = '',
                data_source = 'ENDPOINT_AGENTS',
                metric_group = 'BGP',
                direction = 'FROM_TARGET',
                metric = 'ENDPOINT_GATEWAY_CPU_LOAD_PERCENT',
                filters = {"TEST":[5187,5227],"ENDPOINT_MACHINE_ID":["fbd0050c-07f7-43f7-9631-14b32f096962"]},
                measure = MEAN
            )
        else:
            return ApiMultiMetricColumn(
        )
        """

    def testApiMultiMetricColumn(self):
        """Test ApiMultiMetricColumn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()