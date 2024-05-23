# TestResultAppLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.test_result_app_links import TestResultAppLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultAppLinks from a JSON string
test_result_app_links_instance = TestResultAppLinks.from_json(json)
# print the JSON string representation of the object
print(TestResultAppLinks.to_json())

# convert the object into a dict
test_result_app_links_dict = test_result_app_links_instance.to_dict()
# create an instance of TestResultAppLinks from a dict
test_result_app_links_from_dict = TestResultAppLinks.from_dict(test_result_app_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


