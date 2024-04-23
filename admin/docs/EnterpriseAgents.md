# EnterpriseAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[EnterpriseAgent]**](EnterpriseAgent.md) |  | [optional] 

## Example

```python
from admin.models.enterprise_agents import EnterpriseAgents

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgents from a JSON string
enterprise_agents_instance = EnterpriseAgents.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgents.to_json())

# convert the object into a dict
enterprise_agents_dict = enterprise_agents_instance.to_dict()
# create an instance of EnterpriseAgents from a dict
enterprise_agents_from_dict = EnterpriseAgents.from_dict(enterprise_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


