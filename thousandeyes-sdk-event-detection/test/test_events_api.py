# coding: utf-8

"""
    Event Detection API

     Event detection occurs when ThousandEyes identifies that error signals related to a component (proxy, network node, AS, server etc) have deviated from the baselines established by events. * To determine this, ThousandEyes takes the test results from all accounts groups within an organization, and analyzes that data. * Noisy test results (those that have too many errors in a short window) are removed until they stabilize, and the rest of the results are tagged with the components associated with that test result (for example, proxy, network, or server). * Next, any increase in failures from the test results and each component helps in determining the problem domain and which component may be at fault. * When this failure rate increases beyond a pre-defined threshold (set by the algorithm), an event is triggered and an email notification is sent to the user (if they've enabled email alerts).  With the Events API, you can perform the following tasks on the ThousandEyes platform: * **Retrieve Events**: Obtain a list of events and detailed information for each event. For more information about events, see [Event Detection](https://docs.thousandeyes.com/product-documentation/event-detection). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.event_detection.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.event_detection.api.events_api import EventsApi


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventsApi()

    def tearDown(self) -> None:
        pass

    def test_get_event_models_validation(self) -> None:
        """Test case for get_event request and response models"""

        response_body_json = """
                {
                  "severity" : "medium",
                  "summary" : "Significant number of issues detected with 66.29.146.15",
                  "affectedTests" : {
                    "total" : 5,
                    "tests" : [ {
                      "affectedTargetIds" : [ "123", "1234" ],
                      "affectedAgentIds" : [ "2954", "2953" ],
                      "_links" : {
                        "test" : {
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
                      "name" : "Google test",
                      "testType" : "agent-to-server",
                      "testId" : "226770"
                    }, {
                      "affectedTargetIds" : [ "123", "1234" ],
                      "affectedAgentIds" : [ "2954", "2953" ],
                      "_links" : {
                        "test" : {
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
                      "name" : "Google test",
                      "testType" : "agent-to-server",
                      "testId" : "226770"
                    } ],
                    "inAccountGroup" : 2
                  },
                  "endDate" : "2020-04-23T13:43:16Z",
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
                  "typeName" : "Network Issue",
                  "cause" : [ "Network Loss and/or High RTT" ],
                  "affectedTargets" : {
                    "total" : 5,
                    "inAccountGroup" : 2,
                    "targets" : [ {
                      "affectedAgentIds" : [ "2954", "2953" ],
                      "ip" : "216.239.32.10",
                      "name" : "google.com",
                      "affectedTestIds" : [ "123", "1234" ],
                      "serverId" : "123"
                    }, {
                      "affectedAgentIds" : [ "2954", "2953" ],
                      "ip" : "216.239.32.10",
                      "name" : "google.com",
                      "affectedTestIds" : [ "123", "1234" ],
                      "serverId" : "123"
                    } ]
                  },
                  "type" : "target",
                  "grouping" : {
                    "target" : "google.com"
                  },
                  "affectedAgents" : {
                    "total" : 5,
                    "inAccountGroup" : 2,
                    "agents" : [ {
                      "affectedTargetIds" : [ "123", "1234" ],
                      "agentId" : "2954",
                      "_links" : {
                        "agent" : {
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
                      "countryCode" : "BR",
                      "name" : "São Paulo, Brazil - agent",
                      "location" : "São Paulo, Brazil",
                      "affectedTestIds" : [ "2954", "2953" ],
                      "type" : "enterprise-cluster"
                    }, {
                      "affectedTargetIds" : [ "123", "1234" ],
                      "agentId" : "2954",
                      "_links" : {
                        "agent" : {
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
                      "countryCode" : "BR",
                      "name" : "São Paulo, Brazil - agent",
                      "location" : "São Paulo, Brazil",
                      "affectedTestIds" : [ "2954", "2953" ],
                      "type" : "enterprise-cluster"
                    } ]
                  },
                  "id" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                  "state" : "resolved",
                  "aid" : "1234",
                  "startDate" : "2020-04-23T13:43:16Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.event_detection.models.EventDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_events_models_validation(self) -> None:
        """Test case for get_events request and response models"""

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
                  "aid" : "1234",
                  "startDate" : "2022-07-17T22:00:54Z",
                  "events" : [ {
                    "severity" : "medium",
                    "affectedTests" : {
                      "total" : 5,
                      "inAccountGroup" : 2
                    },
                    "endDate" : "2020-04-23T13:43:16Z",
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
                    "affectedAgents" : {
                      "total" : 5,
                      "inAccountGroup" : 2
                    },
                    "typeName" : "Network Issue",
                    "id" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                    "state" : "resolved",
                    "title" : "Affecting destinations in google.com",
                    "type" : "target",
                    "affectedTargets" : {
                      "total" : 5,
                      "inAccountGroup" : 2
                    },
                    "startDate" : "2020-04-23T13:43:16Z"
                  }, {
                    "severity" : "medium",
                    "affectedTests" : {
                      "total" : 5,
                      "inAccountGroup" : 2
                    },
                    "endDate" : "2020-04-23T13:43:16Z",
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
                    "affectedAgents" : {
                      "total" : 5,
                      "inAccountGroup" : 2
                    },
                    "typeName" : "Network Issue",
                    "id" : "e9c3bf02-a48c-4aa8-9e5f-898800d6f569",
                    "state" : "resolved",
                    "title" : "Affecting destinations in google.com",
                    "type" : "target",
                    "affectedTargets" : {
                      "total" : 5,
                      "inAccountGroup" : 2
                    },
                    "startDate" : "2020-04-23T13:43:16Z"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.event_detection.models.Events.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()