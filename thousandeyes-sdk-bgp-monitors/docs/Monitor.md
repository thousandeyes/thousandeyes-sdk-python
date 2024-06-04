# Monitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_id** | **str** | Country ID | [optional] [readonly] 
**monitor_id** | **str** | BGP monitor ID | [optional] [readonly] 
**ip_address** | **str** | IP address of the BGP monitor | [optional] 
**network** | **str** | Name of the autonomous system in which the monitor is found | [optional] 
**monitor_type** | [**MonitorType**](MonitorType.md) |  | [optional] 
**monitor_name** | **str** | Display name of the BGP monitor | [optional] 

## Example

```python
from thousandeyes_sdk.bgp_monitors.models.monitor import Monitor

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


