# ExtendedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID of the user. | [optional] 
**date_registered** | **datetime** | UTC date the user registered their account (ISO date-time format). | [optional] 
**login_account_group** | [**AccountGroup**](AccountGroup.md) |  | [optional] 
**last_login** | **datetime** | UTC last login of the user (ISO date-time format). | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.extended_user import ExtendedUser

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedUser from a JSON string
extended_user_instance = ExtendedUser.from_json(json)
# print the JSON string representation of the object
print(ExtendedUser.to_json())

# convert the object into a dict
extended_user_dict = extended_user_instance.to_dict()
# create an instance of ExtendedUser from a dict
extended_user_from_dict = ExtendedUser.from_dict(extended_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


