# ProcessMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the process. | [optional] 
**pid** | **int** | The process ID. | [optional] 
**cpu** | **float** | The CPU usage by the process as a percentage (e.g., 0.5 for 50% CPU usage). | [optional] 
**memory_percentage** | **float** | The memory usage by the process as a percentage (e.g., 0.22 for 22%). | [optional] 
**memory_bytes** | **int** | The memory usage by the process in bytes. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.process_metrics import ProcessMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessMetrics from a JSON string
process_metrics_instance = ProcessMetrics.from_json(json)
# print the JSON string representation of the object
print(ProcessMetrics.to_json())

# convert the object into a dict
process_metrics_dict = process_metrics_instance.to_dict()
# create an instance of ProcessMetrics from a dict
process_metrics_from_dict = ProcessMetrics.from_dict(process_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


