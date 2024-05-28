# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.dashboards.models.api_alert_list_alert import ApiAlertListAlert

class TestApiAlertListAlert(unittest.TestCase):
    """ApiAlertListAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAlertListAlert:
        """Test ApiAlertListAlert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAlertListAlert`
        """
        model = ApiAlertListAlert()
        if include_optional:
            return ApiAlertListAlert(
                alert_id = '2004945',
                test_id = '56512',
                rule_id = '281724',
                alert_source = 'Http Test',
                alert_rule = 'Http Test Rule',
                alert_type = 'network-end-to-end-server',
                start_time = '2023-06-02T08:54Z',
                duration_in_seconds = 25,
                active = True
            )
        else:
            return ApiAlertListAlert(
        )
        """

    def testApiAlertListAlert(self):
        """Test ApiAlertListAlert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()