# UserDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID of the user. | [optional] 
**date_registered** | **datetime** | UTC date the user registered their account (ISO date-time format). | [optional] 
**login_account_group** | [**AccountGroup**](AccountGroup.md) |  | [optional] 
**last_login** | **datetime** | UTC last login of the user (ISO date-time format). | [optional] 
**account_group_roles** | [**List[AccountGroupRole]**](AccountGroupRole.md) |  | [optional] 
**all_account_group_roles** | [**List[Role]**](Role.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.user_detail import UserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetail from a JSON string
user_detail_instance = UserDetail.from_json(json)
# print the JSON string representation of the object
print(UserDetail.to_json())

# convert the object into a dict
user_detail_dict = user_detail_instance.to_dict()
# create an instance of UserDetail from a dict
user_detail_from_dict = UserDetail.from_dict(user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


