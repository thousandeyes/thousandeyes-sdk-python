# AccountGroupRolesRequestBodyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group_id** | **str** | Unique ID of the account group. | [optional] 
**role_ids** | **List[str]** | Unique role IDs. | [optional] 

## Example

```python
from admin.models.account_group_roles_request_body_inner import AccountGroupRolesRequestBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupRolesRequestBodyInner from a JSON string
account_group_roles_request_body_inner_instance = AccountGroupRolesRequestBodyInner.from_json(json)
# print the JSON string representation of the object
print(AccountGroupRolesRequestBodyInner.to_json())

# convert the object into a dict
account_group_roles_request_body_inner_dict = account_group_roles_request_body_inner_instance.to_dict()
# create an instance of AccountGroupRolesRequestBodyInner from a dict
account_group_roles_request_body_inner_from_dict = AccountGroupRolesRequestBodyInner.from_dict(account_group_roles_request_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


