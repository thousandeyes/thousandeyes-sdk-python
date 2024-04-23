# GetPermissions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin.models.get_permissions200_response import GetPermissions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPermissions200Response from a JSON string
get_permissions200_response_instance = GetPermissions200Response.from_json(json)
# print the JSON string representation of the object
print(GetPermissions200Response.to_json())

# convert the object into a dict
get_permissions200_response_dict = get_permissions200_response_instance.to_dict()
# create an instance of GetPermissions200Response from a dict
get_permissions200_response_from_dict = GetPermissions200Response.from_dict(get_permissions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


