# GetStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The data stream ID | [optional] [readonly] 
**enabled** | **bool** | Flag to enable or disable the stream integration. | [optional] 
**links** | [**StreamLinks**](StreamLinks.md) |  | [optional] 
**type** | [**StreamType**](StreamType.md) |  | [optional] 
**signal** | [**Signal**](Signal.md) |  | [optional] 
**endpoint_type** | [**EndpointType**](EndpointType.md) |  | [optional] 
**stream_endpoint_url** | **str** | The URL ThousandEyes sends data stream to. For a URL to be valid, it needs to: - Be syntactically correct. - Be reachable. - Use the HTTPS protocol. - When using the &#x60;grpc&#x60; endpointType, streamEndpointUrl cannot contain paths:     - Valid . &#x60;grpc&#x60; - &#x60;https://example.com&#x60;     - Invalid . &#x60;grpc&#x60; - &#x60;https://example.com/collector&#x60;.     - Valid . &#x60;http&#x60; - &#x60;https://example.com/collector&#x60;.  - When using the &#x60;http&#x60; endpointType, the operation must match the exact final full URL (including the path if there is one) to which the data will be sent. Examples below:     - &#x60;https://api.honeycomb.io:443/v1/metrics&#x60;     - &#x60;https://ingest.eu0.signalfx.com/v2/datapoint/otlp&#x60; | [optional] 
**data_model_version** | [**DataModelVersion**](DataModelVersion.md) |  | [optional] 
**custom_headers** | **Dict[str, str]** | Custom headers. | [optional] 
**tag_match** | [**List[TagMatch]**](TagMatch.md) | A collection of tags that determine what tests are included in the data stream. These tag values are also included as attributes in the data stream metrics. | [optional] 
**test_match** | [**List[TestMatch]**](TestMatch.md) | A collection of tests to be included in the data stream. | [optional] 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**exporter_config** | [**ExporterConfig**](ExporterConfig.md) |  | [optional] 
**audit_operation** | [**AuditOperationWithUpdate**](AuditOperationWithUpdate.md) |  | [optional] 
**stream_status** | [**StreamStatus**](StreamStatus.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.get_stream_response import GetStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStreamResponse from a JSON string
get_stream_response_instance = GetStreamResponse.from_json(json)
# print the JSON string representation of the object
print(GetStreamResponse.to_json())

# convert the object into a dict
get_stream_response_dict = get_stream_response_instance.to_dict()
# create an instance of GetStreamResponse from a dict
get_stream_response_from_dict = GetStreamResponse.from_dict(get_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


