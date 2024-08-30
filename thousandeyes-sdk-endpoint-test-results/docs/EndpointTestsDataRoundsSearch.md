# EndpointTestsDataRoundsSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[EndpointTestsDataSearchSort]**](EndpointTestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**EndpointTestsDataThresholdFilters**](EndpointTestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**EndpointTestsDataSearchFilter**](EndpointTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_rounds_search import EndpointTestsDataRoundsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestsDataRoundsSearch from a JSON string
endpoint_tests_data_rounds_search_instance = EndpointTestsDataRoundsSearch.from_json(json)
# print the JSON string representation of the object
print(EndpointTestsDataRoundsSearch.to_json())

# convert the object into a dict
endpoint_tests_data_rounds_search_dict = endpoint_tests_data_rounds_search_instance.to_dict()
# create an instance of EndpointTestsDataRoundsSearch from a dict
endpoint_tests_data_rounds_search_from_dict = EndpointTestsDataRoundsSearch.from_dict(endpoint_tests_data_rounds_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


