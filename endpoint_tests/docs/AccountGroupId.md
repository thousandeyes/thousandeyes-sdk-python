# AccountGroupId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 

## Example

```python
from endpoint_tests.models.account_group_id import AccountGroupId

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupId from a JSON string
account_group_id_instance = AccountGroupId.from_json(json)
# print the JSON string representation of the object
print(AccountGroupId.to_json())

# convert the object into a dict
account_group_id_dict = account_group_id_instance.to_dict()
# create an instance of AccountGroupId from a dict
account_group_id_from_dict = AccountGroupId.from_dict(account_group_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


