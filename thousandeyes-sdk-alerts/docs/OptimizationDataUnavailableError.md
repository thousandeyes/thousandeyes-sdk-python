# OptimizationDataUnavailableError

Problem details returned when an explicitly filtered alert-rule list cannot be evaluated because optimization data is unavailable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A URI reference that identifies the problem type. When this member is not present, its value is assumed to be \&quot;about:blank\&quot;. | [optional] 
**title** | **str** | A short, human-readable summary of the problem type. | [optional] 
**status** | **int** |  | 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**instance** | **str** | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**code** | [**OptimizationDataUnavailableCode**](OptimizationDataUnavailableCode.md) |  | 

## Example

```python
from thousandeyes_sdk.alerts.models.optimization_data_unavailable_error import OptimizationDataUnavailableError

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationDataUnavailableError from a JSON string
optimization_data_unavailable_error_instance = OptimizationDataUnavailableError.from_json(json)
# print the JSON string representation of the object
print(OptimizationDataUnavailableError.to_json())

# convert the object into a dict
optimization_data_unavailable_error_dict = optimization_data_unavailable_error_instance.to_dict()
# create an instance of OptimizationDataUnavailableError from a dict
optimization_data_unavailable_error_from_dict = OptimizationDataUnavailableError.from_dict(optimization_data_unavailable_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


