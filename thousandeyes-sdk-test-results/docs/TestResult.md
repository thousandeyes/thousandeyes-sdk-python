# TestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.test_result import TestResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResult from a JSON string
test_result_instance = TestResult.from_json(json)
# print the JSON string representation of the object
print(TestResult.to_json())

# convert the object into a dict
test_result_dict = test_result_instance.to_dict()
# create an instance of TestResult from a dict
test_result_from_dict = TestResult.from_dict(test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


