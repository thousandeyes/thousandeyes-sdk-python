# CreatedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID of the user. | [optional] 
**date_registered** | **datetime** | UTC date the user registered their account (ISO date-time format). | [optional] 
**login_account_group** | [**AccountGroup**](AccountGroup.md) |  | [optional] 
**account_group_roles** | [**List[AccountGroupRole]**](AccountGroupRole.md) |  | [optional] 
**all_account_group_roles** | [**List[Role]**](Role.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.created_user import CreatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedUser from a JSON string
created_user_instance = CreatedUser.from_json(json)
# print the JSON string representation of the object
print(CreatedUser.to_json())

# convert the object into a dict
created_user_dict = created_user_instance.to_dict()
# create an instance of CreatedUser from a dict
created_user_from_dict = CreatedUser.from_dict(created_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


