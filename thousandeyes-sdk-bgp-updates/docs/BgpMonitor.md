# BgpMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_id** | **str** | Country ID | [optional] [readonly] 
**monitor_id** | **str** | BGP monitor ID | [optional] [readonly] 
**ip_address** | **str** | IP address of the BGP monitor | [optional] 
**network** | **str** | Name of the autonomous system in which the monitor is found | [optional] 
**monitor_type** | [**MonitorType**](MonitorType.md) |  | [optional] 
**monitor_name** | **str** | Display name of the BGP monitor | [optional] 
**asn** | **int** | Autonomous system number in which the monitor is found. | [optional] 

## Example

```python
from thousandeyes_sdk.bgp_updates.models.bgp_monitor import BgpMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of BgpMonitor from a JSON string
bgp_monitor_instance = BgpMonitor.from_json(json)
# print the JSON string representation of the object
print(BgpMonitor.to_json())

# convert the object into a dict
bgp_monitor_dict = bgp_monitor_instance.to_dict()
# create an instance of BgpMonitor from a dict
bgp_monitor_from_dict = BgpMonitor.from_dict(bgp_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


