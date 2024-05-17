# AllAccountGroupRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_account_group_roles** | [**List[Role]**](Role.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.admin.models.all_account_group_roles import AllAccountGroupRoles

# TODO update the JSON string below
json = "{}"
# create an instance of AllAccountGroupRoles from a JSON string
all_account_group_roles_instance = AllAccountGroupRoles.from_json(json)
# print the JSON string representation of the object
print(AllAccountGroupRoles.to_json())

# convert the object into a dict
all_account_group_roles_dict = all_account_group_roles_instance.to_dict()
# create an instance of AllAccountGroupRoles from a dict
all_account_group_roles_from_dict = AllAccountGroupRoles.from_dict(all_account_group_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


