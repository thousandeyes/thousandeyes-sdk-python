# LocalNetworkTopologyResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[LocalNetworkTopologyResultBase]**](LocalNetworkTopologyResultBase.md) |  | [optional] 

## Example

```python
from test_results_api.models.local_network_topology_results import LocalNetworkTopologyResults

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworkTopologyResults from a JSON string
local_network_topology_results_instance = LocalNetworkTopologyResults.from_json(json)
# print the JSON string representation of the object
print LocalNetworkTopologyResults.to_json()

# convert the object into a dict
local_network_topology_results_dict = local_network_topology_results_instance.to_dict()
# create an instance of LocalNetworkTopologyResults from a dict
local_network_topology_results_form_dict = local_network_topology_results.from_dict(local_network_topology_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


