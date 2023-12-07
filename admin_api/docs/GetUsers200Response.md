# GetUsers200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ExtendedUser]**](ExtendedUser.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin_api.models.get_users200_response import GetUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsers200Response from a JSON string
get_users200_response_instance = GetUsers200Response.from_json(json)
# print the JSON string representation of the object
print GetUsers200Response.to_json()

# convert the object into a dict
get_users200_response_dict = get_users200_response_instance.to_dict()
# create an instance of GetUsers200Response from a dict
get_users200_response_form_dict = get_users200_response.from_dict(get_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


