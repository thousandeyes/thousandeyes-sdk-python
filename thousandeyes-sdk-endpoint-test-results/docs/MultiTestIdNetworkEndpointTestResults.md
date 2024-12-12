# MultiTestIdNetworkEndpointTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkEndpointTestResult]**](NetworkEndpointTestResult.md) |  | [optional] 
**total_hits** | **int** | Total number of measurements that match the search criteria. | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationNextLink**](PaginationNextLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_network_endpoint_test_results import MultiTestIdNetworkEndpointTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTestIdNetworkEndpointTestResults from a JSON string
multi_test_id_network_endpoint_test_results_instance = MultiTestIdNetworkEndpointTestResults.from_json(json)
# print the JSON string representation of the object
print(MultiTestIdNetworkEndpointTestResults.to_json())

# convert the object into a dict
multi_test_id_network_endpoint_test_results_dict = multi_test_id_network_endpoint_test_results_instance.to_dict()
# create an instance of MultiTestIdNetworkEndpointTestResults from a dict
multi_test_id_network_endpoint_test_results_from_dict = MultiTestIdNetworkEndpointTestResults.from_dict(multi_test_id_network_endpoint_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


