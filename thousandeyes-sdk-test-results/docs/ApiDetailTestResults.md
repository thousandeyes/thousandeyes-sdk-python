# ApiDetailTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ApiDetailTestResult]**](ApiDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.api_detail_test_results import ApiDetailTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDetailTestResults from a JSON string
api_detail_test_results_instance = ApiDetailTestResults.from_json(json)
# print the JSON string representation of the object
print(ApiDetailTestResults.to_json())

# convert the object into a dict
api_detail_test_results_dict = api_detail_test_results_instance.to_dict()
# create an instance of ApiDetailTestResults from a dict
api_detail_test_results_from_dict = ApiDetailTestResults.from_dict(api_detail_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


