# EnterpriseAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier that specifies the account group that owns the enterprise agents. | [optional] 
**account_group_name** | **str** | Name of the account group which owns the enterprise agents. | [optional] 
**enterprise_agents_used** | **int** | Number of enterprise agents owned by the specific account group in the usage period. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.enterprise_agents import EnterpriseAgents

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


