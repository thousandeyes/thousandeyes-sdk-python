# OrganizationQuotaAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Unique identifier of the organization. | [optional] 
**account_groups** | [**List[AccountGroupQuota]**](AccountGroupQuota.md) | List of account groups quotas. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.organization_quota_assignment import OrganizationQuotaAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationQuotaAssignment from a JSON string
organization_quota_assignment_instance = OrganizationQuotaAssignment.from_json(json)
# print the JSON string representation of the object
print(OrganizationQuotaAssignment.to_json())

# convert the object into a dict
organization_quota_assignment_dict = organization_quota_assignment_instance.to_dict()
# create an instance of OrganizationQuotaAssignment from a dict
organization_quota_assignment_from_dict = OrganizationQuotaAssignment.from_dict(organization_quota_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


