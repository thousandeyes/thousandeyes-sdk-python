# PathVisTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisTestResult]**](PathVisTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.path_vis_test_results import PathVisTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisTestResults from a JSON string
path_vis_test_results_instance = PathVisTestResults.from_json(json)
# print the JSON string representation of the object
print(PathVisTestResults.to_json())

# convert the object into a dict
path_vis_test_results_dict = path_vis_test_results_instance.to_dict()
# create an instance of PathVisTestResults from a dict
path_vis_test_results_from_dict = PathVisTestResults.from_dict(path_vis_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


