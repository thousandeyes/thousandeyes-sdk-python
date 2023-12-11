# UsageUsageQuota


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month_start** | **datetime** | Beginning of usage period in UTC (ISO date-time format). | [optional] 
**month_end** | **datetime** | End of usage period in UTC (ISO date-time format).. | [optional] 
**cloud_units_included** | **int** | Monthly number of cloud units allocated, as part of the contract. | [optional] 
**endpoint_agents_included** | **int** | Monthly number of endpoint agents allocated, as part of the contract. | [optional] 
**endpoint_agents_essentials_included** | **int** | Monthly number of endpoint agents essentials allocated, as part of the contract. | [optional] 
**endpoint_agents_embedded_included** | **int** | Number of embedded endpoint agents allocated monthly, as specified in the contract. | [optional] 
**enterprise_agents_included** | **int** | Monthly number of enterprise agents allocated, as part of the contract. Returns non-zero value only for organizations with legacy billing. | [optional] 

## Example

```python
from usage_api.models.usage_usage_quota import UsageUsageQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UsageUsageQuota from a JSON string
usage_usage_quota_instance = UsageUsageQuota.from_json(json)
# print the JSON string representation of the object
print UsageUsageQuota.to_json()

# convert the object into a dict
usage_usage_quota_dict = usage_usage_quota_instance.to_dict()
# create an instance of UsageUsageQuota from a dict
usage_usage_quota_form_dict = usage_usage_quota.from_dict(usage_usage_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


