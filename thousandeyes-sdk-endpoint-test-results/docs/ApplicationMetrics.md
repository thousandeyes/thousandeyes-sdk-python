# ApplicationMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the application. | [optional] 
**total_cpu** | **float** | The total CPU usage by all application processes. | [optional] 
**total_memory_percentage** | **float** | The total percentage of memory used by all application processes. | [optional] 
**total_memory_bytes** | **int** | The total memory in bytes used by all application processes. | [optional] 
**processes** | [**List[ProcessMetrics]**](ProcessMetrics.md) | A list of application processes. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.application_metrics import ApplicationMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetrics from a JSON string
application_metrics_instance = ApplicationMetrics.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetrics.to_json())

# convert the object into a dict
application_metrics_dict = application_metrics_instance.to_dict()
# create an instance of ApplicationMetrics from a dict
application_metrics_from_dict = ApplicationMetrics.from_dict(application_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


