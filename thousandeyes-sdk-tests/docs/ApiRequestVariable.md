# ApiRequestVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variable name | [optional] 
**value** | **str** | The JSON path of data within the Response Body to assign to this variable. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.api_request_variable import ApiRequestVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestVariable from a JSON string
api_request_variable_instance = ApiRequestVariable.from_json(json)
# print the JSON string representation of the object
print(ApiRequestVariable.to_json())

# convert the object into a dict
api_request_variable_dict = api_request_variable_instance.to_dict()
# create an instance of ApiRequestVariable from a dict
api_request_variable_from_dict = ApiRequestVariable.from_dict(api_request_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


