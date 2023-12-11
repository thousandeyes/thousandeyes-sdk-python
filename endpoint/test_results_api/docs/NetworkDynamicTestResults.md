# NetworkDynamicTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkDynamicTestResult]**](NetworkDynamicTestResult.md) |  | [optional] 
**test** | [**DynamicTest**](DynamicTest.md) |  | [optional] 

## Example

```python
from test_results_api.models.network_dynamic_test_results import NetworkDynamicTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDynamicTestResults from a JSON string
network_dynamic_test_results_instance = NetworkDynamicTestResults.from_json(json)
# print the JSON string representation of the object
print NetworkDynamicTestResults.to_json()

# convert the object into a dict
network_dynamic_test_results_dict = network_dynamic_test_results_instance.to_dict()
# create an instance of NetworkDynamicTestResults from a dict
network_dynamic_test_results_form_dict = network_dynamic_test_results.from_dict(network_dynamic_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


