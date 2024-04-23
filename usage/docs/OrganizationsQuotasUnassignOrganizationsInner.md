# OrganizationsQuotasUnassignOrganizationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Unique identifier of the organization. | [optional] 
**account_groups** | **List[str]** | List of account group IDs. | [optional] 

## Example

```python
from usage.models.organizations_quotas_unassign_organizations_inner import OrganizationsQuotasUnassignOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsQuotasUnassignOrganizationsInner from a JSON string
organizations_quotas_unassign_organizations_inner_instance = OrganizationsQuotasUnassignOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print(OrganizationsQuotasUnassignOrganizationsInner.to_json())

# convert the object into a dict
organizations_quotas_unassign_organizations_inner_dict = organizations_quotas_unassign_organizations_inner_instance.to_dict()
# create an instance of OrganizationsQuotasUnassignOrganizationsInner from a dict
organizations_quotas_unassign_organizations_inner_from_dict = OrganizationsQuotasUnassignOrganizationsInner.from_dict(organizations_quotas_unassign_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


