# EndpointTestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_search_filter import EndpointTestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestsDataSearchFilter from a JSON string
endpoint_tests_data_search_filter_instance = EndpointTestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(EndpointTestsDataSearchFilter.to_json())

# convert the object into a dict
endpoint_tests_data_search_filter_dict = endpoint_tests_data_search_filter_instance.to_dict()
# create an instance of EndpointTestsDataSearchFilter from a dict
endpoint_tests_data_search_filter_from_dict = EndpointTestsDataSearchFilter.from_dict(endpoint_tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


