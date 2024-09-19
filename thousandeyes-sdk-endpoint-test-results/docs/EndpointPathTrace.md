# EndpointPathTrace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the hop destination. | [optional] [readonly] 
**number_of_hops** | **int** | Number of hops for path trace to destination. | [optional] [readonly] 
**protocol** | [**EndpointTestResultProtocol**](EndpointTestResultProtocol.md) |  | [optional] 
**tcp_path_trace_mode** | [**TcpPathTraceModeResponse**](TcpPathTraceModeResponse.md) |  | [optional] 
**udp_path_trace_mode** | [**UdpPathTraceModeResponse**](UdpPathTraceModeResponse.md) |  | [optional] 
**path_id** | **str** | Unique ID of path trace. | [optional] [readonly] 
**response_time** | **int** | RTT of the path trace to the destination in milliseconds. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_trace import EndpointPathTrace

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointPathTrace from a JSON string
endpoint_path_trace_instance = EndpointPathTrace.from_json(json)
# print the JSON string representation of the object
print(EndpointPathTrace.to_json())

# convert the object into a dict
endpoint_path_trace_dict = endpoint_path_trace_instance.to_dict()
# create an instance of EndpointPathTrace from a dict
endpoint_path_trace_from_dict = EndpointPathTrace.from_dict(endpoint_path_trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


