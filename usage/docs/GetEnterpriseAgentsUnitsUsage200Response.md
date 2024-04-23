# GetEnterpriseAgentsUnitsUsage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**List[EnterpriseAgentUnitsByTestOwnerAccountGroupBreakdownsInner]**](EnterpriseAgentUnitsByTestOwnerAccountGroupBreakdownsInner.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from usage.models.get_enterprise_agents_units_usage200_response import GetEnterpriseAgentsUnitsUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnterpriseAgentsUnitsUsage200Response from a JSON string
get_enterprise_agents_units_usage200_response_instance = GetEnterpriseAgentsUnitsUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetEnterpriseAgentsUnitsUsage200Response.to_json())

# convert the object into a dict
get_enterprise_agents_units_usage200_response_dict = get_enterprise_agents_units_usage200_response_instance.to_dict()
# create an instance of GetEnterpriseAgentsUnitsUsage200Response from a dict
get_enterprise_agents_units_usage200_response_from_dict = GetEnterpriseAgentsUnitsUsage200Response.from_dict(get_enterprise_agents_units_usage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


