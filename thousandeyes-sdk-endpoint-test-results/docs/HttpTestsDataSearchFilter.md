# HttpTestsDataSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **List[str]** | Filter by test | [optional] 
**agent_id** | **List[str]** | Filter using the &#x60;agent-id&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_tests_data_search_filter import HttpTestsDataSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTestsDataSearchFilter from a JSON string
http_tests_data_search_filter_instance = HttpTestsDataSearchFilter.from_json(json)
# print the JSON string representation of the object
print(HttpTestsDataSearchFilter.to_json())

# convert the object into a dict
http_tests_data_search_filter_dict = http_tests_data_search_filter_instance.to_dict()
# create an instance of HttpTestsDataSearchFilter from a dict
http_tests_data_search_filter_from_dict = HttpTestsDataSearchFilter.from_dict(http_tests_data_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


