# StreamStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_success** | **int** | Last timestamp when data was successfully sent to the stream endpoint. | [optional] 
**last_failure** | **int** | Last timestamp when data failed to send the stream endpoint. | [optional] 
**status** | [**StreamStatusType**](StreamStatusType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.stream_status import StreamStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StreamStatus from a JSON string
stream_status_instance = StreamStatus.from_json(json)
# print the JSON string representation of the object
print(StreamStatus.to_json())

# convert the object into a dict
stream_status_dict = stream_status_instance.to_dict()
# create an instance of StreamStatus from a dict
stream_status_from_dict = StreamStatus.from_dict(stream_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


