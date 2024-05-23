# AccountGroupQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Value of the quota for the given Account Group. | [optional] 
**aid** | **str** | Unique ID of the account group. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.account_group_quota import AccountGroupQuota

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupQuota from a JSON string
account_group_quota_instance = AccountGroupQuota.from_json(json)
# print the JSON string representation of the object
print(AccountGroupQuota.to_json())

# convert the object into a dict
account_group_quota_dict = account_group_quota_instance.to_dict()
# create an instance of AccountGroupQuota from a dict
account_group_quota_from_dict = AccountGroupQuota.from_dict(account_group_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


