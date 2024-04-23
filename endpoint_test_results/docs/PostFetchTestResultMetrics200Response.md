# PostFetchTestResultMetrics200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkTestResult]**](NetworkTestResult.md) |  | [optional] 
**total_hits** | **float** | Total number of measurements that match the search criteria | [optional] 
**test** | [**EndpointScheduledTest**](EndpointScheduledTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationNextLinkLinks**](PaginationNextLinkLinks.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.post_fetch_test_result_metrics200_response import PostFetchTestResultMetrics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostFetchTestResultMetrics200Response from a JSON string
post_fetch_test_result_metrics200_response_instance = PostFetchTestResultMetrics200Response.from_json(json)
# print the JSON string representation of the object
print(PostFetchTestResultMetrics200Response.to_json())

# convert the object into a dict
post_fetch_test_result_metrics200_response_dict = post_fetch_test_result_metrics200_response_instance.to_dict()
# create an instance of PostFetchTestResultMetrics200Response from a dict
post_fetch_test_result_metrics200_response_from_dict = PostFetchTestResultMetrics200Response.from_dict(post_fetch_test_result_metrics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


