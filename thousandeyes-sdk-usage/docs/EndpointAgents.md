# EndpointAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Unique identifier of the account group owning the endpoint agents. | [optional] 
**account_group_name** | **str** | Name of the account group which owns the endpoint agents. | [optional] 
**endpoint_agents_used** | **int** | Number of endpoint agents owned by the specific account group in the usage period. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.endpoint_agents import EndpointAgents

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgents from a JSON string
endpoint_agents_instance = EndpointAgents.from_json(json)
# print the JSON string representation of the object
print(EndpointAgents.to_json())

# convert the object into a dict
endpoint_agents_dict = endpoint_agents_instance.to_dict()
# create an instance of EndpointAgents from a dict
endpoint_agents_from_dict = EndpointAgents.from_dict(endpoint_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


