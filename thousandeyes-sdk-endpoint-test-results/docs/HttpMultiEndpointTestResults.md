# HttpMultiEndpointTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HttpEndpointTestResult]**](HttpEndpointTestResult.md) |  | [optional] 
**total_hits** | **int** | Total number of measurements that match the search criteria. | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationNextAndSelfLink**](PaginationNextAndSelfLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_multi_endpoint_test_results import HttpMultiEndpointTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of HttpMultiEndpointTestResults from a JSON string
http_multi_endpoint_test_results_instance = HttpMultiEndpointTestResults.from_json(json)
# print the JSON string representation of the object
print(HttpMultiEndpointTestResults.to_json())

# convert the object into a dict
http_multi_endpoint_test_results_dict = http_multi_endpoint_test_results_instance.to_dict()
# create an instance of HttpMultiEndpointTestResults from a dict
http_multi_endpoint_test_results_from_dict = HttpMultiEndpointTestResults.from_dict(http_multi_endpoint_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


