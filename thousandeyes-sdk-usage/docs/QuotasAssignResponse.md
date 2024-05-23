# QuotasAssignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationQuota]**](OrganizationQuota.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.quotas_assign_response import QuotasAssignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotasAssignResponse from a JSON string
quotas_assign_response_instance = QuotasAssignResponse.from_json(json)
# print the JSON string representation of the object
print(QuotasAssignResponse.to_json())

# convert the object into a dict
quotas_assign_response_dict = quotas_assign_response_instance.to_dict()
# create an instance of QuotasAssignResponse from a dict
quotas_assign_response_from_dict = QuotasAssignResponse.from_dict(quotas_assign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


