# EndpointTestsDataSearchSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**EndpointTestsDataSearchSortKey**](EndpointTestsDataSearchSortKey.md) |  | [optional] 
**order** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_search_sort import EndpointTestsDataSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestsDataSearchSort from a JSON string
endpoint_tests_data_search_sort_instance = EndpointTestsDataSearchSort.from_json(json)
# print the JSON string representation of the object
print(EndpointTestsDataSearchSort.to_json())

# convert the object into a dict
endpoint_tests_data_search_sort_dict = endpoint_tests_data_search_sort_instance.to_dict()
# create an instance of EndpointTestsDataSearchSort from a dict
endpoint_tests_data_search_sort_from_dict = EndpointTestsDataSearchSort.from_dict(endpoint_tests_data_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


