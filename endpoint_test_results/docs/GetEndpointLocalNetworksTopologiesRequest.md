# GetEndpointLocalNetworksTopologiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_filters** | [**EndpointNetworkTopologyResultRequestFilter**](EndpointNetworkTopologyResultRequestFilter.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.get_endpoint_local_networks_topologies_request import GetEndpointLocalNetworksTopologiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointLocalNetworksTopologiesRequest from a JSON string
get_endpoint_local_networks_topologies_request_instance = GetEndpointLocalNetworksTopologiesRequest.from_json(json)
# print the JSON string representation of the object
print(GetEndpointLocalNetworksTopologiesRequest.to_json())

# convert the object into a dict
get_endpoint_local_networks_topologies_request_dict = get_endpoint_local_networks_topologies_request_instance.to_dict()
# create an instance of GetEndpointLocalNetworksTopologiesRequest from a dict
get_endpoint_local_networks_topologies_request_from_dict = GetEndpointLocalNetworksTopologiesRequest.from_dict(get_endpoint_local_networks_topologies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


