# TestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_filter import TestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TestsDataSearchFilter from a JSON string
tests_data_search_filter_instance = TestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(TestsDataSearchFilter.to_json())

# convert the object into a dict
tests_data_search_filter_dict = tests_data_search_filter_instance.to_dict()
# create an instance of TestsDataSearchFilter from a dict
tests_data_search_filter_from_dict = TestsDataSearchFilter.from_dict(tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


