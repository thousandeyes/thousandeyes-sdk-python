# RealUserEndpointTestNetworkResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RealUserEndpointTestNetworkResult]**](RealUserEndpointTestNetworkResult.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationNextLink**](PaginationNextLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_network_results import RealUserEndpointTestNetworkResults

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestNetworkResults from a JSON string
real_user_endpoint_test_network_results_instance = RealUserEndpointTestNetworkResults.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestNetworkResults.to_json())

# convert the object into a dict
real_user_endpoint_test_network_results_dict = real_user_endpoint_test_network_results_instance.to_dict()
# create an instance of RealUserEndpointTestNetworkResults from a dict
real_user_endpoint_test_network_results_from_dict = RealUserEndpointTestNetworkResults.from_dict(real_user_endpoint_test_network_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


