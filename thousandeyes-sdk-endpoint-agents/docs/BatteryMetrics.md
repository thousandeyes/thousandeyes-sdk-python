# BatteryMetrics

Battery metrics for the endpoint agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_level** | [**BatteryLevel**](BatteryLevel.md) |  | 
**battery_level_normalized_percent** | **float** | Battery level as a normalized percentage (0-1). | 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.battery_metrics import BatteryMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of BatteryMetrics from a JSON string
battery_metrics_instance = BatteryMetrics.from_json(json)
# print the JSON string representation of the object
print(BatteryMetrics.to_json())

# convert the object into a dict
battery_metrics_dict = battery_metrics_instance.to_dict()
# create an instance of BatteryMetrics from a dict
battery_metrics_from_dict = BatteryMetrics.from_dict(battery_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


