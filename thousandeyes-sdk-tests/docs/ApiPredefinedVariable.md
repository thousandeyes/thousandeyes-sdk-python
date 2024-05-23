# ApiPredefinedVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variable name. Must be unique. | [optional] 
**value** | **str** | Variable value, will be treated as string. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.api_predefined_variable import ApiPredefinedVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPredefinedVariable from a JSON string
api_predefined_variable_instance = ApiPredefinedVariable.from_json(json)
# print the JSON string representation of the object
print(ApiPredefinedVariable.to_json())

# convert the object into a dict
api_predefined_variable_dict = api_predefined_variable_instance.to_dict()
# create an instance of ApiPredefinedVariable from a dict
api_predefined_variable_from_dict = ApiPredefinedVariable.from_dict(api_predefined_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


