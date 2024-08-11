# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.endpoint_labels.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.endpoint_labels.api.manage_labels_api import ManageLabelsApi


class TestManageLabelsApi(unittest.TestCase):
    """ManageLabelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManageLabelsApi()

    def tearDown(self) -> None:
        pass

    def test_create_endpoint_label_models_validation(self) -> None:
        """Test case for create_endpoint_label request and response models"""
        request_body_json = """
                {
                  "color" : "#ff3333",
                  "matchType" : "and",
                  "name" : "Head office meeting rooms",
                  "id" : "abc-123-def",
                  "filters" : [ {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  }, {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_labels.models.LabelRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "color" : "#ff3333",
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
                  "matchType" : "and",
                  "name" : "Head office meeting rooms",
                  "id" : "abc-123-def",
                  "filters" : [ {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  }, {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_labels.models.LabelResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_endpoint_label_models_validation(self) -> None:
        """Test case for delete_endpoint_label request and response models"""


    def test_get_endpoint_label_models_validation(self) -> None:
        """Test case for get_endpoint_label request and response models"""

        response_body_json = """
                {
                  "color" : "#ff3333",
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
                  "matchType" : "and",
                  "name" : "Head office meeting rooms",
                  "id" : "abc-123-def",
                  "filters" : [ {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  }, {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_labels.models.LabelResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_endpoint_labels_models_validation(self) -> None:
        """Test case for get_endpoint_labels request and response models"""

        response_body_json = """
                {
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
                    "color" : "#ff3333",
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
                    "matchType" : "and",
                    "name" : "Head office meeting rooms",
                    "id" : "abc-123-def",
                    "filters" : [ {
                      "mode" : "in",
                      "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                      "key" : "vpn-client-network"
                    }, {
                      "mode" : "in",
                      "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                      "key" : "vpn-client-network"
                    } ]
                  }, {
                    "color" : "#ff3333",
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
                    "matchType" : "and",
                    "name" : "Head office meeting rooms",
                    "id" : "abc-123-def",
                    "filters" : [ {
                      "mode" : "in",
                      "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                      "key" : "vpn-client-network"
                    }, {
                      "mode" : "in",
                      "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                      "key" : "vpn-client-network"
                    } ]
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_labels.models.Labels.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_endpoint_label_models_validation(self) -> None:
        """Test case for update_endpoint_label request and response models"""
        request_body_json = """
                {
                  "color" : "#ff3333",
                  "matchType" : "and",
                  "name" : "Head office meeting rooms",
                  "id" : "abc-123-def",
                  "filters" : [ {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  }, {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_labels.models.Label.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "color" : "#ff3333",
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
                  "matchType" : "and",
                  "name" : "Head office meeting rooms",
                  "id" : "abc-123-def",
                  "filters" : [ {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  }, {
                    "mode" : "in",
                    "values" : [ "10.1.1.0/24", "192.168.1.0/24" ],
                    "key" : "vpn-client-network"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_labels.models.LabelResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
