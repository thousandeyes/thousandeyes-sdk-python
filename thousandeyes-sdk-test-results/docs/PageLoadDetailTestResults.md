# PageLoadDetailTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PageLoadDetailTestResult]**](PageLoadDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.page_load_detail_test_results import PageLoadDetailTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PageLoadDetailTestResults from a JSON string
page_load_detail_test_results_instance = PageLoadDetailTestResults.from_json(json)
# print the JSON string representation of the object
print(PageLoadDetailTestResults.to_json())

# convert the object into a dict
page_load_detail_test_results_dict = page_load_detail_test_results_instance.to_dict()
# create an instance of PageLoadDetailTestResults from a dict
page_load_detail_test_results_from_dict = PageLoadDetailTestResults.from_dict(page_load_detail_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


