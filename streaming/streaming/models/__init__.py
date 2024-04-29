# coding: utf-8

# flake8: noqa
"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from streaming.models.api_error import ApiError
from streaming.models.api_error_integration_limits import ApiErrorIntegrationLimits
from streaming.models.audit_operation import AuditOperation
from streaming.models.audit_operation_with_update import AuditOperationWithUpdate
from streaming.models.bad_request_error import BadRequestError
from streaming.models.create_stream_response import CreateStreamResponse
from streaming.models.endpoint_type import EndpointType
from streaming.models.get_stream_response import GetStreamResponse
from streaming.models.put_stream import PutStream
from streaming.models.put_stream_tag_match_inner import PutStreamTagMatchInner
from streaming.models.stream import Stream
from streaming.models.stream_response import StreamResponse
from streaming.models.stream_response_links import StreamResponseLinks
from streaming.models.stream_response_links_self import StreamResponseLinksSelf
from streaming.models.stream_type import StreamType
from streaming.models.tag_match_object_type import TagMatchObjectType
from streaming.models.unauthorized_error import UnauthorizedError