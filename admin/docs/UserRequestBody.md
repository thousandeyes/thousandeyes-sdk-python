# UserRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s display name. | [optional] 
**email** | **str** | User&#39;s email address. | [optional] 
**login_account_group_id** | **str** | Unique ID of the login account group. | [optional] 
**account_group_roles** | [**List[AccountGroupRolesRequestBodyInner]**](AccountGroupRolesRequestBodyInner.md) |  | [optional] 
**all_account_group_role_ids** | **List[str]** | Unique IDs representing the roles. | [optional] 

## Example

```python
from thousandeyes_sdk.admin.models.user_request_body import UserRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequestBody from a JSON string
user_request_body_instance = UserRequestBody.from_json(json)
# print the JSON string representation of the object
print(UserRequestBody.to_json())

# convert the object into a dict
user_request_body_dict = user_request_body_instance.to_dict()
# create an instance of UserRequestBody from a dict
user_request_body_from_dict = UserRequestBody.from_dict(user_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


