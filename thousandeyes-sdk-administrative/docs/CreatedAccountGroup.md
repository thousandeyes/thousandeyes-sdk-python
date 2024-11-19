# CreatedAccountGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**account_group_name** | **str** | Account group name | [optional] 
**is_current_account_group** | **bool** | Indicates whether the requested aid is the context of the current account. | [optional] 
**is_default_account_group** | **bool** | Indicates whether the aid is the default one for the requesting user. | [optional] 
**organization_name** | **str** | (Optional) The name of the organization associated with the account group. | [optional] 
**org_id** | **str** | (Optional) The ID for the organization associated with the account group. | [optional] 
**users** | [**List[UserAccountGroup]**](UserAccountGroup.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.created_account_group import CreatedAccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedAccountGroup from a JSON string
created_account_group_instance = CreatedAccountGroup.from_json(json)
# print the JSON string representation of the object
print(CreatedAccountGroup.to_json())

# convert the object into a dict
created_account_group_dict = created_account_group_instance.to_dict()
# create an instance of CreatedAccountGroup from a dict
created_account_group_from_dict = CreatedAccountGroup.from_dict(created_account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


