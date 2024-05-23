# MultiTestIdTestsDataRoundsSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_sort** | [**List[TestsDataSearchSort]**](TestsDataSearchSort.md) |  | [optional] 
**threshold_filter** | [**TestsDataThresholdFilters**](TestsDataThresholdFilters.md) |  | [optional] 
**search_filters** | [**MultiTestIdTestsDataSearchFilter**](MultiTestIdTestsDataSearchFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_tests_data_rounds_search import MultiTestIdTestsDataRoundsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTestIdTestsDataRoundsSearch from a JSON string
multi_test_id_tests_data_rounds_search_instance = MultiTestIdTestsDataRoundsSearch.from_json(json)
# print the JSON string representation of the object
print(MultiTestIdTestsDataRoundsSearch.to_json())

# convert the object into a dict
multi_test_id_tests_data_rounds_search_dict = multi_test_id_tests_data_rounds_search_instance.to_dict()
# create an instance of MultiTestIdTestsDataRoundsSearch from a dict
multi_test_id_tests_data_rounds_search_from_dict = MultiTestIdTestsDataRoundsSearch.from_dict(multi_test_id_tests_data_rounds_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


