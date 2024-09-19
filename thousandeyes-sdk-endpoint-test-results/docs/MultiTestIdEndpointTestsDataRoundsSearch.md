# MultiTestIdEndpointTestsDataRoundsSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[EndpointTestsDataSearchSort]**](EndpointTestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**EndpointTestsDataThresholdFilters**](EndpointTestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**MultiTestIdEndpointTestsDataSearchFilter**](MultiTestIdEndpointTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_endpoint_tests_data_rounds_search import MultiTestIdEndpointTestsDataRoundsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTestIdEndpointTestsDataRoundsSearch from a JSON string
multi_test_id_endpoint_tests_data_rounds_search_instance = MultiTestIdEndpointTestsDataRoundsSearch.from_json(json)
# print the JSON string representation of the object
print(MultiTestIdEndpointTestsDataRoundsSearch.to_json())

# convert the object into a dict
multi_test_id_endpoint_tests_data_rounds_search_dict = multi_test_id_endpoint_tests_data_rounds_search_instance.to_dict()
# create an instance of MultiTestIdEndpointTestsDataRoundsSearch from a dict
multi_test_id_endpoint_tests_data_rounds_search_from_dict = MultiTestIdEndpointTestsDataRoundsSearch.from_dict(multi_test_id_endpoint_tests_data_rounds_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


