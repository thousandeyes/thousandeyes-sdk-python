# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alerts.models.alert import Alert

class TestAlert(unittest.TestCase):
    """Alert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Alert:
        """Test Alert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Alert`
        """
        model = Alert()
        if include_optional:
            return Alert(
                id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569',
                alert_type = 'http-server',
                start_date = '2020-04-23T13:43:16Z',
                end_date = '2020-04-23T13:43:16Z',
                violation_count = 2,
                duration = 60,
                suppressed = False,
                meta = alerts.models.base_alert_all_of_meta.BaseAlert_allOf_meta(
                    version = 1, ),
                links = alerts.models.alert_links__links.AlertLinks__links(
                    test = alerts.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    rule = alerts.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    app_link = , 
                    self = , ),
                alert_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569',
                date_start = '2020-04-23 13:43:16',
                date_end = '2020-04-23 13:43:16',
                rule_id = 127094,
                state = 'ACTIVE',
                severity = 'MAJOR',
                permalink = 'https://app.thousandeyes.com/alerts/list?__a=75&alertId=2783&agentId=12',
                api_links = [
                    { }
                    ],
                alert_rule_id = '127094',
                alert_state = 'active',
                alert_severity = 'major'
            )
        else:
            return Alert(
        )
        """

    def testAlert(self):
        """Test Alert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()