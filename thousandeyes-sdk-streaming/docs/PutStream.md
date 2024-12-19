# PutStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_headers** | **Dict[str, str]** | Custom headers. **Note**: When using the &#x60;splunk-hec&#x60; &#x60;type&#x60;, the &#x60;customHeaders&#x60; must contain just one element with the key &#x60;token&#x60; and the value of the *Splunk HEC Token*. | [optional] 
**stream_endpoint_url** | **str** | The URL ThousandEyes sends data stream to. For a URL to be valid, it needs to: - Be syntactically correct. - Be reachable. - Use the HTTPS protocol. - When using the &#x60;grpc&#x60; endpointType, streamEndpointUrl cannot contain paths:     - Valid . &#x60;grpc&#x60; - &#x60;https://example.com&#x60;     - Invalid . &#x60;grpc&#x60; - &#x60;https://example.com/collector&#x60;.     - Valid . &#x60;http&#x60; - &#x60;https://example.com/collector&#x60;.  - When using the &#x60;http&#x60; endpointType, the operation must match the exact final full URL (including the path if there is one) to which the data will be sent. Examples below:     - &#x60;https://api.honeycomb.io:443/v1/metrics&#x60;     - &#x60;https://ingest.eu0.signalfx.com/v2/datapoint/otlp&#x60; | [optional] 
**tag_match** | [**List[TagMatch]**](TagMatch.md) | A collection of tags that determine what tests are included in the data stream. These tag values are also included as attributes in the data stream metrics. | [optional] 
**test_match** | [**List[TestMatch]**](TestMatch.md) | A collection of tests to be included in the data stream. | [optional] 
**enabled** | **bool** | Flag to enable or disable the stream integration. | [optional] 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**exporter_config** | [**ExporterConfig**](ExporterConfig.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.put_stream import PutStream

# TODO update the JSON string below
json = "{}"
# create an instance of PutStream from a JSON string
put_stream_instance = PutStream.from_json(json)
# print the JSON string representation of the object
print(PutStream.to_json())

# convert the object into a dict
put_stream_dict = put_stream_instance.to_dict()
# create an instance of PutStream from a dict
put_stream_from_dict = PutStream.from_dict(put_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


