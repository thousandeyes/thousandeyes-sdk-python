# DynamicEndpointTestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 
**webex_conference_id** | **List[str]** | Filter using the &#x60;conference-id&#x60; of the webex call. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.dynamic_endpoint_tests_data_search_filter import DynamicEndpointTestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicEndpointTestsDataSearchFilter from a JSON string
dynamic_endpoint_tests_data_search_filter_instance = DynamicEndpointTestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(DynamicEndpointTestsDataSearchFilter.to_json())

# convert the object into a dict
dynamic_endpoint_tests_data_search_filter_dict = dynamic_endpoint_tests_data_search_filter_instance.to_dict()
# create an instance of DynamicEndpointTestsDataSearchFilter from a dict
dynamic_endpoint_tests_data_search_filter_from_dict = DynamicEndpointTestsDataSearchFilter.from_dict(dynamic_endpoint_tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


