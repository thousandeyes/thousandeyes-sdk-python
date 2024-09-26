# TestResultMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | **str** | Unique monitor ID. | [optional] [readonly] 
**monitor_name** | **str** | The name of the Monitor. | [optional] [readonly] 
**country_id** | **str** | 2-digit ISO country code. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.test_result_monitor import TestResultMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultMonitor from a JSON string
test_result_monitor_instance = TestResultMonitor.from_json(json)
# print the JSON string representation of the object
print(TestResultMonitor.to_json())

# convert the object into a dict
test_result_monitor_dict = test_result_monitor_instance.to_dict()
# create an instance of TestResultMonitor from a dict
test_result_monitor_from_dict = TestResultMonitor.from_dict(test_result_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


