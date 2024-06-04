# PhysicalMemoryUsedBytes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** | The minimum sampled memory usage value recorded during the monitored period. | [optional] [readonly] 
**max** | **float** | The maximum sampled memory usage value recorded during the monitored period. | [optional] [readonly] 
**mean** | **float** | The mean (average) value of memory usage sampled over the monitored period. | [optional] [readonly] 
**median** | **float** | The median value of memory usage sampled over the monitored period. | [optional] [readonly] 
**std_dev** | **float** | The standard deviation of memory usage sampled during the monitored period. | [optional] [readonly] 
**count** | **int** | The total number of samples collected during the monitored period. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.physical_memory_used_bytes import PhysicalMemoryUsedBytes

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalMemoryUsedBytes from a JSON string
physical_memory_used_bytes_instance = PhysicalMemoryUsedBytes.from_json(json)
# print the JSON string representation of the object
print(PhysicalMemoryUsedBytes.to_json())

# convert the object into a dict
physical_memory_used_bytes_dict = physical_memory_used_bytes_instance.to_dict()
# create an instance of PhysicalMemoryUsedBytes from a dict
physical_memory_used_bytes_from_dict = PhysicalMemoryUsedBytes.from_dict(physical_memory_used_bytes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


