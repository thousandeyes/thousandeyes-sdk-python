# GetEndpointLocalNetworkTopologyDetails200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[LocalNetworkTopologyResult]**](LocalNetworkTopologyResult.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from test_results_api.models.get_endpoint_local_network_topology_details200_response import GetEndpointLocalNetworkTopologyDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointLocalNetworkTopologyDetails200Response from a JSON string
get_endpoint_local_network_topology_details200_response_instance = GetEndpointLocalNetworkTopologyDetails200Response.from_json(json)
# print the JSON string representation of the object
print GetEndpointLocalNetworkTopologyDetails200Response.to_json()

# convert the object into a dict
get_endpoint_local_network_topology_details200_response_dict = get_endpoint_local_network_topology_details200_response_instance.to_dict()
# create an instance of GetEndpointLocalNetworkTopologyDetails200Response from a dict
get_endpoint_local_network_topology_details200_response_form_dict = get_endpoint_local_network_topology_details200_response.from_dict(get_endpoint_local_network_topology_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


