# ConsoleLogsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**console_logs** | [**List[ConsoleLogs]**](ConsoleLogs.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.console_logs_result import ConsoleLogsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleLogsResult from a JSON string
console_logs_result_instance = ConsoleLogsResult.from_json(json)
# print the JSON string representation of the object
print(ConsoleLogsResult.to_json())

# convert the object into a dict
console_logs_result_dict = console_logs_result_instance.to_dict()
# create an instance of ConsoleLogsResult from a dict
console_logs_result_from_dict = ConsoleLogsResult.from_dict(console_logs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


