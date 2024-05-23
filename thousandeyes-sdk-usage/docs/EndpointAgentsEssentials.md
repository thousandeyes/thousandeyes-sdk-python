# EndpointAgentsEssentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Unique identifier of the account group owning the endpoint agents essentials. | [optional] 
**account_group_name** | **str** | Name of the account group which owns the endpoint agents essentials. | [optional] 
**endpoint_agents_essentials_used** | **int** | Number of endpoint agents essentials owned by the specific account group in the usage period. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.endpoint_agents_essentials import EndpointAgentsEssentials

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsEssentials from a JSON string
endpoint_agents_essentials_instance = EndpointAgentsEssentials.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentsEssentials.to_json())

# convert the object into a dict
endpoint_agents_essentials_dict = endpoint_agents_essentials_instance.to_dict()
# create an instance of EndpointAgentsEssentials from a dict
endpoint_agents_essentials_from_dict = EndpointAgentsEssentials.from_dict(endpoint_agents_essentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


