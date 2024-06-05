# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**uid** | **str** | Unique ID of the user. | [optional] 
**date_registered** | **datetime** | UTC date the user registered their account (ISO date-time format). | [optional] 
**login_account_group** | [**AccountGroup**](AccountGroup.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


