# UsageQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month_start** | **datetime** | Beginning of usage period in UTC (ISO date-time format). | [optional] 
**month_end** | **datetime** | End of usage period in UTC (ISO date-time format).. | [optional] 
**cloud_units_included** | **int** | Monthly number of cloud units allocated, as part of the contract. | [optional] 
**device_agents_included** | **int** | Number of device agents (connected devices product) allocated monthly, as specified in the contract. | [optional] 
**endpoint_agents_included** | **int** | Monthly number of endpoint agents allocated, as part of the contract. | [optional] 
**endpoint_agents_essentials_included** | **int** | Monthly number of endpoint agents essentials allocated, as part of the contract. | [optional] 
**endpoint_agents_embedded_included** | **int** | Number of embedded endpoint agents allocated monthly, as specified in the contract. | [optional] 
**enterprise_agents_included** | **int** | Monthly number of enterprise agents allocated, as part of the contract. Returns non-zero value only for organizations with legacy billing. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.usage_quota import UsageQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UsageQuota from a JSON string
usage_quota_instance = UsageQuota.from_json(json)
# print the JSON string representation of the object
print(UsageQuota.to_json())

# convert the object into a dict
usage_quota_dict = usage_quota_instance.to_dict()
# create an instance of UsageQuota from a dict
usage_quota_from_dict = UsageQuota.from_dict(usage_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


