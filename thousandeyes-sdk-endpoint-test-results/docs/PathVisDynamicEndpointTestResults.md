# PathVisDynamicEndpointTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDynamicEndpointTestResult]**](PathVisDynamicEndpointTestResult.md) |  | [optional] 
**test** | [**DynamicTest**](DynamicTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**total_hits** | **int** | Total number of measurements that match the search criteria. | [optional] 
**links** | [**PaginationNextAndSelfLink**](PaginationNextAndSelfLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.path_vis_dynamic_endpoint_test_results import PathVisDynamicEndpointTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDynamicEndpointTestResults from a JSON string
path_vis_dynamic_endpoint_test_results_instance = PathVisDynamicEndpointTestResults.from_json(json)
# print the JSON string representation of the object
print(PathVisDynamicEndpointTestResults.to_json())

# convert the object into a dict
path_vis_dynamic_endpoint_test_results_dict = path_vis_dynamic_endpoint_test_results_instance.to_dict()
# create an instance of PathVisDynamicEndpointTestResults from a dict
path_vis_dynamic_endpoint_test_results_from_dict = PathVisDynamicEndpointTestResults.from_dict(path_vis_dynamic_endpoint_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


