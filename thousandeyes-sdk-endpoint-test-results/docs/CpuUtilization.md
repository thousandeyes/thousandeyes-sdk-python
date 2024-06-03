# CpuUtilization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** | The minimum sampled usage value recorded during the monitored period. | [optional] [readonly] 
**max** | **float** | The maximum sampled usage value recorded during the monitored period. | [optional] [readonly] 
**mean** | **float** | The mean (average) sampled usage value recorded during the monitored period. | [optional] [readonly] 
**median** | **float** | The median sampled usage value recorded during the monitored period. | [optional] [readonly] 
**std_dev** | **float** | The standard deviation of sampled usage values recorded during the monitored period. | [optional] [readonly] 
**count** | **int** | The total number of samples collected during the monitored period. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.cpu_utilization import CpuUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of CpuUtilization from a JSON string
cpu_utilization_instance = CpuUtilization.from_json(json)
# print the JSON string representation of the object
print(CpuUtilization.to_json())

# convert the object into a dict
cpu_utilization_dict = cpu_utilization_instance.to_dict()
# create an instance of CpuUtilization from a dict
cpu_utilization_from_dict = CpuUtilization.from_dict(cpu_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


