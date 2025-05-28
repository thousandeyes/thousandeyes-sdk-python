# TestVersionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_timestamp** | **datetime** | Timestamp when this version was created. | [optional] 
**test_id** | **str** | The unique identifier of the test. | [optional] 
**created_by** | **str** | The user who created the version. | [optional] 
**version_id** | **str** | The unique identifier for a specific version of the test settings. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_version_history import TestVersionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TestVersionHistory from a JSON string
test_version_history_instance = TestVersionHistory.from_json(json)
# print the JSON string representation of the object
print(TestVersionHistory.to_json())

# convert the object into a dict
test_version_history_dict = test_version_history_instance.to_dict()
# create an instance of TestVersionHistory from a dict
test_version_history_from_dict = TestVersionHistory.from_dict(test_version_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


