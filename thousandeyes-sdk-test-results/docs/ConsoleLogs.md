# ConsoleLogs

Console logs captured during script execution to help troubleshoot transaction issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Severity level of the log, or UNKNOWN if the log is system-generated. | [optional] 
**timestamp** | **str** | Unix epoch time, in milliseconds, when the log entry was captured. | [optional] 
**value** | **str** | Log message. | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.console_logs import ConsoleLogs

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleLogs from a JSON string
console_logs_instance = ConsoleLogs.from_json(json)
# print the JSON string representation of the object
print(ConsoleLogs.to_json())

# convert the object into a dict
console_logs_dict = console_logs_instance.to_dict()
# create an instance of ConsoleLogs from a dict
console_logs_from_dict = ConsoleLogs.from_dict(console_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


