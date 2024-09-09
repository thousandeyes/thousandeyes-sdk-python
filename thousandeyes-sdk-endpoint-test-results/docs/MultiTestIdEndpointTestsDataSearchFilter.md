# MultiTestIdEndpointTestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 
**test_id** | **List[str]** |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_endpoint_tests_data_search_filter import MultiTestIdEndpointTestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTestIdEndpointTestsDataSearchFilter from a JSON string
multi_test_id_endpoint_tests_data_search_filter_instance = MultiTestIdEndpointTestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(MultiTestIdEndpointTestsDataSearchFilter.to_json())

# convert the object into a dict
multi_test_id_endpoint_tests_data_search_filter_dict = multi_test_id_endpoint_tests_data_search_filter_instance.to_dict()
# create an instance of MultiTestIdEndpointTestsDataSearchFilter from a dict
multi_test_id_endpoint_tests_data_search_filter_from_dict = MultiTestIdEndpointTestsDataSearchFilter.from_dict(multi_test_id_endpoint_tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


