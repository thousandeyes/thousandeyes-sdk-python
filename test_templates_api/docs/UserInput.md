# UserInput

The set of inputs that the user must fill in to use the test template. These inputs are provided by the user when creating a set of tests via the test template API or via the UI. The UI dynamically displays these user inputs for the user to input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the user input field. | 
**title** | **str** | The title of the user input field; may be used by UI. | [optional] 
**description** | **str** | Description of the user input field; used by UI. | [optional] 
**default_value** | [**UserInputDefaultValue**](UserInputDefaultValue.md) |  | [optional] 
**type** | [**UserInputType**](UserInputType.md) |  | 

## Example

```python
from test_templates_api.models.user_input import UserInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserInput from a JSON string
user_input_instance = UserInput.from_json(json)
# print the JSON string representation of the object
print UserInput.to_json()

# convert the object into a dict
user_input_dict = user_input_instance.to_dict()
# create an instance of UserInput from a dict
user_input_form_dict = user_input.from_dict(user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


