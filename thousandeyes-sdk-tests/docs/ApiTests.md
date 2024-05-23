# ApiTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedApiTest]**](UnexpandedApiTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.api_tests import ApiTests

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTests from a JSON string
api_tests_instance = ApiTests.from_json(json)
# print the JSON string representation of the object
print(ApiTests.to_json())

# convert the object into a dict
api_tests_dict = api_tests_instance.to_dict()
# create an instance of ApiTests from a dict
api_tests_from_dict = ApiTests.from_dict(api_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


