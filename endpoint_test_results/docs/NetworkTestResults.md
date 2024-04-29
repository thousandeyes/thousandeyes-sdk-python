# NetworkTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkTestResult]**](NetworkTestResult.md) |  | [optional] 
**total_hits** | **float** | Total number of measurements that match the search criteria | [optional] 
**test** | [**EndpointScheduledTest**](EndpointScheduledTest.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.network_test_results import NetworkTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkTestResults from a JSON string
network_test_results_instance = NetworkTestResults.from_json(json)
# print the JSON string representation of the object
print(NetworkTestResults.to_json())

# convert the object into a dict
network_test_results_dict = network_test_results_instance.to_dict()
# create an instance of NetworkTestResults from a dict
network_test_results_from_dict = NetworkTestResults.from_dict(network_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


