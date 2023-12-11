# DynamicBaseTestResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**DynamicTestApplication**](DynamicTestApplication.md) |  | [optional] 
**webex** | [**DynamicBaseTestResultWebex**](DynamicBaseTestResultWebex.md) |  | [optional] 

## Example

```python
from test_results_api.models.dynamic_base_test_result import DynamicBaseTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicBaseTestResult from a JSON string
dynamic_base_test_result_instance = DynamicBaseTestResult.from_json(json)
# print the JSON string representation of the object
print DynamicBaseTestResult.to_json()

# convert the object into a dict
dynamic_base_test_result_dict = dynamic_base_test_result_instance.to_dict()
# create an instance of DynamicBaseTestResult from a dict
dynamic_base_test_result_form_dict = dynamic_base_test_result.from_dict(dynamic_base_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


