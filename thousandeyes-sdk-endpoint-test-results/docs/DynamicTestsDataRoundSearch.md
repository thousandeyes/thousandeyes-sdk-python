# DynamicTestsDataRoundSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[TestsDataSearchSort]**](TestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**TestsDataThresholdFilters**](TestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**DynamicTestsDataSearchFilter**](DynamicTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.dynamic_tests_data_round_search import DynamicTestsDataRoundSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTestsDataRoundSearch from a JSON string
dynamic_tests_data_round_search_instance = DynamicTestsDataRoundSearch.from_json(json)
# print the JSON string representation of the object
print(DynamicTestsDataRoundSearch.to_json())

# convert the object into a dict
dynamic_tests_data_round_search_dict = dynamic_tests_data_round_search_instance.to_dict()
# create an instance of DynamicTestsDataRoundSearch from a dict
dynamic_tests_data_round_search_from_dict = DynamicTestsDataRoundSearch.from_dict(dynamic_tests_data_round_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


