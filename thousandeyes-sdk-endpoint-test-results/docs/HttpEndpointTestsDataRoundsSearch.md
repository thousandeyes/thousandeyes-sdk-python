# HttpEndpointTestsDataRoundsSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[HttpEndpointTestsDataSearchSort]**](HttpEndpointTestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**HttpEndpointTestsDataThresholdFilters**](HttpEndpointTestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**HttpEndpointTestsDataSearchFilter**](HttpEndpointTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_rounds_search import HttpEndpointTestsDataRoundsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of HttpEndpointTestsDataRoundsSearch from a JSON string
http_endpoint_tests_data_rounds_search_instance = HttpEndpointTestsDataRoundsSearch.from_json(json)
# print the JSON string representation of the object
print(HttpEndpointTestsDataRoundsSearch.to_json())

# convert the object into a dict
http_endpoint_tests_data_rounds_search_dict = http_endpoint_tests_data_rounds_search_instance.to_dict()
# create an instance of HttpEndpointTestsDataRoundsSearch from a dict
http_endpoint_tests_data_rounds_search_from_dict = HttpEndpointTestsDataRoundsSearch.from_dict(http_endpoint_tests_data_rounds_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


