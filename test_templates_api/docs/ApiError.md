# ApiError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from test_templates_api.models.api_error import ApiError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError from a JSON string
api_error_instance = ApiError.from_json(json)
# print the JSON string representation of the object
print ApiError.to_json()

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of ApiError from a dict
api_error_form_dict = api_error.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


