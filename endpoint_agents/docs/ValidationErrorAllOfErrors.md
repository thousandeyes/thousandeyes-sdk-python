# ValidationErrorAllOfErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | (Optional) A unique error type/code that can be referenced in the documentation for further details. | [optional] 
**var_field** | **int** | Identifies the field that triggered this particular error. | [optional] 
**message** | **str** | A short, human-readable summary of the error. | [optional] 

## Example

```python
from endpoint_agents.models.validation_error_all_of_errors import ValidationErrorAllOfErrors

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorAllOfErrors from a JSON string
validation_error_all_of_errors_instance = ValidationErrorAllOfErrors.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorAllOfErrors.to_json())

# convert the object into a dict
validation_error_all_of_errors_dict = validation_error_all_of_errors_instance.to_dict()
# create an instance of ValidationErrorAllOfErrors from a dict
validation_error_all_of_errors_from_dict = ValidationErrorAllOfErrors.from_dict(validation_error_all_of_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


