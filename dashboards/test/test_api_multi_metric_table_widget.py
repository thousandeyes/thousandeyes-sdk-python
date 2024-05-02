# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.api_multi_metric_table_widget import ApiMultiMetricTableWidget

class TestApiMultiMetricTableWidget(unittest.TestCase):
    """ApiMultiMetricTableWidget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMultiMetricTableWidget:
        """Test ApiMultiMetricTableWidget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMultiMetricTableWidget`
        """
        model = ApiMultiMetricTableWidget()
        if include_optional:
            return ApiMultiMetricTableWidget(
                id = '1234',
                title = 'Widget Title',
                visual_mode = 'Full',
                embed_url = 'https://embed.thousandeyes.com/e/00aa:3039802d-5c76-42d2-9a93-c6e5f9d3122f',
                is_embedded = True,
                metric_group = 'BGP',
                direction = 'FROM_TARGET',
                metric = 'ENDPOINT_GATEWAY_CPU_LOAD_PERCENT',
                filters = {"TEST":[5187,5227],"ENDPOINT_MACHINE_ID":["fbd0050c-07f7-43f7-9631-14b32f096962"]},
                measure = dashboards.models.api_widget_measure.ApiWidgetMeasure(
                    type = 'MEAN', 
                    percentile_value = 95.0, ),
                fixed_timespan = dashboards.models.api_duration.ApiDuration(
                    value = 10, 
                    unit = 'Days', ),
                api_link = '',
                should_exclude_alert_suppression_windows = True,
                links = dashboards.models.self_links__links.SelfLinks__links(
                    self = dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), ),
                type = 'Multi Metric Table',
                compare_to_previous_value = True,
                row_group_by = 'ALL',
                sort_by = 'alphabetical',
                sort_direction = 'ascending',
                limit = 10,
                multi_metric_columns = [
                    dashboards.models.api_multi_metric_column.ApiMultiMetricColumn(
                        id = '', 
                        data_source = 'ENDPOINT_AGENTS', 
                        metric_group = 'BGP', 
                        direction = 'FROM_TARGET', 
                        metric = 'ENDPOINT_GATEWAY_CPU_LOAD_PERCENT', 
                        filters = {"TEST":[5187,5227],"ENDPOINT_MACHINE_ID":["fbd0050c-07f7-43f7-9631-14b32f096962"]}, 
                        measure = dashboards.models.api_widget_measure.ApiWidgetMeasure(
                            type = 'MEAN', 
                            percentile_value = 95.0, ), )
                    ],
                data_source = 'ENDPOINT_AGENTS'
            )
        else:
            return ApiMultiMetricTableWidget(
                type = 'Multi Metric Table',
        )
        """

    def testApiMultiMetricTableWidget(self):
        """Test ApiMultiMetricTableWidget"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
