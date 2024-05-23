# OrganizationsQuotasAssign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationQuotaAssignment]**](OrganizationQuotaAssignment.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.organizations_quotas_assign import OrganizationsQuotasAssign

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsQuotasAssign from a JSON string
organizations_quotas_assign_instance = OrganizationsQuotasAssign.from_json(json)
# print the JSON string representation of the object
print(OrganizationsQuotasAssign.to_json())

# convert the object into a dict
organizations_quotas_assign_dict = organizations_quotas_assign_instance.to_dict()
# create an instance of OrganizationsQuotasAssign from a dict
organizations_quotas_assign_from_dict = OrganizationsQuotasAssign.from_dict(organizations_quotas_assign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


