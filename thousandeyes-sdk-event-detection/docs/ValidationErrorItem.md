# ValidationErrorItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | (Optional) A unique error type/code that can be referenced in the documentation for further details. | [optional] 
**var_field** | **str** | Identifies the field that triggered this particular error. | [optional] 
**message** | **str** | A short, human-readable summary of the error. | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.validation_error_item import ValidationErrorItem

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorItem from a JSON string
validation_error_item_instance = ValidationErrorItem.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorItem.to_json())

# convert the object into a dict
validation_error_item_dict = validation_error_item_instance.to_dict()
# create an instance of ValidationErrorItem from a dict
validation_error_item_from_dict = ValidationErrorItem.from_dict(validation_error_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


