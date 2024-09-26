# EndpointPathVisRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_id** | **str** | Unique ID of path trace. | [optional] [readonly] 
**protocol** | [**EndpointTestResultProtocol**](EndpointTestResultProtocol.md) |  | [optional] 
**tcp_path_trace_mode** | [**TcpPathTraceModeResponse**](TcpPathTraceModeResponse.md) |  | [optional] 
**udp_path_trace_mode** | [**UdpPathTraceModeResponse**](UdpPathTraceModeResponse.md) |  | [optional] 
**hops** | [**List[EndpointPathVisHop]**](EndpointPathVisHop.md) | Array of hop objects indicating each step in the traceroute. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_vis_route import EndpointPathVisRoute

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointPathVisRoute from a JSON string
endpoint_path_vis_route_instance = EndpointPathVisRoute.from_json(json)
# print the JSON string representation of the object
print(EndpointPathVisRoute.to_json())

# convert the object into a dict
endpoint_path_vis_route_dict = endpoint_path_vis_route_instance.to_dict()
# create an instance of EndpointPathVisRoute from a dict
endpoint_path_vis_route_from_dict = EndpointPathVisRoute.from_dict(endpoint_path_vis_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


