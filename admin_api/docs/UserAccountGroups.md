# UserAccountGroups


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserAccountGroup]**](UserAccountGroup.md) |  | [optional] 

## Example

```python
from admin_api.models.user_account_groups import UserAccountGroups

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountGroups from a JSON string
user_account_groups_instance = UserAccountGroups.from_json(json)
# print the JSON string representation of the object
print UserAccountGroups.to_json()

# convert the object into a dict
user_account_groups_dict = user_account_groups_instance.to_dict()
# create an instance of UserAccountGroups from a dict
user_account_groups_form_dict = user_account_groups.from_dict(user_account_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


