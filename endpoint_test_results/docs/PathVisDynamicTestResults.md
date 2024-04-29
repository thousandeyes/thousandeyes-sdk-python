# PathVisDynamicTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDynamicTestResult]**](PathVisDynamicTestResult.md) |  | [optional] 
**test** | [**DynamicTest**](DynamicTest.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.path_vis_dynamic_test_results import PathVisDynamicTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDynamicTestResults from a JSON string
path_vis_dynamic_test_results_instance = PathVisDynamicTestResults.from_json(json)
# print the JSON string representation of the object
print(PathVisDynamicTestResults.to_json())

# convert the object into a dict
path_vis_dynamic_test_results_dict = path_vis_dynamic_test_results_instance.to_dict()
# create an instance of PathVisDynamicTestResults from a dict
path_vis_dynamic_test_results_from_dict = PathVisDynamicTestResults.from_dict(path_vis_dynamic_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


