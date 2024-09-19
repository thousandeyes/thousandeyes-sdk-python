# HttpEndpointTestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **List[str]** | Filter by test | [optional] 
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_search_filter import HttpEndpointTestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HttpEndpointTestsDataSearchFilter from a JSON string
http_endpoint_tests_data_search_filter_instance = HttpEndpointTestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(HttpEndpointTestsDataSearchFilter.to_json())

# convert the object into a dict
http_endpoint_tests_data_search_filter_dict = http_endpoint_tests_data_search_filter_instance.to_dict()
# create an instance of HttpEndpointTestsDataSearchFilter from a dict
http_endpoint_tests_data_search_filter_from_dict = HttpEndpointTestsDataSearchFilter.from_dict(http_endpoint_tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


