# TestCustomHeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root** | **Dict[str, str]** | Use these HTTP headers for root server request. | [optional] 
**domains** | **Dict[str, Dict[str, str]]** | Use these HTTP headers for the specified domains. | [optional] 
**all** | **Dict[str, str]** | Use these HTTP headers for all domains. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.test_custom_headers import TestCustomHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of TestCustomHeaders from a JSON string
test_custom_headers_instance = TestCustomHeaders.from_json(json)
# print the JSON string representation of the object
print(TestCustomHeaders.to_json())

# convert the object into a dict
test_custom_headers_dict = test_custom_headers_instance.to_dict()
# create an instance of TestCustomHeaders from a dict
test_custom_headers_from_dict = TestCustomHeaders.from_dict(test_custom_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


