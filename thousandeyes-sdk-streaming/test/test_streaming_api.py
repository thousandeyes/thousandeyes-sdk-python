# coding: utf-8

"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.streaming.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.streaming.api.streaming_api import StreamingApi


class TestStreamingApi(unittest.TestCase):
    """StreamingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StreamingApi()

    def tearDown(self) -> None:
        pass

    def test_create_stream_models_validation(self) -> None:
        """Test case for create_stream request and response models"""
        request_body_json = """
                {
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "endpointType" : "grpc",
                  "streamEndpointUrl" : "https://api.thousandeyes.otel-collector",
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "type" : "opentelemetry",
                  "dataModelVersion" : "v2",
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  },
                  "enabled" : true
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.streaming.models.Stream.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "endpointType" : "grpc",
                  "_links" : {
                    "self" : {
                      "href" : "https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799"
                    }
                  },
                  "streamEndpointUrl" : "https://api.thousandeyes.otel-collector",
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "type" : "opentelemetry",
                  "enabled" : true,
                  "dataModelVersion" : "v2",
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "id" : "342ieu09",
                  "auditOperation" : {
                    "createdDate" : 1679677853573,
                    "createdBy" : 3962
                  },
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.streaming.models.CreateStreamResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_stream_models_validation(self) -> None:
        """Test case for delete_stream request and response models"""


    def test_get_stream_models_validation(self) -> None:
        """Test case for get_stream request and response models"""

        response_body_json = """
                {
                  "endpointType" : "grpc",
                  "_links" : {
                    "self" : {
                      "href" : "https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799"
                    }
                  },
                  "streamEndpointUrl" : "https://api.thousandeyes.otel-collector",
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "type" : "opentelemetry",
                  "enabled" : true,
                  "dataModelVersion" : "v2",
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "id" : "342ieu09",
                  "auditOperation" : {
                    "createdDate" : 1679677853573,
                    "updatedBy" : 3962,
                    "createdBy" : 3962,
                    "updatedDate" : 1679677853573
                  },
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.streaming.models.GetStreamResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_streams_models_validation(self) -> None:
        """Test case for get_streams request and response models"""

        response_body_json = """
                [ {
                  "endpointType" : "grpc",
                  "_links" : {
                    "self" : {
                      "href" : "https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799"
                    }
                  },
                  "streamEndpointUrl" : "https://api.thousandeyes.otel-collector",
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "type" : "opentelemetry",
                  "enabled" : true,
                  "dataModelVersion" : "v2",
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "id" : "342ieu09",
                  "auditOperation" : {
                    "createdDate" : 1679677853573,
                    "updatedBy" : 3962,
                    "createdBy" : 3962,
                    "updatedDate" : 1679677853573
                  },
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  }
                }, {
                  "endpointType" : "grpc",
                  "_links" : {
                    "self" : {
                      "href" : "https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799"
                    }
                  },
                  "streamEndpointUrl" : "https://api.thousandeyes.otel-collector",
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "type" : "opentelemetry",
                  "enabled" : true,
                  "dataModelVersion" : "v2",
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "id" : "342ieu09",
                  "auditOperation" : {
                    "createdDate" : 1679677853573,
                    "updatedBy" : 3962,
                    "createdBy" : 3962,
                    "updatedDate" : 1679677853573
                  },
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  }
                } ]"""

        response_loaded_json = json.loads(response_body_json)
        response_from_dict = [thousandeyes_sdk.streaming.models.GetStreamResponse.from_dict(value) for value in response_loaded_json]
        self.assertGreater(response_from_dict.__len__(), 0)
        for index, element in enumerate(response_from_dict):
            self.assertIsNotNone(element)
            assert_constructed_model_matches_example_json(element, response_loaded_json[index])

    def test_update_stream_models_validation(self) -> None:
        """Test case for update_stream request and response models"""
        request_body_json = """
                {
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  },
                  "enabled" : true
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.streaming.models.PutStream.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "endpointType" : "grpc",
                  "_links" : {
                    "self" : {
                      "href" : "https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799"
                    }
                  },
                  "streamEndpointUrl" : "https://api.thousandeyes.otel-collector",
                  "exporterConfig" : {
                    "splunkHec" : {
                      "sourceType" : "ThousandEyesOTel",
                      "index" : "thousandeyes_otel_events_index",
                      "source" : "ThousandEyesOTel",
                      "token" : "d0a91307-be2f-4218-a9f8-71c02d98846b"
                    }
                  },
                  "filters" : {
                    "testTypes" : {
                      "values" : [ "agent-to-server", "bgp", "http-server" ]
                    }
                  },
                  "type" : "opentelemetry",
                  "enabled" : true,
                  "dataModelVersion" : "v2",
                  "testMatch" : [ {
                    "id" : "1234",
                    "domain" : "cea"
                  }, {
                    "id" : "5678",
                    "domain" : "endpoint"
                  } ],
                  "tagMatch" : [ {
                    "key" : "keyA",
                    "value" : "valueA"
                  }, {
                    "key" : "keyB",
                    "value" : "valueB"
                  } ],
                  "id" : "342ieu09",
                  "auditOperation" : {
                    "createdDate" : 1679677853573,
                    "updatedBy" : 3962,
                    "createdBy" : 3962,
                    "updatedDate" : 1679677853573
                  },
                  "customHeaders" : {
                    "Authorization" : "*****",
                    "Content-Type" : "*****"
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.streaming.models.GetStreamResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
