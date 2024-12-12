# NetworkEndpointTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkEndpointTestResult]**](NetworkEndpointTestResult.md) |  | [optional] 
**total_hits** | **int** | Total number of measurements that match the search criteria. | [optional] 
**test** | [**EndpointScheduledTest**](EndpointScheduledTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationNextLink**](PaginationNextLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_endpoint_test_results import NetworkEndpointTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkEndpointTestResults from a JSON string
network_endpoint_test_results_instance = NetworkEndpointTestResults.from_json(json)
# print the JSON string representation of the object
print(NetworkEndpointTestResults.to_json())

# convert the object into a dict
network_endpoint_test_results_dict = network_endpoint_test_results_instance.to_dict()
# create an instance of NetworkEndpointTestResults from a dict
network_endpoint_test_results_from_dict = NetworkEndpointTestResults.from_dict(network_endpoint_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


