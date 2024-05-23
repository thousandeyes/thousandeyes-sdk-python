# OrganizationsQuotasUnassign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationQuotaUnassignment]**](OrganizationQuotaUnassignment.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.organizations_quotas_unassign import OrganizationsQuotasUnassign

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsQuotasUnassign from a JSON string
organizations_quotas_unassign_instance = OrganizationsQuotasUnassign.from_json(json)
# print the JSON string representation of the object
print(OrganizationsQuotasUnassign.to_json())

# convert the object into a dict
organizations_quotas_unassign_dict = organizations_quotas_unassign_instance.to_dict()
# create an instance of OrganizationsQuotasUnassign from a dict
organizations_quotas_unassign_from_dict = OrganizationsQuotasUnassign.from_dict(organizations_quotas_unassign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


