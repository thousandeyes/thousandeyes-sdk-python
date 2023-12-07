# CreateAccountGroup201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**account_group_name** | **str** | Account group name | [optional] 
**is_current_account_group** | **bool** | Indicates whether the requested aid is the context of the current account. | [optional] 
**is_default_account_group** | **bool** | Indicates whether the aid is the default one for the requesting user. | [optional] 
**organization_name** | **str** | (Optional) Indicates whether the aid is the default one for the requesting user. | [optional] 
**users** | [**List[UserAccountGroup]**](UserAccountGroup.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin_api.models.create_account_group201_response import CreateAccountGroup201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountGroup201Response from a JSON string
create_account_group201_response_instance = CreateAccountGroup201Response.from_json(json)
# print the JSON string representation of the object
print CreateAccountGroup201Response.to_json()

# convert the object into a dict
create_account_group201_response_dict = create_account_group201_response_instance.to_dict()
# create an instance of CreateAccountGroup201Response from a dict
create_account_group201_response_form_dict = create_account_group201_response.from_dict(create_account_group201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


