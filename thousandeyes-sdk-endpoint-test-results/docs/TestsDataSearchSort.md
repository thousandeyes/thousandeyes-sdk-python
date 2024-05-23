# TestsDataSearchSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**TestsDataSearchSortKey**](TestsDataSearchSortKey.md) |  | [optional] 
**order** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_sort import TestsDataSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of TestsDataSearchSort from a JSON string
tests_data_search_sort_instance = TestsDataSearchSort.from_json(json)
# print the JSON string representation of the object
print(TestsDataSearchSort.to_json())

# convert the object into a dict
tests_data_search_sort_dict = tests_data_search_sort_instance.to_dict()
# create an instance of TestsDataSearchSort from a dict
tests_data_search_sort_from_dict = TestsDataSearchSort.from_dict(tests_data_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


