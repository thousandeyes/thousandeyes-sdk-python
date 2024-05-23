# TestsDataRoundsSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[TestsDataSearchSort]**](TestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**TestsDataThresholdFilters**](TestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**TestsDataSearchFilter**](TestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.tests_data_rounds_search import TestsDataRoundsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of TestsDataRoundsSearch from a JSON string
tests_data_rounds_search_instance = TestsDataRoundsSearch.from_json(json)
# print the JSON string representation of the object
print(TestsDataRoundsSearch.to_json())

# convert the object into a dict
tests_data_rounds_search_dict = tests_data_rounds_search_instance.to_dict()
# create an instance of TestsDataRoundsSearch from a dict
tests_data_rounds_search_from_dict = TestsDataRoundsSearch.from_dict(tests_data_rounds_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


