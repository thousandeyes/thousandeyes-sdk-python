# GetRoles200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin_api.models.get_roles200_response import GetRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoles200Response from a JSON string
get_roles200_response_instance = GetRoles200Response.from_json(json)
# print the JSON string representation of the object
print GetRoles200Response.to_json()

# convert the object into a dict
get_roles200_response_dict = get_roles200_response_instance.to_dict()
# create an instance of GetRoles200Response from a dict
get_roles200_response_form_dict = get_roles200_response.from_dict(get_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


