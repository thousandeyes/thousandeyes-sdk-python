# Monitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | **str** | Unique monitor ID. | [optional] [readonly] 
**monitor_name** | **str** | The name of the Monitor. | [optional] [readonly] 
**country_id** | **str** | 2-digit ISO country code. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.monitor import Monitor

# TODO update the JSON string below
json = "{}"
# create an instance of Monitor from a JSON string
monitor_instance = Monitor.from_json(json)
# print the JSON string representation of the object
print(Monitor.to_json())

# convert the object into a dict
monitor_dict = monitor_instance.to_dict()
# create an instance of Monitor from a dict
monitor_from_dict = Monitor.from_dict(monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


