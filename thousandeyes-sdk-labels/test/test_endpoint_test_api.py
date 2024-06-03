# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.labels.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.labels.api.endpoint_test_api import EndpointTestApi


class TestEndpointTestApi(unittest.TestCase):
    """EndpointTestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EndpointTestApi()

    def tearDown(self) -> None:
        pass

    def test_create_endpoint_test_label_models_validation(self) -> None:
        """Test case for create_endpoint_test_label request and response models"""
        request_body_json = """
                {
                  "name" : "My new label",
                  "ids" : [ "5048", "1234" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.labels.models.LabelRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "labelId" : "961123",
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
                  "name" : "Label XYZ",
                  "ids" : [ "231286", "6317a3ca0d2bfc6ab882d6ce", "6317a3ca0d2bfc6ab882d6ca" ],
                  "isBuiltIn" : true,
                  "type" : "endpoint-test"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.labels.models.LabelDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_endpoint_test_label_models_validation(self) -> None:
        """Test case for delete_endpoint_test_label request and response models"""


    def test_get_endpoint_test_label_models_validation(self) -> None:
        """Test case for get_endpoint_test_label request and response models"""

        response_body_json = """
                {
                  "labelId" : "961123",
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
                  "name" : "Label XYZ",
                  "ids" : [ "231286", "6317a3ca0d2bfc6ab882d6ce", "6317a3ca0d2bfc6ab882d6ca" ],
                  "isBuiltIn" : true,
                  "type" : "endpoint-test"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.labels.models.LabelDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_endpoint_test_labels_models_validation(self) -> None:
        """Test case for get_endpoint_test_labels request and response models"""

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
                  "labels" : [ {
                    "labelId" : "961123",
                    "name" : "Label XYZ",
                    "isBuiltIn" : true,
                    "type" : "endpoint-test"
                  }, {
                    "labelId" : "961123",
                    "name" : "Label XYZ",
                    "isBuiltIn" : true,
                    "type" : "endpoint-test"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.labels.models.Labels.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_endpoint_test_label_models_validation(self) -> None:
        """Test case for update_endpoint_test_label request and response models"""
        request_body_json = """
                {
                  "name" : "My new label",
                  "ids" : [ "5048", "1234" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.labels.models.LabelRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "labelId" : "961123",
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
                  "name" : "Label XYZ",
                  "ids" : [ "231286", "6317a3ca0d2bfc6ab882d6ce", "6317a3ca0d2bfc6ab882d6ca" ],
                  "isBuiltIn" : true,
                  "type" : "endpoint-test"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.labels.models.LabelDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
