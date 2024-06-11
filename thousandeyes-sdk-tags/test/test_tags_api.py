# coding: utf-8

"""
    Tags API

    The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or alert rules) with meaningful metadata. For example: `branch:sfo`, `branch:nyc`, and `team:netops`.  This feature provides:  * Support for automation. * Powerful and flexible reports/dashboards. * Support for third-party integrations.  Things to note with the ThousandEyes Tags API:  * Tags are backwards-compatible with existing labels. * Tags are separated by Tests (CEA), Agents (CEA), Endpoint Agents, Scheduled Endpoint Tests, and Reports. A single tag can only apply to one type of target object, so each tag must specify the target type of object via a `type` field. * Tags are defined in a single table so that they can be represented using a single model - `Tag`. 

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.tags.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.tags.api.tags_api import TagsApi


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TagsApi()

    def tearDown(self) -> None:
        pass

    def test_create_tag_models_validation(self) -> None:
        """Test case for create_tag request and response models"""
        request_body_json = """
                {
                  "accessType" : "all",
                  "assignments" : [ {
                    "id" : "123",
                    "type" : "test"
                  }, {
                    "id" : "123",
                    "type" : "test"
                  } ],
                  "color" : "#FF0000",
                  "icon" : "icon",
                  "legacyId" : "legacyId",
                  "id" : "5aeab5d5-0d34-4d44-a7ac-fb440185295c",
                  "aid" : 1234,
                  "value" : "sfo",
                  "key" : "branch",
                  "createDate" : "2022-03-01T23:31:11Z",
                  "objectType" : "test"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.TagInfo.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_create_tags_models_validation(self) -> None:
        """Test case for create_tags request and response models"""
        request_body_json = """
                {
                  "errors" : [ {
                    "tag" : {
                      "key" : {
                        "accessType" : "all",
                        "assignments" : [ {
                          "id" : "123",
                          "type" : "test"
                        }, {
                          "id" : "123",
                          "type" : "test"
                        } ],
                        "color" : "#FF0000",
                        "icon" : "icon",
                        "legacyId" : "legacyId",
                        "id" : "5aeab5d5-0d34-4d44-a7ac-fb440185295c",
                        "aid" : 1234,
                        "value" : "sfo",
                        "key" : "branch",
                        "createDate" : "2022-03-01T23:31:11Z",
                        "objectType" : "test"
                      }
                    },
                    "message" : "Object successfully created",
                    "responseCode" : 200
                  }, {
                    "tag" : {
                      "key" : {
                        "accessType" : "all",
                        "assignments" : [ {
                          "id" : "123",
                          "type" : "test"
                        }, {
                          "id" : "123",
                          "type" : "test"
                        } ],
                        "color" : "#FF0000",
                        "icon" : "icon",
                        "legacyId" : "legacyId",
                        "id" : "5aeab5d5-0d34-4d44-a7ac-fb440185295c",
                        "aid" : 1234,
                        "value" : "sfo",
                        "key" : "branch",
                        "createDate" : "2022-03-01T23:31:11Z",
                        "objectType" : "test"
                      }
                    },
                    "message" : "Object successfully created",
                    "responseCode" : 200
                  } ],
                  "tags" : [ {
                    "accessType" : "all",
                    "assignments" : [ {
                      "id" : "123",
                      "type" : "test"
                    }, {
                      "id" : "123",
                      "type" : "test"
                    } ],
                    "color" : "#FF0000",
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
                    "icon" : "icon",
                    "legacyId" : "legacyId",
                    "id" : "5aeab5d5-0d34-4d44-a7ac-fb440185295c",
                    "aid" : 1234,
                    "value" : "sfo",
                    "key" : "branch",
                    "createDate" : "2022-03-01T23:31:11Z",
                    "objectType" : "test"
                  }, {
                    "accessType" : "all",
                    "assignments" : [ {
                      "id" : "123",
                      "type" : "test"
                    }, {
                      "id" : "123",
                      "type" : "test"
                    } ],
                    "color" : "#FF0000",
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
                    "icon" : "icon",
                    "legacyId" : "legacyId",
                    "id" : "5aeab5d5-0d34-4d44-a7ac-fb440185295c",
                    "aid" : 1234,
                    "value" : "sfo",
                    "key" : "branch",
                    "createDate" : "2022-03-01T23:31:11Z",
                    "objectType" : "test"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.BulkTagResponse.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_delete_tag_models_validation(self) -> None:
        """Test case for delete_tag request and response models"""


    def test_get_tag_models_validation(self) -> None:
        """Test case for get_tag request and response models"""


    def test_get_tags_models_validation(self) -> None:
        """Test case for get_tags request and response models"""


    def test_update_tag_models_validation(self) -> None:
        """Test case for update_tag request and response models"""
        request_body_json = """
                {
                  "accessType" : "all",
                  "assignments" : [ {
                    "id" : "123",
                    "type" : "test"
                  }, {
                    "id" : "123",
                    "type" : "test"
                  } ],
                  "color" : "#FF0000",
                  "icon" : "icon",
                  "legacyId" : "legacyId",
                  "id" : "5aeab5d5-0d34-4d44-a7ac-fb440185295c",
                  "aid" : 1234,
                  "value" : "sfo",
                  "key" : "branch",
                  "createDate" : "2022-03-01T23:31:11Z",
                  "objectType" : "test"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.TagInfo.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)



if __name__ == '__main__':
    unittest.main()
