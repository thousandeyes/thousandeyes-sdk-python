# StreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The data stream ID | [optional] [readonly] 
**enabled** | **bool** | Flag to indicate if the stream integration is currently enabled. | [optional] [readonly] 
**links** | [**StreamLinks**](StreamLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.stream_response import StreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResponse from a JSON string
stream_response_instance = StreamResponse.from_json(json)
# print the JSON string representation of the object
print(StreamResponse.to_json())

# convert the object into a dict
stream_response_dict = stream_response_instance.to_dict()
# create an instance of StreamResponse from a dict
stream_response_from_dict = StreamResponse.from_dict(stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


