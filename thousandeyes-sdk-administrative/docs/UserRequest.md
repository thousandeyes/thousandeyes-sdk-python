# UserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**login_account_group_id** | **str** | Unique ID of the login account group. | [optional] 
**account_group_roles** | [**List[UserAccountGroupRole]**](UserAccountGroupRole.md) |  | [optional] 
**all_account_group_role_ids** | **List[str]** | Unique IDs representing the roles. | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.user_request import UserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequest from a JSON string
user_request_instance = UserRequest.from_json(json)
# print the JSON string representation of the object
print(UserRequest.to_json())

# convert the object into a dict
user_request_dict = user_request_instance.to_dict()
# create an instance of UserRequest from a dict
user_request_from_dict = UserRequest.from_dict(user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


