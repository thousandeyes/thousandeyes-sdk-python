# SimpleAgentAllOfNetworkProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | Autonomous System Number (ASN) announcing the agent&#39;s public IP prefix. | [optional] [readonly] 
**name** | **str** | Name of the network provider organization. | [optional] [readonly] 
**type** | [**NetworkProviderType**](NetworkProviderType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.simple_agent_all_of_network_provider_info import SimpleAgentAllOfNetworkProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAgentAllOfNetworkProviderInfo from a JSON string
simple_agent_all_of_network_provider_info_instance = SimpleAgentAllOfNetworkProviderInfo.from_json(json)
# print the JSON string representation of the object
print(SimpleAgentAllOfNetworkProviderInfo.to_json())

# convert the object into a dict
simple_agent_all_of_network_provider_info_dict = simple_agent_all_of_network_provider_info_instance.to_dict()
# create an instance of SimpleAgentAllOfNetworkProviderInfo from a dict
simple_agent_all_of_network_provider_info_from_dict = SimpleAgentAllOfNetworkProviderInfo.from_dict(simple_agent_all_of_network_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


