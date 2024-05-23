# MultiTestIdTestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 
**test_id** | **List[str]** |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_tests_data_search_filter import MultiTestIdTestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTestIdTestsDataSearchFilter from a JSON string
multi_test_id_tests_data_search_filter_instance = MultiTestIdTestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(MultiTestIdTestsDataSearchFilter.to_json())

# convert the object into a dict
multi_test_id_tests_data_search_filter_dict = multi_test_id_tests_data_search_filter_instance.to_dict()
# create an instance of MultiTestIdTestsDataSearchFilter from a dict
multi_test_id_tests_data_search_filter_from_dict = MultiTestIdTestsDataSearchFilter.from_dict(multi_test_id_tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


