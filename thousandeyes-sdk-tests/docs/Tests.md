# Tests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[SimpleTest]**](SimpleTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.tests import Tests

# TODO update the JSON string below
json = "{}"
# create an instance of Tests from a JSON string
tests_instance = Tests.from_json(json)
# print the JSON string representation of the object
print(Tests.to_json())

# convert the object into a dict
tests_dict = tests_instance.to_dict()
# create an instance of Tests from a dict
tests_from_dict = Tests.from_dict(tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


