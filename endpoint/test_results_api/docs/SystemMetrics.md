# SystemMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time_ms** | **float** | The start time of metrics collection, expressed in milliseconds since the Epoch. | [optional] [readonly] 
**end_time_ms** | **float** | The end time of metrics collection, expressed in milliseconds since the Epoch. | [optional] [readonly] 
**cpu_utilization** | [**CpuUtilization**](CpuUtilization.md) |  | [optional] 
**physical_memory_used_bytes** | [**PhysicalMemoryUsedBytes**](PhysicalMemoryUsedBytes.md) |  | [optional] 
**physical_memory_total_bytes** | **float** | Total physical memory of the system. | [optional] [readonly] 

## Example

```python
from test_results_api.models.system_metrics import SystemMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMetrics from a JSON string
system_metrics_instance = SystemMetrics.from_json(json)
# print the JSON string representation of the object
print SystemMetrics.to_json()

# convert the object into a dict
system_metrics_dict = system_metrics_instance.to_dict()
# create an instance of SystemMetrics from a dict
system_metrics_form_dict = system_metrics.from_dict(system_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


