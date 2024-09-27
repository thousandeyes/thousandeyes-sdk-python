# DynamicEndpointTestsDataRoundSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[EndpointTestsDataSearchSort]**](EndpointTestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**EndpointTestsDataThresholdFilters**](EndpointTestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**DynamicEndpointTestsDataSearchFilter**](DynamicEndpointTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.dynamic_endpoint_tests_data_round_search import DynamicEndpointTestsDataRoundSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicEndpointTestsDataRoundSearch from a JSON string
dynamic_endpoint_tests_data_round_search_instance = DynamicEndpointTestsDataRoundSearch.from_json(json)
# print the JSON string representation of the object
print(DynamicEndpointTestsDataRoundSearch.to_json())

# convert the object into a dict
dynamic_endpoint_tests_data_round_search_dict = dynamic_endpoint_tests_data_round_search_instance.to_dict()
# create an instance of DynamicEndpointTestsDataRoundSearch from a dict
dynamic_endpoint_tests_data_round_search_from_dict = DynamicEndpointTestsDataRoundSearch.from_dict(dynamic_endpoint_tests_data_round_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


