# EndpointAgentsEssentialsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **object** | Unique identifier of the account group owning the endpoint agents essentials. | [optional] 
**account_group_name** | **object** | Name of the account group which owns the endpoint agents essentials. | [optional] 
**endpoint_agents_essentials_used** | **int** | Number of endpoint agents essentials owned by the specific account group in the usage period. | [optional] 

## Example

```python
from usage.models.endpoint_agents_essentials_inner import EndpointAgentsEssentialsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsEssentialsInner from a JSON string
endpoint_agents_essentials_inner_instance = EndpointAgentsEssentialsInner.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentsEssentialsInner.to_json())

# convert the object into a dict
endpoint_agents_essentials_inner_dict = endpoint_agents_essentials_inner_instance.to_dict()
# create an instance of EndpointAgentsEssentialsInner from a dict
endpoint_agents_essentials_inner_from_dict = EndpointAgentsEssentialsInner.from_dict(endpoint_agents_essentials_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


