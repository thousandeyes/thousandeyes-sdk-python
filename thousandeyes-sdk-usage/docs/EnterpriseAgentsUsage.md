# EnterpriseAgentsUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**List[EnterpriseAgentUnitsByTestOwnerAccountGroup]**](EnterpriseAgentUnitsByTestOwnerAccountGroup.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.enterprise_agents_usage import EnterpriseAgentsUsage

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentsUsage from a JSON string
enterprise_agents_usage_instance = EnterpriseAgentsUsage.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgentsUsage.to_json())

# convert the object into a dict
enterprise_agents_usage_dict = enterprise_agents_usage_instance.to_dict()
# create an instance of EnterpriseAgentsUsage from a dict
enterprise_agents_usage_from_dict = EnterpriseAgentsUsage.from_dict(enterprise_agents_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


