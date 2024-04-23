# AccountGroupRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group_roles** | [**List[AccountGroupRolesAccountGroupRolesInner]**](AccountGroupRolesAccountGroupRolesInner.md) |  | [optional] 

## Example

```python
from admin.models.account_group_roles import AccountGroupRoles

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupRoles from a JSON string
account_group_roles_instance = AccountGroupRoles.from_json(json)
# print the JSON string representation of the object
print(AccountGroupRoles.to_json())

# convert the object into a dict
account_group_roles_dict = account_group_roles_instance.to_dict()
# create an instance of AccountGroupRoles from a dict
account_group_roles_from_dict = AccountGroupRoles.from_dict(account_group_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


