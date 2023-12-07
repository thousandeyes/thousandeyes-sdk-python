# LoginAccountGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_account_group** | [**AccountGroup1**](AccountGroup1.md) |  | [optional] 

## Example

```python
from admin_api.models.login_account_group import LoginAccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LoginAccountGroup from a JSON string
login_account_group_instance = LoginAccountGroup.from_json(json)
# print the JSON string representation of the object
print LoginAccountGroup.to_json()

# convert the object into a dict
login_account_group_dict = login_account_group_instance.to_dict()
# create an instance of LoginAccountGroup from a dict
login_account_group_form_dict = login_account_group.from_dict(login_account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


