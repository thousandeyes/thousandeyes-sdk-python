# TestVersionHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 
**test_version_history** | [**List[TestVersionHistory]**](TestVersionHistory.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_version_history_response import TestVersionHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestVersionHistoryResponse from a JSON string
test_version_history_response_instance = TestVersionHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(TestVersionHistoryResponse.to_json())

# convert the object into a dict
test_version_history_response_dict = test_version_history_response_instance.to_dict()
# create an instance of TestVersionHistoryResponse from a dict
test_version_history_response_from_dict = TestVersionHistoryResponse.from_dict(test_version_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


