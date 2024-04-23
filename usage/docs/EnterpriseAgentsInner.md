# EnterpriseAgentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **object** | A unique identifier that specifies the account group that owns the enterprise agents. | [optional] 
**account_group_name** | **object** | Name of the account group which owns the enterprise agents. | [optional] 
**enterprise_agents_used** | **int** | Number of enterprise agents owned by the specific account group in the usage period. | [optional] 

## Example

```python
from usage.models.enterprise_agents_inner import EnterpriseAgentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentsInner from a JSON string
enterprise_agents_inner_instance = EnterpriseAgentsInner.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgentsInner.to_json())

# convert the object into a dict
enterprise_agents_inner_dict = enterprise_agents_inner_instance.to_dict()
# create an instance of EnterpriseAgentsInner from a dict
enterprise_agents_inner_from_dict = EnterpriseAgentsInner.from_dict(enterprise_agents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


