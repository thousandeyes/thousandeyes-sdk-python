# OrganizationsQuotasAssignOrganizationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Unique identifier of the organization. | [optional] 
**account_groups** | [**List[AccountGroupQuota]**](AccountGroupQuota.md) | List of account groups quotas. | [optional] 

## Example

```python
from usage_api.models.organizations_quotas_assign_organizations_inner import OrganizationsQuotasAssignOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsQuotasAssignOrganizationsInner from a JSON string
organizations_quotas_assign_organizations_inner_instance = OrganizationsQuotasAssignOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print OrganizationsQuotasAssignOrganizationsInner.to_json()

# convert the object into a dict
organizations_quotas_assign_organizations_inner_dict = organizations_quotas_assign_organizations_inner_instance.to_dict()
# create an instance of OrganizationsQuotasAssignOrganizationsInner from a dict
organizations_quotas_assign_organizations_inner_form_dict = organizations_quotas_assign_organizations_inner.from_dict(organizations_quotas_assign_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


