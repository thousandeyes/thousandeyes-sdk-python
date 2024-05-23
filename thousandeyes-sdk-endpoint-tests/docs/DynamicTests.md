# DynamicTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[DynamicTest]**](DynamicTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.dynamic_tests import DynamicTests

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTests from a JSON string
dynamic_tests_instance = DynamicTests.from_json(json)
# print the JSON string representation of the object
print(DynamicTests.to_json())

# convert the object into a dict
dynamic_tests_dict = dynamic_tests_instance.to_dict()
# create an instance of DynamicTests from a dict
dynamic_tests_from_dict = DynamicTests.from_dict(dynamic_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


