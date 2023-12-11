# PathVisTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisTestResult]**](PathVisTestResult.md) |  | [optional] 
**test** | [**EndpointScheduledTest**](EndpointScheduledTest.md) |  | [optional] 

## Example

```python
from test_results_api.models.path_vis_test_results import PathVisTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisTestResults from a JSON string
path_vis_test_results_instance = PathVisTestResults.from_json(json)
# print the JSON string representation of the object
print PathVisTestResults.to_json()

# convert the object into a dict
path_vis_test_results_dict = path_vis_test_results_instance.to_dict()
# create an instance of PathVisTestResults from a dict
path_vis_test_results_form_dict = path_vis_test_results.from_dict(path_vis_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


