# coding: utf-8

"""
    Agents API

     ## Overview Manage Cloud and Enterprise Agents available to your account in ThousandEyes.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.agents.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.agents.api.cloud_and_enterprise_agent_notification_rules_api import CloudAndEnterpriseAgentNotificationRulesApi


class TestCloudAndEnterpriseAgentNotificationRulesApi(unittest.TestCase):
    """CloudAndEnterpriseAgentNotificationRulesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CloudAndEnterpriseAgentNotificationRulesApi()

    def tearDown(self) -> None:
        pass

    def test_get_agents_notification_rule_models_validation(self) -> None:
        """Test case for get_agents_notification_rule request and response models"""

        response_body_json = """
                {
                  "isDefault" : false,
                  "expression" : "((lastContact >= 30 min))",
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
                  "ruleName" : "Default Agent Offline Notification",
                  "ruleId" : "281474976710706",
                  "notifications" : {
                    "thirdParty" : [ {
                      "integrationType" : "slack",
                      "integrationName" : "integrationSlack1",
                      "authToken" : "0VqDYEpidpHVAK397x8PBsmZ",
                      "channel" : "#slackChannel",
                      "integrationId" : "wb-78",
                      "authMethod" : "Basic",
                      "authUser" : "user123",
                      "target" : "https://hooks.slack.com/services/asd/0VqDYEpidpHVAK397x8PBsmZ"
                    }, {
                      "integrationType" : "slack",
                      "integrationName" : "integrationSlack1",
                      "authToken" : "0VqDYEpidpHVAK397x8PBsmZ",
                      "channel" : "#slackChannel",
                      "integrationId" : "wb-78",
                      "authMethod" : "Basic",
                      "authUser" : "user123",
                      "target" : "https://hooks.slack.com/services/asd/0VqDYEpidpHVAK397x8PBsmZ"
                    } ],
                    "webhook" : [ {
                      "integrationType" : "slack",
                      "integrationName" : "integrationSlack1",
                      "authToken" : "0VqDYEpidpHVAK397x8PBsmZ",
                      "channel" : "#slackChannel",
                      "integrationId" : "wb-78",
                      "authMethod" : "Basic",
                      "authUser" : "user123",
                      "target" : "https://hooks.slack.com/services/asd/0VqDYEpidpHVAK397x8PBsmZ"
                    }, {
                      "integrationType" : "slack",
                      "integrationName" : "integrationSlack1",
                      "authToken" : "0VqDYEpidpHVAK397x8PBsmZ",
                      "channel" : "#slackChannel",
                      "integrationId" : "wb-78",
                      "authMethod" : "Basic",
                      "authUser" : "user123",
                      "target" : "https://hooks.slack.com/services/asd/0VqDYEpidpHVAK397x8PBsmZ"
                    } ],
                    "email" : {
                      "recipients" : [ "user1@thousandeyes.com", "user2@cisco.com" ],
                      "message" : "This test is failing, check as soon as possible."
                    }
                  },
                  "notifyOnClear" : true,
                  "agents" : [ {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  }, {
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "verifySslCertificates" : true
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.agents.models.NotificationRuleDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_agents_notification_rules_models_validation(self) -> None:
        """Test case for get_agents_notification_rules request and response models"""

        response_body_json = """
                {
                  "agentAlertRules" : [ {
                    "ruleId" : "281474976710706",
                    "ruleName" : "Default Agent Offline Notification",
                    "expression" : "((lastContact >= 30 min))",
                    "notifyOnClear" : true,
                    "isDefault" : false
                  }, {
                    "ruleId" : "281474976710709",
                    "ruleName" : "Test Rule",
                    "expression" : "((lastContact >= 40 min))",
                    "notifyOnClear" : true,
                    "isDefault" : true
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
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.agents.models.ListNotificationRulesResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
