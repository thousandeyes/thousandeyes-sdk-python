# EndpointNetworkTopologyResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_filters** | [**EndpointNetworkTopologyResultRequestFilter**](EndpointNetworkTopologyResultRequestFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request import EndpointNetworkTopologyResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointNetworkTopologyResultRequest from a JSON string
endpoint_network_topology_result_request_instance = EndpointNetworkTopologyResultRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointNetworkTopologyResultRequest.to_json())

# convert the object into a dict
endpoint_network_topology_result_request_dict = endpoint_network_topology_result_request_instance.to_dict()
# create an instance of EndpointNetworkTopologyResultRequest from a dict
endpoint_network_topology_result_request_from_dict = EndpointNetworkTopologyResultRequest.from_dict(endpoint_network_topology_result_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


