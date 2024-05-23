# EnterpriseAgentUnitsByTestOwnerAccountGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Unique identifier of the account group where some tests are incurring the enterprise agent units. | [optional] 
**account_group_name** | **str** | Name of the account group which owns the tests that are incurring enterprise agent units. | [optional] 
**agent_id** | **str** | Unique identifier of the enterprise agent generating usage. | [optional] 
**agent_name** | **str** | Name of the enterprise agent generating usage. | [optional] 
**enterprise_units_used** | **int** | Number of enterprise agent units owned by the specific account group in the usage period. | [optional] 
**enterprise_units_projected** | **int** | Number of enterprise units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing. | [optional] 
**vagent_id** | **str** | Unique identifier of the virtual agent generating usage | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.enterprise_agent_units_by_test_owner_account_group import EnterpriseAgentUnitsByTestOwnerAccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentUnitsByTestOwnerAccountGroup from a JSON string
enterprise_agent_units_by_test_owner_account_group_instance = EnterpriseAgentUnitsByTestOwnerAccountGroup.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgentUnitsByTestOwnerAccountGroup.to_json())

# convert the object into a dict
enterprise_agent_units_by_test_owner_account_group_dict = enterprise_agent_units_by_test_owner_account_group_instance.to_dict()
# create an instance of EnterpriseAgentUnitsByTestOwnerAccountGroup from a dict
enterprise_agent_units_by_test_owner_account_group_from_dict = EnterpriseAgentUnitsByTestOwnerAccountGroup.from_dict(enterprise_agent_units_by_test_owner_account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


