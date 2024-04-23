# GetTestResultPageLoadComponentDetail200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PageLoadDetailTestResult]**](PageLoadDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from test_results.models.get_test_result_page_load_component_detail200_response import GetTestResultPageLoadComponentDetail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultPageLoadComponentDetail200Response from a JSON string
get_test_result_page_load_component_detail200_response_instance = GetTestResultPageLoadComponentDetail200Response.from_json(json)
# print the JSON string representation of the object
print(GetTestResultPageLoadComponentDetail200Response.to_json())

# convert the object into a dict
get_test_result_page_load_component_detail200_response_dict = get_test_result_page_load_component_detail200_response_instance.to_dict()
# create an instance of GetTestResultPageLoadComponentDetail200Response from a dict
get_test_result_page_load_component_detail200_response_from_dict = GetTestResultPageLoadComponentDetail200Response.from_dict(get_test_result_page_load_component_detail200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


