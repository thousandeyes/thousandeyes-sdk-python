# GetAccountGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_groups** | [**List[AccountGroup]**](AccountGroup.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin.models.get_account_groups200_response import GetAccountGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountGroups200Response from a JSON string
get_account_groups200_response_instance = GetAccountGroups200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountGroups200Response.to_json())

# convert the object into a dict
get_account_groups200_response_dict = get_account_groups200_response_instance.to_dict()
# create an instance of GetAccountGroups200Response from a dict
get_account_groups200_response_from_dict = GetAccountGroups200Response.from_dict(get_account_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


