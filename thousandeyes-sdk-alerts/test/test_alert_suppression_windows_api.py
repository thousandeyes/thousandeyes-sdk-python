# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.alerts.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.alerts.api.alert_suppression_windows_api import AlertSuppressionWindowsApi


class TestAlertSuppressionWindowsApi(unittest.TestCase):
    """AlertSuppressionWindowsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AlertSuppressionWindowsApi()

    def tearDown(self) -> None:
        pass

    def test_create_alert_suppression_window_models_validation(self) -> None:
        """Test case for create_alert_suppression_window request and response models"""
        request_body_json = """
                {
                  "duration" : 0,
                  "alertSuppressionWindowId" : "2411",
                  "tests" : [ "71687", "71687" ],
                  "isEnabled" : false,
                  "repeat" : {
                    "intervalType" : "day",
                    "intervalLength" : 2,
                    "type" : "week",
                    "daysOfWeek" : [ "sun", "sun" ]
                  },
                  "endRepeat" : {
                    "date" : "2017-07-01",
                    "count" : 3,
                    "type" : "never"
                  },
                  "name" : "Monthly maintenance",
                  "startDate" : "2017-07-01T05:00:00Z",
                  "status" : "ended"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.alerts.models.AlertSuppressionWindowRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "duration" : 0,
                  "alertSuppressionWindowId" : "2411",
                  "tests" : [ {
                    "alertRules" : [ {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    }, {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    } ],
                    "interval" : 120,
                    "alertsEnabled" : true,
                    "enabled" : true
                  }, {
                    "alertRules" : [ {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    }, {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    } ],
                    "interval" : 120,
                    "alertsEnabled" : true,
                    "enabled" : true
                  } ],
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "isEnabled" : false,
                  "repeat" : {
                    "intervalType" : "day",
                    "intervalLength" : 2,
                    "type" : "week",
                    "daysOfWeek" : [ "sun", "sun" ]
                  },
                  "endRepeat" : {
                    "date" : "2017-07-01",
                    "count" : 3,
                    "type" : "never"
                  },
                  "name" : "Monthly maintenance",
                  "startDate" : "2017-07-01T05:00:00Z",
                  "status" : "ended"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.AlertSuppressionWindowDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_alert_suppression_window_models_validation(self) -> None:
        """Test case for delete_alert_suppression_window request and response models"""


    def test_get_alert_suppression_window_models_validation(self) -> None:
        """Test case for get_alert_suppression_window request and response models"""

        response_body_json = """
                {
                  "duration" : 0,
                  "alertSuppressionWindowId" : "2411",
                  "tests" : [ {
                    "alertRules" : [ {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    }, {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    } ],
                    "interval" : 120,
                    "alertsEnabled" : true,
                    "enabled" : true
                  }, {
                    "alertRules" : [ {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    }, {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    } ],
                    "interval" : 120,
                    "alertsEnabled" : true,
                    "enabled" : true
                  } ],
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "isEnabled" : false,
                  "repeat" : {
                    "intervalType" : "day",
                    "intervalLength" : 2,
                    "type" : "week",
                    "daysOfWeek" : [ "sun", "sun" ]
                  },
                  "endRepeat" : {
                    "date" : "2017-07-01",
                    "count" : 3,
                    "type" : "never"
                  },
                  "name" : "Monthly maintenance",
                  "startDate" : "2017-07-01T05:00:00Z",
                  "status" : "ended"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.AlertSuppressionWindowDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_alert_suppression_windows_models_validation(self) -> None:
        """Test case for get_alert_suppression_windows request and response models"""

        response_body_json = """
                {
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "alertSuppressionWindows" : [ {
                    "duration" : 0,
                    "alertSuppressionWindowId" : "2411",
                    "_links" : {
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "isEnabled" : false,
                    "repeat" : {
                      "intervalType" : "day",
                      "intervalLength" : 2,
                      "type" : "week",
                      "daysOfWeek" : [ "sun", "sun" ]
                    },
                    "endRepeat" : {
                      "date" : "2017-07-01",
                      "count" : 3,
                      "type" : "never"
                    },
                    "name" : "Monthly maintenance",
                    "startDate" : "2017-07-01T05:00:00Z",
                    "status" : "ended"
                  }, {
                    "duration" : 0,
                    "alertSuppressionWindowId" : "2411",
                    "_links" : {
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "isEnabled" : false,
                    "repeat" : {
                      "intervalType" : "day",
                      "intervalLength" : 2,
                      "type" : "week",
                      "daysOfWeek" : [ "sun", "sun" ]
                    },
                    "endRepeat" : {
                      "date" : "2017-07-01",
                      "count" : 3,
                      "type" : "never"
                    },
                    "name" : "Monthly maintenance",
                    "startDate" : "2017-07-01T05:00:00Z",
                    "status" : "ended"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.AlertSuppressionWindows.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_alert_suppression_window_models_validation(self) -> None:
        """Test case for update_alert_suppression_window request and response models"""
        request_body_json = """
                {
                  "duration" : 0,
                  "alertSuppressionWindowId" : "2411",
                  "tests" : [ "71687", "71687" ],
                  "isEnabled" : false,
                  "repeat" : {
                    "intervalType" : "day",
                    "intervalLength" : 2,
                    "type" : "week",
                    "daysOfWeek" : [ "sun", "sun" ]
                  },
                  "endRepeat" : {
                    "date" : "2017-07-01",
                    "count" : 3,
                    "type" : "never"
                  },
                  "name" : "Monthly maintenance",
                  "startDate" : "2017-07-01T05:00:00Z",
                  "status" : "ended"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.alerts.models.AlertSuppressionWindowRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "duration" : 0,
                  "alertSuppressionWindowId" : "2411",
                  "tests" : [ {
                    "alertRules" : [ {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    }, {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    } ],
                    "interval" : 120,
                    "alertsEnabled" : true,
                    "enabled" : true
                  }, {
                    "alertRules" : [ {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    }, {
                      "severity" : "major",
                      "roundsViolatingOutOf" : 5,
                      "roundsViolatingRequired" : 2,
                      "isDefault" : true,
                      "expression" : "((hops((hopDelay >= 100 ms))))",
                      "alertType" : "http-server",
                      "minimumSourcesPct" : 99,
                      "ruleName" : "The End of the Internet",
                      "minimumSources" : 10,
                      "roundsViolatingMode" : "exact",
                      "ruleId" : "127094",
                      "direction" : "to-target"
                    } ],
                    "interval" : 120,
                    "alertsEnabled" : true,
                    "enabled" : true
                  } ],
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "isEnabled" : false,
                  "repeat" : {
                    "intervalType" : "day",
                    "intervalLength" : 2,
                    "type" : "week",
                    "daysOfWeek" : [ "sun", "sun" ]
                  },
                  "endRepeat" : {
                    "date" : "2017-07-01",
                    "count" : 3,
                    "type" : "never"
                  },
                  "name" : "Monthly maintenance",
                  "startDate" : "2017-07-01T05:00:00Z",
                  "status" : "ended"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.AlertSuppressionWindowDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
