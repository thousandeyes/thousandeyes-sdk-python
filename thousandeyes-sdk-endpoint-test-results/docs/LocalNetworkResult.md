# LocalNetworkResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **str** | The network ID. Each network occurrence has a unique ID. | [optional] [readonly] 
**network_name** | **str** | The network name. | [optional] [readonly] 
**local_prefix** | **str** | Network local private address. | [optional] [readonly] 
**public_ip_range** | **str** | Network public IP range. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.local_network_result import LocalNetworkResult

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworkResult from a JSON string
local_network_result_instance = LocalNetworkResult.from_json(json)
# print the JSON string representation of the object
print(LocalNetworkResult.to_json())

# convert the object into a dict
local_network_result_dict = local_network_result_instance.to_dict()
# create an instance of LocalNetworkResult from a dict
local_network_result_from_dict = LocalNetworkResult.from_dict(local_network_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


