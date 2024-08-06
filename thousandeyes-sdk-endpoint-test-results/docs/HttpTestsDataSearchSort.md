# HttpTestsDataSearchSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**HttpTestsDataSearchSortKey**](HttpTestsDataSearchSortKey.md) |  | [optional] 
**order** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_tests_data_search_sort import HttpTestsDataSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTestsDataSearchSort from a JSON string
http_tests_data_search_sort_instance = HttpTestsDataSearchSort.from_json(json)
# print the JSON string representation of the object
print(HttpTestsDataSearchSort.to_json())

# convert the object into a dict
http_tests_data_search_sort_dict = http_tests_data_search_sort_instance.to_dict()
# create an instance of HttpTestsDataSearchSort from a dict
http_tests_data_search_sort_from_dict = HttpTestsDataSearchSort.from_dict(http_tests_data_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


