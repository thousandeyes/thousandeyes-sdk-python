# SystemMetricDetails

Details of system metrics that contain top applications by CPU/memory usage. Not populated by default. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_cpu_applications** | [**List[ApplicationMetrics]**](ApplicationMetrics.md) | A list of applications that consume more than 2% of the CPU. | [optional] [readonly] 
**top_memory_applications** | [**List[ApplicationMetrics]**](ApplicationMetrics.md) | A list of applications that consume more than 2% of the RAM. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.system_metric_details import SystemMetricDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMetricDetails from a JSON string
system_metric_details_instance = SystemMetricDetails.from_json(json)
# print the JSON string representation of the object
print(SystemMetricDetails.to_json())

# convert the object into a dict
system_metric_details_dict = system_metric_details_instance.to_dict()
# create an instance of SystemMetricDetails from a dict
system_metric_details_from_dict = SystemMetricDetails.from_dict(system_metric_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


