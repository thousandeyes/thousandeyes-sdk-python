# PathVisDetailTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDetailTestResult]**](PathVisDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.path_vis_detail_test_results import PathVisDetailTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDetailTestResults from a JSON string
path_vis_detail_test_results_instance = PathVisDetailTestResults.from_json(json)
# print the JSON string representation of the object
print(PathVisDetailTestResults.to_json())

# convert the object into a dict
path_vis_detail_test_results_dict = path_vis_detail_test_results_instance.to_dict()
# create an instance of PathVisDetailTestResults from a dict
path_vis_detail_test_results_from_dict = PathVisDetailTestResults.from_dict(path_vis_detail_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


