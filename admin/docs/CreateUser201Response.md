# CreateUser201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID of the user. | [optional] 
**date_registered** | **datetime** | UTC date the user registered their account (ISO date-time format). | [optional] 
**login_account_group** | [**AccountGroup1**](AccountGroup1.md) |  | [optional] 
**account_group_roles** | [**List[AccountGroupRolesAccountGroupRolesInner]**](AccountGroupRolesAccountGroupRolesInner.md) |  | [optional] 
**all_account_group_roles** | [**List[Role]**](Role.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.admin.models.create_user201_response import CreateUser201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUser201Response from a JSON string
create_user201_response_instance = CreateUser201Response.from_json(json)
# print the JSON string representation of the object
print(CreateUser201Response.to_json())

# convert the object into a dict
create_user201_response_dict = create_user201_response_instance.to_dict()
# create an instance of CreateUser201Response from a dict
create_user201_response_from_dict = CreateUser201Response.from_dict(create_user201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


