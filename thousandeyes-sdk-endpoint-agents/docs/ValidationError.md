# ValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A URI reference that identifies the problem type. When this member is not present, its value is assumed to be \&quot;about:blank\&quot;. | [optional] 
**title** | **str** | A short, human-readable summary of the problem type. | [optional] 
**status** | **int** | The HTTP status code generated by the origin server for this occurrence of the problem. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**instance** | **str** | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**errors** | [**List[ValidationErrorItem]**](ValidationErrorItem.md) | (Optional) When multiple errors occur, the details for each error are listed. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_from_dict = ValidationError.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


