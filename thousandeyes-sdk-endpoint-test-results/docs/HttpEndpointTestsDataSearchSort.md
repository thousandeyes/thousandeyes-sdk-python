# HttpEndpointTestsDataSearchSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**HttpEndpointTestsDataSearchSortKey**](HttpEndpointTestsDataSearchSortKey.md) |  | [optional] 
**order** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_search_sort import HttpEndpointTestsDataSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of HttpEndpointTestsDataSearchSort from a JSON string
http_endpoint_tests_data_search_sort_instance = HttpEndpointTestsDataSearchSort.from_json(json)
# print the JSON string representation of the object
print(HttpEndpointTestsDataSearchSort.to_json())

# convert the object into a dict
http_endpoint_tests_data_search_sort_dict = http_endpoint_tests_data_search_sort_instance.to_dict()
# create an instance of HttpEndpointTestsDataSearchSort from a dict
http_endpoint_tests_data_search_sort_from_dict = HttpEndpointTestsDataSearchSort.from_dict(http_endpoint_tests_data_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


