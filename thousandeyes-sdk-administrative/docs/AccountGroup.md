# AccountGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**account_group_name** | **str** | Account group name | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.account_group import AccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroup from a JSON string
account_group_instance = AccountGroup.from_json(json)
# print the JSON string representation of the object
print(AccountGroup.to_json())

# convert the object into a dict
account_group_dict = account_group_instance.to_dict()
# create an instance of AccountGroup from a dict
account_group_from_dict = AccountGroup.from_dict(account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


