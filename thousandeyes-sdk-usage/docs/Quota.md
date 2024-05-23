# Quota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_quota** | [**OrganizationQuota**](OrganizationQuota.md) |  | [optional] 
**account_group_quotas** | [**List[AccountGroupQuota]**](AccountGroupQuota.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.quota import Quota

# TODO update the JSON string below
json = "{}"
# create an instance of Quota from a JSON string
quota_instance = Quota.from_json(json)
# print the JSON string representation of the object
print(Quota.to_json())

# convert the object into a dict
quota_dict = quota_instance.to_dict()
# create an instance of Quota from a dict
quota_from_dict = Quota.from_dict(quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


