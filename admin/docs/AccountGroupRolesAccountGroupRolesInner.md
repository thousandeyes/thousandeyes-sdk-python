# AccountGroupRolesAccountGroupRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group** | [**AccountGroup1**](AccountGroup1.md) |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 

## Example

```python
from admin.models.account_group_roles_account_group_roles_inner import AccountGroupRolesAccountGroupRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupRolesAccountGroupRolesInner from a JSON string
account_group_roles_account_group_roles_inner_instance = AccountGroupRolesAccountGroupRolesInner.from_json(json)
# print the JSON string representation of the object
print(AccountGroupRolesAccountGroupRolesInner.to_json())

# convert the object into a dict
account_group_roles_account_group_roles_inner_dict = account_group_roles_account_group_roles_inner_instance.to_dict()
# create an instance of AccountGroupRolesAccountGroupRolesInner from a dict
account_group_roles_account_group_roles_inner_from_dict = AccountGroupRolesAccountGroupRolesInner.from_dict(account_group_roles_account_group_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


