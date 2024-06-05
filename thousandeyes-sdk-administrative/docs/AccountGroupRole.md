# AccountGroupRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group** | [**AccountGroup**](AccountGroup.md) |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.account_group_role import AccountGroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupRole from a JSON string
account_group_role_instance = AccountGroupRole.from_json(json)
# print the JSON string representation of the object
print(AccountGroupRole.to_json())

# convert the object into a dict
account_group_role_dict = account_group_role_instance.to_dict()
# create an instance of AccountGroupRole from a dict
account_group_role_from_dict = AccountGroupRole.from_dict(account_group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


