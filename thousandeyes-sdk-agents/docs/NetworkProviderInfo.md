# NetworkProviderInfo

Information about the network provider that owns the agent's public IP prefix.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | Autonomous System Number (ASN) announcing the agent&#39;s public IP prefix. | [optional] [readonly] 
**name** | **str** | Name of the network provider organization. | [optional] [readonly] 
**type** | [**NetworkProviderType**](NetworkProviderType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.network_provider_info import NetworkProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProviderInfo from a JSON string
network_provider_info_instance = NetworkProviderInfo.from_json(json)
# print the JSON string representation of the object
print(NetworkProviderInfo.to_json())

# convert the object into a dict
network_provider_info_dict = network_provider_info_instance.to_dict()
# create an instance of NetworkProviderInfo from a dict
network_provider_info_from_dict = NetworkProviderInfo.from_dict(network_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


