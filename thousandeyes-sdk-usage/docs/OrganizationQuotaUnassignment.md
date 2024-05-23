# OrganizationQuotaUnassignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Unique identifier of the organization. | [optional] 
**account_groups** | **List[str]** | List of account group IDs. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.organization_quota_unassignment import OrganizationQuotaUnassignment

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationQuotaUnassignment from a JSON string
organization_quota_unassignment_instance = OrganizationQuotaUnassignment.from_json(json)
# print the JSON string representation of the object
print(OrganizationQuotaUnassignment.to_json())

# convert the object into a dict
organization_quota_unassignment_dict = organization_quota_unassignment_instance.to_dict()
# create an instance of OrganizationQuotaUnassignment from a dict
organization_quota_unassignment_from_dict = OrganizationQuotaUnassignment.from_dict(organization_quota_unassignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


