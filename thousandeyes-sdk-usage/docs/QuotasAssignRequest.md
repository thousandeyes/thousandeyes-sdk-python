# QuotasAssignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationQuota]**](OrganizationQuota.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.quotas_assign_request import QuotasAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuotasAssignRequest from a JSON string
quotas_assign_request_instance = QuotasAssignRequest.from_json(json)
# print the JSON string representation of the object
print(QuotasAssignRequest.to_json())

# convert the object into a dict
quotas_assign_request_dict = quotas_assign_request_instance.to_dict()
# create an instance of QuotasAssignRequest from a dict
quotas_assign_request_from_dict = QuotasAssignRequest.from_dict(quotas_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


