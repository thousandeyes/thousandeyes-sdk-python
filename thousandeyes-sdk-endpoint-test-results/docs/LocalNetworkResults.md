# LocalNetworkResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_networks** | [**List[LocalNetworkResult]**](LocalNetworkResult.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.local_network_results import LocalNetworkResults

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworkResults from a JSON string
local_network_results_instance = LocalNetworkResults.from_json(json)
# print the JSON string representation of the object
print(LocalNetworkResults.to_json())

# convert the object into a dict
local_network_results_dict = local_network_results_instance.to_dict()
# create an instance of LocalNetworkResults from a dict
local_network_results_from_dict = LocalNetworkResults.from_dict(local_network_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


