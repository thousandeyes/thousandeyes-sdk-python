# GetEndpointLocalNetworks200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_networks** | [**List[LocalNetworkResult]**](LocalNetworkResult.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from test_results_api.models.get_endpoint_local_networks200_response import GetEndpointLocalNetworks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointLocalNetworks200Response from a JSON string
get_endpoint_local_networks200_response_instance = GetEndpointLocalNetworks200Response.from_json(json)
# print the JSON string representation of the object
print GetEndpointLocalNetworks200Response.to_json()

# convert the object into a dict
get_endpoint_local_networks200_response_dict = get_endpoint_local_networks200_response_instance.to_dict()
# create an instance of GetEndpointLocalNetworks200Response from a dict
get_endpoint_local_networks200_response_form_dict = get_endpoint_local_networks200_response.from_dict(get_endpoint_local_networks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


