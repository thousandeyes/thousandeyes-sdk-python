# RealUserTestPageResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RealUserTestPageResult]**](RealUserTestPageResult.md) |  | [optional] 

## Example

```python
from test_results_api.models.real_user_test_page_results import RealUserTestPageResults

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserTestPageResults from a JSON string
real_user_test_page_results_instance = RealUserTestPageResults.from_json(json)
# print the JSON string representation of the object
print RealUserTestPageResults.to_json()

# convert the object into a dict
real_user_test_page_results_dict = real_user_test_page_results_instance.to_dict()
# create an instance of RealUserTestPageResults from a dict
real_user_test_page_results_form_dict = real_user_test_page_results.from_dict(real_user_test_page_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


