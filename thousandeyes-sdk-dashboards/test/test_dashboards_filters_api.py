# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.dashboards.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.dashboards.api.dashboards_filters_api import DashboardsFiltersApi


class TestDashboardsFiltersApi(unittest.TestCase):
    """DashboardsFiltersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DashboardsFiltersApi()

    def tearDown(self) -> None:
        pass

    def test_create_dashboard_filter_models_validation(self) -> None:
        """Test case for create_dashboard_filter request and response models"""
        request_body_json = """
                {
                  "context" : [ {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  }, {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  } ],
                  "name" : "cea-filter",
                  "description" : "Global filter for CEA widgets"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.dashboards.models.ApiContextFilterRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "createdDate" : "2024-02-01T22:19:19Z",
                  "createdBy" : {
                    "uid" : "1",
                    "name" : "Test User"
                  },
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
                  "context" : [ {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  }, {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  } ],
                  "name" : "cea-filter",
                  "modifiedDate" : "2024-02-01T22:19:19Z",
                  "description" : "Global filter for CEA widgets",
                  "modifiedBy" : {
                    "uid" : "1",
                    "name" : "Test User"
                  },
                  "id" : "65bc18e8f2073a4a469cd958",
                  "aid" : "11"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.dashboards.models.ApiContextFilterResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_dashboard_filter_models_validation(self) -> None:
        """Test case for delete_dashboard_filter request and response models"""


    def test_get_dashboard_filter_models_validation(self) -> None:
        """Test case for get_dashboard_filter request and response models"""

        response_body_json = """
                {
                  "createdDate" : "2024-02-01T22:19:19Z",
                  "createdBy" : {
                    "uid" : "1",
                    "name" : "Test User"
                  },
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
                  "context" : [ {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  }, {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  } ],
                  "name" : "cea-filter",
                  "modifiedDate" : "2024-02-01T22:19:19Z",
                  "description" : "Global filter for CEA widgets",
                  "modifiedBy" : {
                    "uid" : "1",
                    "name" : "Test User"
                  },
                  "id" : "65bc18e8f2073a4a469cd958",
                  "aid" : "11"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.dashboards.models.ApiContextFilterResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_dashboards_filters_models_validation(self) -> None:
        """Test case for get_dashboards_filters request and response models"""

        response_body_json = """
                {
                  "dashboardFilters" : [ {
                    "createdDate" : "2024-02-01T22:19:19Z",
                    "createdBy" : {
                      "uid" : "1",
                      "name" : "Test User"
                    },
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
                    "context" : [ {
                      "dataSourceId" : "VIRTUAL_AGENT",
                      "filters" : [ {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      }, {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      } ]
                    }, {
                      "dataSourceId" : "VIRTUAL_AGENT",
                      "filters" : [ {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      }, {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      } ]
                    } ],
                    "name" : "cea-filter",
                    "modifiedDate" : "2024-02-01T22:19:19Z",
                    "description" : "Global filter for CEA widgets",
                    "modifiedBy" : {
                      "uid" : "1",
                      "name" : "Test User"
                    },
                    "id" : "65bc18e8f2073a4a469cd958",
                    "aid" : "11"
                  }, {
                    "createdDate" : "2024-02-01T22:19:19Z",
                    "createdBy" : {
                      "uid" : "1",
                      "name" : "Test User"
                    },
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
                    "context" : [ {
                      "dataSourceId" : "VIRTUAL_AGENT",
                      "filters" : [ {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      }, {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      } ]
                    }, {
                      "dataSourceId" : "VIRTUAL_AGENT",
                      "filters" : [ {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      }, {
                        "filterId" : "TEST_LABEL",
                        "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                        "values" : [ "45862", "59749" ]
                      } ]
                    } ],
                    "name" : "cea-filter",
                    "modifiedDate" : "2024-02-01T22:19:19Z",
                    "description" : "Global filter for CEA widgets",
                    "modifiedBy" : {
                      "uid" : "1",
                      "name" : "Test User"
                    },
                    "id" : "65bc18e8f2073a4a469cd958",
                    "aid" : "11"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.dashboards.models.ApiContextFiltersResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_dashboard_filter_models_validation(self) -> None:
        """Test case for update_dashboard_filter request and response models"""
        request_body_json = """
                {
                  "context" : [ {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  }, {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  } ],
                  "name" : "cea-filter",
                  "description" : "Global filter for CEA widgets"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.dashboards.models.ApiContextFilterRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "createdDate" : "2024-02-01T22:19:19Z",
                  "createdBy" : {
                    "uid" : "1",
                    "name" : "Test User"
                  },
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
                  "context" : [ {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  }, {
                    "dataSourceId" : "VIRTUAL_AGENT",
                    "filters" : [ {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    }, {
                      "filterId" : "TEST_LABEL",
                      "metricIds" : [ "WEB_PAGE_LOAD_COMPLETION_RATE", "WEB_TTFB", "WEB_AVAILABILITY" ],
                      "values" : [ "45862", "59749" ]
                    } ]
                  } ],
                  "name" : "cea-filter",
                  "modifiedDate" : "2024-02-01T22:19:19Z",
                  "description" : "Global filter for CEA widgets",
                  "modifiedBy" : {
                    "uid" : "1",
                    "name" : "Test User"
                  },
                  "id" : "65bc18e8f2073a4a469cd958",
                  "aid" : "11"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.dashboards.models.ApiContextFilterResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
