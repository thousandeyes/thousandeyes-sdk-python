# QuotasQuotasInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_quota** | [**OrganizationQuota**](OrganizationQuota.md) |  | [optional] 
**account_group_quotas** | [**List[AccountGroupQuota]**](AccountGroupQuota.md) |  | [optional] 

## Example

```python
from usage_api.models.quotas_quotas_inner import QuotasQuotasInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuotasQuotasInner from a JSON string
quotas_quotas_inner_instance = QuotasQuotasInner.from_json(json)
# print the JSON string representation of the object
print QuotasQuotasInner.to_json()

# convert the object into a dict
quotas_quotas_inner_dict = quotas_quotas_inner_instance.to_dict()
# create an instance of QuotasQuotasInner from a dict
quotas_quotas_inner_form_dict = quotas_quotas_inner.from_dict(quotas_quotas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


