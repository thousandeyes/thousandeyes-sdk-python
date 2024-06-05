# UserAccountGroupRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group_id** | **str** | Unique ID of the account group. | [optional] 
**role_ids** | **List[str]** | Unique role IDs. | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.user_account_group_role import UserAccountGroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountGroupRole from a JSON string
user_account_group_role_instance = UserAccountGroupRole.from_json(json)
# print the JSON string representation of the object
print(UserAccountGroupRole.to_json())

# convert the object into a dict
user_account_group_role_dict = user_account_group_role_instance.to_dict()
# create an instance of UserAccountGroupRole from a dict
user_account_group_role_from_dict = UserAccountGroupRole.from_dict(user_account_group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


