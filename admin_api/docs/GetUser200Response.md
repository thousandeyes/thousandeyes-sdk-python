# GetUser200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID of the user. | [optional] 
**date_registered** | **datetime** | UTC date the user registered their account (ISO date-time format). | [optional] 
**login_account_group** | [**AccountGroup1**](AccountGroup1.md) |  | [optional] 
**last_login** | **datetime** | UTC last login of the user (ISO date-time format). | [optional] 
**account_group_roles** | [**List[AccountGroupRolesAccountGroupRolesInner]**](AccountGroupRolesAccountGroupRolesInner.md) |  | [optional] 
**all_account_group_roles** | [**List[Role]**](Role.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin_api.models.get_user200_response import GetUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUser200Response from a JSON string
get_user200_response_instance = GetUser200Response.from_json(json)
# print the JSON string representation of the object
print GetUser200Response.to_json()

# convert the object into a dict
get_user200_response_dict = get_user200_response_instance.to_dict()
# create an instance of GetUser200Response from a dict
get_user200_response_form_dict = get_user200_response.from_dict(get_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


