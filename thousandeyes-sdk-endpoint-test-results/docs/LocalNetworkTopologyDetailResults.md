# LocalNetworkTopologyDetailResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[LocalNetworkTopologyResult]**](LocalNetworkTopologyResult.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_detail_results import LocalNetworkTopologyDetailResults

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworkTopologyDetailResults from a JSON string
local_network_topology_detail_results_instance = LocalNetworkTopologyDetailResults.from_json(json)
# print the JSON string representation of the object
print(LocalNetworkTopologyDetailResults.to_json())

# convert the object into a dict
local_network_topology_detail_results_dict = local_network_topology_detail_results_instance.to_dict()
# create an instance of LocalNetworkTopologyDetailResults from a dict
local_network_topology_detail_results_from_dict = LocalNetworkTopologyDetailResults.from_dict(local_network_topology_detail_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


