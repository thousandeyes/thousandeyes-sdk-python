# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alerts.models.alert_rounds_violation_mode import AlertRoundsViolationMode

class TestAlertRoundsViolationMode(unittest.TestCase):
    """AlertRoundsViolationMode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAlertRoundsViolationMode(self):
        """Test AlertRoundsViolationMode"""
        # inst = AlertRoundsViolationMode()

if __name__ == '__main__':
    unittest.main()
