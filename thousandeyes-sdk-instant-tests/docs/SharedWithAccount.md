# SharedWithAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Account group ID. | [optional] 
**name** | **str** | Account group name. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.shared_with_account import SharedWithAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SharedWithAccount from a JSON string
shared_with_account_instance = SharedWithAccount.from_json(json)
# print the JSON string representation of the object
print(SharedWithAccount.to_json())

# convert the object into a dict
shared_with_account_dict = shared_with_account_instance.to_dict()
# create an instance of SharedWithAccount from a dict
shared_with_account_from_dict = SharedWithAccount.from_dict(shared_with_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


