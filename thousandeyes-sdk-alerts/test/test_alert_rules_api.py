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
from thousandeyes_sdk.alerts.api.alert_rules_api import AlertRulesApi


class TestAlertRulesApi(unittest.TestCase):
    """AlertRulesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AlertRulesApi()

    def tearDown(self) -> None:
        pass

    def test_create_alert_rule_models_validation(self) -> None:
        """Test case for create_alert_rule request and response models"""
        request_body_json = """
                {
                  "severity" : "major",
                  "expression" : "((hops((hopDelay >= 100 ms))))",
                  "alertType" : "http-server",
                  "includeCoveredPrefixes" : true,
                  "roundsViolatingMode" : "exact",
                  "sensitivityLevel" : "medium",
                  "alertGroupType" : "endpoint",
                  "notifyOnClear" : true,
                  "testIds" : [ "281474976710706", "271659" ],
                  "roundsViolatingOutOf" : 5,
                  "roundsViolatingRequired" : 2,
                  "isDefault" : true,
                  "minimumSourcesPct" : 99,
                  "ruleName" : "The End of the Internet",
                  "minimumSources" : 10,
                  "ruleId" : "127094",
                  "notifications" : {
                    "thirdParty" : [ {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    }, {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    } ],
                    "webhook" : [ {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    }, {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    } ],
                    "email" : {
                      "recipients" : [ "noreply@thousandeyes.com" ],
                      "message" : "Notification message"
                    },
                    "customWebhook" : [ {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    }, {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    } ]
                  },
                  "direction" : "to-target"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.alerts.models.RuleDetailUpdate.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "severity" : "major",
                  "expression" : "((hops((hopDelay >= 100 ms))))",
                  "alertType" : "http-server",
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
                  "includeCoveredPrefixes" : true,
                  "roundsViolatingMode" : "exact",
                  "sensitivityLevel" : "medium",
                  "alertGroupType" : "endpoint",
                  "notifyOnClear" : true,
                  "testIds" : [ "281474976710706", "271659" ],
                  "roundsViolatingOutOf" : 5,
                  "roundsViolatingRequired" : 2,
                  "isDefault" : true,
                  "minimumSourcesPct" : 99,
                  "ruleName" : "The End of the Internet",
                  "minimumSources" : 10,
                  "ruleId" : "127094",
                  "notifications" : {
                    "thirdParty" : [ {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    }, {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    } ],
                    "webhook" : [ {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    }, {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    } ],
                    "email" : {
                      "recipients" : [ "noreply@thousandeyes.com" ],
                      "message" : "Notification message"
                    },
                    "customWebhook" : [ {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    }, {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    } ]
                  },
                  "direction" : "to-target"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.Rule.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_alert_rule_models_validation(self) -> None:
        """Test case for delete_alert_rule request and response models"""


    def test_get_alert_rule_models_validation(self) -> None:
        """Test case for get_alert_rule request and response models"""

        response_body_json = """
                {
                  "severity" : "major",
                  "expression" : "((hops((hopDelay >= 100 ms))))",
                  "alertType" : "http-server",
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
                  "includeCoveredPrefixes" : true,
                  "roundsViolatingMode" : "exact",
                  "sensitivityLevel" : "medium",
                  "alertGroupType" : "endpoint",
                  "notifyOnClear" : true,
                  "roundsViolatingOutOf" : 5,
                  "roundsViolatingRequired" : 2,
                  "isDefault" : true,
                  "tests" : [ {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  }, {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  } ],
                  "minimumSourcesPct" : 99,
                  "ruleName" : "The End of the Internet",
                  "minimumSources" : 10,
                  "ruleId" : "127094",
                  "notifications" : {
                    "thirdParty" : [ {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    }, {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    } ],
                    "webhook" : [ {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    }, {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    } ],
                    "email" : {
                      "recipients" : [ "noreply@thousandeyes.com" ],
                      "message" : "Notification message"
                    },
                    "customWebhook" : [ {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    }, {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    } ]
                  },
                  "direction" : "to-target"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.RuleDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_alerts_rules_models_validation(self) -> None:
        """Test case for get_alerts_rules request and response models"""

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
                  "alertRules" : [ {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "includeCoveredPrefixes" : true,
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "alertGroupType" : "endpoint",
                    "notifyOnClear" : true,
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  }, {
                    "severity" : "major",
                    "expression" : "((hops((hopDelay >= 100 ms))))",
                    "alertType" : "http-server",
                    "includeCoveredPrefixes" : true,
                    "roundsViolatingMode" : "exact",
                    "sensitivityLevel" : "medium",
                    "alertGroupType" : "endpoint",
                    "notifyOnClear" : true,
                    "roundsViolatingOutOf" : 5,
                    "roundsViolatingRequired" : 2,
                    "isDefault" : true,
                    "minimumSourcesPct" : 99,
                    "ruleName" : "The End of the Internet",
                    "minimumSources" : 10,
                    "ruleId" : "127094",
                    "direction" : "to-target"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.Rules.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_alert_rule_models_validation(self) -> None:
        """Test case for update_alert_rule request and response models"""
        request_body_json = """
                {
                  "severity" : "major",
                  "expression" : "((hops((hopDelay >= 100 ms))))",
                  "alertType" : "http-server",
                  "includeCoveredPrefixes" : true,
                  "roundsViolatingMode" : "exact",
                  "sensitivityLevel" : "medium",
                  "alertGroupType" : "endpoint",
                  "notifyOnClear" : true,
                  "testIds" : [ "281474976710706", "271659" ],
                  "roundsViolatingOutOf" : 5,
                  "roundsViolatingRequired" : 2,
                  "isDefault" : true,
                  "minimumSourcesPct" : 99,
                  "ruleName" : "The End of the Internet",
                  "minimumSources" : 10,
                  "ruleId" : "127094",
                  "notifications" : {
                    "thirdParty" : [ {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    }, {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    } ],
                    "webhook" : [ {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    }, {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    } ],
                    "email" : {
                      "recipients" : [ "noreply@thousandeyes.com" ],
                      "message" : "Notification message"
                    },
                    "customWebhook" : [ {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    }, {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    } ]
                  },
                  "direction" : "to-target"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.alerts.models.RuleDetailUpdate.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "severity" : "major",
                  "expression" : "((hops((hopDelay >= 100 ms))))",
                  "alertType" : "http-server",
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
                  "includeCoveredPrefixes" : true,
                  "roundsViolatingMode" : "exact",
                  "sensitivityLevel" : "medium",
                  "alertGroupType" : "endpoint",
                  "notifyOnClear" : true,
                  "testIds" : [ "281474976710706", "271659" ],
                  "roundsViolatingOutOf" : 5,
                  "roundsViolatingRequired" : 2,
                  "isDefault" : true,
                  "minimumSourcesPct" : 99,
                  "ruleName" : "The End of the Internet",
                  "minimumSources" : 10,
                  "ruleId" : "127094",
                  "notifications" : {
                    "thirdParty" : [ {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    }, {
                      "integrationType" : "slack",
                      "integrationId" : "sl-101"
                    } ],
                    "webhook" : [ {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    }, {
                      "integrationType" : "webhook",
                      "integrationId" : "wb-201"
                    } ],
                    "email" : {
                      "recipients" : [ "noreply@thousandeyes.com" ],
                      "message" : "Notification message"
                    },
                    "customWebhook" : [ {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    }, {
                      "integrationType" : "custom-webhook",
                      "integrationName" : "My webhook",
                      "integrationId" : "6e069ae9-8537-4120-b988-61bf8e0d8b87",
                      "target" : "https://example.com/test/webhooks/notifications"
                    } ]
                  },
                  "direction" : "to-target"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.alerts.models.Rule.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
