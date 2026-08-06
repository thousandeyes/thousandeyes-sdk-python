# ConsoleLogsTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ConsoleLogsResult]**](ConsoleLogsResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.console_logs_test_results import ConsoleLogsTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleLogsTestResults from a JSON string
console_logs_test_results_instance = ConsoleLogsTestResults.from_json(json)
# print the JSON string representation of the object
print(ConsoleLogsTestResults.to_json())

# convert the object into a dict
console_logs_test_results_dict = console_logs_test_results_instance.to_dict()
# create an instance of ConsoleLogsTestResults from a dict
console_logs_test_results_from_dict = ConsoleLogsTestResults.from_dict(console_logs_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


