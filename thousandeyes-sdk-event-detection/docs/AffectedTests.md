# AffectedTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number affected. | [optional] [readonly] 
**in_account_group** | **int** | Indicates if in the affected account group. | [optional] [readonly] 
**tests** | [**List[EventApiAffectedTest]**](EventApiAffectedTest.md) | List of affected tests. | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.affected_tests import AffectedTests

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedTests from a JSON string
affected_tests_instance = AffectedTests.from_json(json)
# print the JSON string representation of the object
print(AffectedTests.to_json())

# convert the object into a dict
affected_tests_dict = affected_tests_instance.to_dict()
# create an instance of AffectedTests from a dict
affected_tests_from_dict = AffectedTests.from_dict(affected_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


