# HttpTestsDataRoundsSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[HttpTestsDataSearchSort]**](HttpTestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**HttpTestsDataThresholdFilters**](HttpTestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**HttpTestsDataSearchFilter**](HttpTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_tests_data_rounds_search import HttpTestsDataRoundsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTestsDataRoundsSearch from a JSON string
http_tests_data_rounds_search_instance = HttpTestsDataRoundsSearch.from_json(json)
# print the JSON string representation of the object
print(HttpTestsDataRoundsSearch.to_json())

# convert the object into a dict
http_tests_data_rounds_search_dict = http_tests_data_rounds_search_instance.to_dict()
# create an instance of HttpTestsDataRoundsSearch from a dict
http_tests_data_rounds_search_from_dict = HttpTestsDataRoundsSearch.from_dict(http_tests_data_rounds_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


