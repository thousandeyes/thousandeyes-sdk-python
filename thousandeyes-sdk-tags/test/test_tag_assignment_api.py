# coding: utf-8

"""
    Tags API

    The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or alert rules) with meaningful metadata. For example: `branch:sfo`, `branch:nyc`, and `team:netops`.  This feature provides:  * Support for automation. * Powerful and flexible reports/dashboards. * Support for third-party integrations.  Things to note with the ThousandEyes Tags API:  * Tags are backwards-compatible with existing labels. * Tags are separated by Tests (CEA), Agents (CEA), Endpoint Agents, Scheduled Endpoint Tests, and Reports. A single tag can only apply to one type of target object, so each tag must specify the target type of object via a `type` field. * Tags are defined in a single table so that they can be represented using a single model - `Tag`. 

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.tags.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.tags.api.tag_assignment_api import TagAssignmentApi


class TestTagAssignmentApi(unittest.TestCase):
    """TagAssignmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TagAssignmentApi()

    def tearDown(self) -> None:
        pass

    def test_assign_tag_models_validation(self) -> None:
        """Test case for assign_tag request and response models"""
        request_body_json = """
                {
                  "assignments" : [ {
                    "id" : "123",
                    "type" : "test"
                  }, {
                    "id" : "123",
                    "type" : "test"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.TagAssignment.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_assign_tags_models_validation(self) -> None:
        """Test case for assign_tags request and response models"""
        request_body_json = """
                {
                  "tags" : [ {
                    "assignments" : [ {
                      "id" : "123",
                      "type" : "test"
                    }, {
                      "id" : "123",
                      "type" : "test"
                    } ],
                    "tagId" : "c6b78e57-81a2-4c5f-a11a-d96c3c664d55"
                  }, {
                    "assignments" : [ {
                      "id" : "123",
                      "type" : "test"
                    }, {
                      "id" : "123",
                      "type" : "test"
                    } ],
                    "tagId" : "c6b78e57-81a2-4c5f-a11a-d96c3c664d55"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.BulkTagAssignments.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_unassign_tag_models_validation(self) -> None:
        """Test case for unassign_tag request and response models"""
        request_body_json = """
                {
                  "assignments" : [ {
                    "id" : "123",
                    "type" : "test"
                  }, {
                    "id" : "123",
                    "type" : "test"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.TagAssignment.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_unassign_tags_models_validation(self) -> None:
        """Test case for unassign_tags request and response models"""
        request_body_json = """
                {
                  "tags" : [ {
                    "assignments" : [ {
                      "id" : "123",
                      "type" : "test"
                    }, {
                      "id" : "123",
                      "type" : "test"
                    } ],
                    "tagId" : "c6b78e57-81a2-4c5f-a11a-d96c3c664d55"
                  }, {
                    "assignments" : [ {
                      "id" : "123",
                      "type" : "test"
                    }, {
                      "id" : "123",
                      "type" : "test"
                    } ],
                    "tagId" : "c6b78e57-81a2-4c5f-a11a-d96c3c664d55"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tags.models.BulkTagAssignments.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)



if __name__ == '__main__':
    unittest.main()
