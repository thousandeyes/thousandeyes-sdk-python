# AccountGroupDetail


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
**agents** | [**List[EnterpriseAgent]**](EnterpriseAgent.md) |  | [optional] 
**account_token** | **str** | The account group token is an alphanumeric string used to bind an Enterprise Agent to a specific account group. This token is not a password that must be kept secret. You can retrieve your &#x60;AccountGroupToken&#x60; from the &#x60;/account-groups/{id}&#x60; endpoint. | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.account_group_detail import AccountGroupDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupDetail from a JSON string
account_group_detail_instance = AccountGroupDetail.from_json(json)
# print the JSON string representation of the object
print(AccountGroupDetail.to_json())

# convert the object into a dict
account_group_detail_dict = account_group_detail_instance.to_dict()
# create an instance of AccountGroupDetail from a dict
account_group_detail_from_dict = AccountGroupDetail.from_dict(account_group_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


