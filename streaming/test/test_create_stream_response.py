# coding: utf-8

"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from streaming.models.create_stream_response import CreateStreamResponse

class TestCreateStreamResponse(unittest.TestCase):
    """CreateStreamResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateStreamResponse:
        """Test CreateStreamResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateStreamResponse`
        """
        model = CreateStreamResponse()
        if include_optional:
            return CreateStreamResponse(
                id = '342ieu09',
                enabled = False,
                links = streaming.models.stream_response__links.StreamResponse__links(
                    self = streaming.models.stream_response__links_self.StreamResponse__links_self(
                        href = 'https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799', ), ),
                type = 'opentelemetry',
                endpoint_type = 'grpc',
                stream_endpoint_url = 'https://api.thousandeyes.otel-collector',
                custom_headers = {Authorization=*****, Content-Type=*****},
                tag_match = [{objectType=test, key=keyA, value=valueA}, {objectType=test, key=keyB, value=valueB}],
                audit_operation = streaming.models.audit_operation.AuditOperation(
                    created_by = 3962, 
                    created_date = 1679677853573, )
            )
        else:
            return CreateStreamResponse(
        )
        """

    def testCreateStreamResponse(self):
        """Test CreateStreamResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()