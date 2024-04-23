# TestSharedAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Account group ID. | [optional] 
**name** | **str** | Account group name. | [optional] 

## Example

```python
from instant_tests.models.test_shared_accounts_inner import TestSharedAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TestSharedAccountsInner from a JSON string
test_shared_accounts_inner_instance = TestSharedAccountsInner.from_json(json)
# print the JSON string representation of the object
print(TestSharedAccountsInner.to_json())

# convert the object into a dict
test_shared_accounts_inner_dict = test_shared_accounts_inner_instance.to_dict()
# create an instance of TestSharedAccountsInner from a dict
test_shared_accounts_inner_from_dict = TestSharedAccountsInner.from_dict(test_shared_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


