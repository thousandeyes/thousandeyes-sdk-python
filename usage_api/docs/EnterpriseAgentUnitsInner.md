# EnterpriseAgentUnitsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **object** | Unique identifier of the account group owning the enterprise agent units. | [optional] 
**account_group_name** | **object** | Name of the account group which owns the enterprise agent units. | [optional] 
**agent_id** | **str** | Unique identifier of the enterprise agent generating usage. | [optional] 
**agent_name** | **str** | Name of the enterprise agent generating usage. | [optional] 
**enterprise_units_used** | **int** | Number of enterprise agent units owned by the specific account group in the usage period. | [optional] 
**enterprise_units_projected** | **int** | Number of enterprise units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing. | [optional] 
**vagent_id** | **str** | Unique identifier of the virtual agent generating usage | [optional] 

## Example

```python
from usage_api.models.enterprise_agent_units_inner import EnterpriseAgentUnitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentUnitsInner from a JSON string
enterprise_agent_units_inner_instance = EnterpriseAgentUnitsInner.from_json(json)
# print the JSON string representation of the object
print EnterpriseAgentUnitsInner.to_json()

# convert the object into a dict
enterprise_agent_units_inner_dict = enterprise_agent_units_inner_instance.to_dict()
# create an instance of EnterpriseAgentUnitsInner from a dict
enterprise_agent_units_inner_form_dict = enterprise_agent_units_inner.from_dict(enterprise_agent_units_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


