# AccountGroup1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**account_group_name** | **str** | Account group name | [optional] 

## Example

```python
from admin_api.models.account_group1 import AccountGroup1

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroup1 from a JSON string
account_group1_instance = AccountGroup1.from_json(json)
# print the JSON string representation of the object
print AccountGroup1.to_json()

# convert the object into a dict
account_group1_dict = account_group1_instance.to_dict()
# create an instance of AccountGroup1 from a dict
account_group1_form_dict = account_group1.from_dict(account_group1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


