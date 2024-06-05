# UserAccountGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID representing the user. | [optional] 
**last_login** | **datetime** | User&#39;s UTC last login date (ISO date-time format). | [optional] 
**date_registered** | **datetime** | User&#39;s UTC registration date (ISO date-time format). | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.user_account_group import UserAccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountGroup from a JSON string
user_account_group_instance = UserAccountGroup.from_json(json)
# print the JSON string representation of the object
print(UserAccountGroup.to_json())

# convert the object into a dict
user_account_group_dict = user_account_group_instance.to_dict()
# create an instance of UserAccountGroup from a dict
user_account_group_from_dict = UserAccountGroup.from_dict(user_account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


