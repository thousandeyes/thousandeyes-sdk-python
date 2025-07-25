# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.alerts.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.alerts.api.alerts_api import AlertsApi


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AlertsApi()

    def tearDown(self) -> None:
        pass

    def test_get_alert_models_validation(self) -> None:
        """Test case for get_alert request and response models"""

        response_body_json = """
                {
                  "severity" : "major",
                  "alertType" : "http-server",
                  "endDate" : "2022-07-18T22:00:54Z",
                  "_links" : {
                    "appLink" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "test" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "rule" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
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
                  "alertSeverity" : "major",
                  "duration" : 60,
                  "violationCount" : 2,
                  "meta" : {
                    "version" : 1
                  },
                  "details" : [ {
                    "name" : "Bucharest, Romania",
                    "start" : {
                      "metrics" : "metrics"
                    },
                    "end" : {
                      "metrics" : "metrics"
                    },
                    "id" : "3379",
                    "state" : "trigger",
                    "type" : "cea_agent"
                  }, {
                    "name" : "Bucharest, Romania",
                    "start" : {
                      "metrics" : "metrics"
                    },
                    "end" : {
                      "metrics" : "metrics"
                    },
                    "id" : "3379",
                    "state" : "trigger",
                    "type" : "cea_agent"
                  } ],
                  "id" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                  "suppressed" : false,
                  "state" : "trigger",
                  "alertState" : "trigger",
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.AlertDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_alerts_models_validation(self) -> None:
        """Test case for get_alerts request and response models"""

        response_body_json = """
                {
                  "alerts" : [ {
                    "severity" : "MAJOR",
                    "alertType" : "http-server",
                    "endDate" : "2022-07-18T22:00:54Z",
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      },
                      "test" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      },
                      "rule" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      },
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
                    "apiLinks" : [ {
                      "key" : ""
                    }, {
                      "key" : ""
                    } ],
                    "alertSeverity" : "major",
                    "dateEnd" : "2020-04-23 13:43:16",
                    "duration" : 60,
                    "violationCount" : 2,
                    "dateStart" : "2020-04-23 13:43:16",
                    "meta" : {
                      "version" : 1
                    },
                    "id" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                    "suppressed" : false,
                    "alertId" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                    "state" : "ACTIVE",
                    "ruleId" : 127094,
                    "permalink" : "https://app.thousandeyes.com/alerts/list?__a=75&alertId=2783&agentId=12",
                    "alertState" : "trigger",
                    "startDate" : "2022-07-17T22:00:54Z",
                    "alertRuleId" : "127094"
                  }, {
                    "severity" : "MAJOR",
                    "alertType" : "http-server",
                    "endDate" : "2022-07-18T22:00:54Z",
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      },
                      "test" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      },
                      "rule" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      },
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
                    "apiLinks" : [ {
                      "key" : ""
                    }, {
                      "key" : ""
                    } ],
                    "alertSeverity" : "major",
                    "dateEnd" : "2020-04-23 13:43:16",
                    "duration" : 60,
                    "violationCount" : 2,
                    "dateStart" : "2020-04-23 13:43:16",
                    "meta" : {
                      "version" : 1
                    },
                    "id" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                    "suppressed" : false,
                    "alertId" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                    "state" : "ACTIVE",
                    "ruleId" : 127094,
                    "permalink" : "https://app.thousandeyes.com/alerts/list?__a=75&alertId=2783&agentId=12",
                    "alertState" : "trigger",
                    "startDate" : "2022-07-17T22:00:54Z",
                    "alertRuleId" : "127094"
                  } ],
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
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
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.Alerts.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
