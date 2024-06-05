# AccountGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_groups** | [**List[AccountGroupInfo]**](AccountGroupInfo.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.account_groups import AccountGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroups from a JSON string
account_groups_instance = AccountGroups.from_json(json)
# print the JSON string representation of the object
print(AccountGroups.to_json())

# convert the object into a dict
account_groups_dict = account_groups_instance.to_dict()
# create an instance of AccountGroups from a dict
account_groups_from_dict = AccountGroups.from_dict(account_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


