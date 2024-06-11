# coding: utf-8

"""
    Administrative API

    Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.administrative.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.administrative.api.user_events_api import UserEventsApi


class TestUserEventsApi(unittest.TestCase):
    """UserEventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserEventsApi()

    def tearDown(self) -> None:
        pass

    def test_get_user_events_models_validation(self) -> None:
        """Test case for get_user_events request and response models"""

        response_body_json = """
                {
                  "endDate" : "2022-07-18T22:00:54Z",
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
                  },
                  "auditEvents" : [ {
                    "accountGroupName" : "API Sandbox",
                    "aid" : "1234",
                    "date" : "2020-07-17T21:54:54Z",
                    "event" : "Report created.",
                    "ipAddress" : "99.128.0.0/11",
                    "uid" : "1234",
                    "user" : "API Sandbox User (noreply@thousandeyes.com)",
                    "resources" : [ {
                      "name" : "My New report",
                      "type" : "reportTitle"
                    }, {
                      "name" : "Other Report",
                      "type" : "testName"
                    } ]
                  }, {
                    "accountGroupName" : "API Sandbox",
                    "aid" : "1234",
                    "date" : "2020-07-17T22:00:54Z",
                    "event" : "Login failed.",
                    "ipAddress" : "99.128.0.0/11",
                    "uid" : "1234",
                    "user" : "API Sandbox User (noreply@thousandeyes.com)"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.AuditUserEvents.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
