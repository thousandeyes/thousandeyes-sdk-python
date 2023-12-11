# UsageUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota** | [**UsageUsageQuota**](UsageUsageQuota.md) |  | [optional] 
**cloud_units_used** | **int** | Number of cloud units consumed thus far in the usage period. | [optional] 
**cloud_units_projected** | **int** | Number of cloud units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. | [optional] 
**cloud_units_next_billing_period** | **int** | Number of cloud units projected in the upcoming usage period, based on configuration of enabled tests. This value is updated hourly. | [optional] 
**enterprise_units_used** | **int** | Number of enterprise units consumed in the usage period. Returns non-zero value only for organizations with metered billing. | [optional] 
**enterprise_units_projected** | **int** | Number of enterprise units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing. | [optional] 
**enterprise_units_next_billing_period** | **int** | Number of enterprise units projected in the upcoming usage period, based on configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing. | [optional] 
**endpoint_agents_used** | **int** | Number of endpoint agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**endpoint_agents_essentials_used** | **int** | Number of endpoint agents essentials used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**endpoint_agents_embedded_used** | **int** | Number of embedded endpoint agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**enterprise_agents_used** | **int** | Number of enterprise agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**enterprise_agent_units** | [**List[EnterpriseAgentUnitsInner]**](EnterpriseAgentUnitsInner.md) | A breakdown of enterprise unit consumption for each agent during the current monthly period. Each entry provides data for both the current actual usage and the projected usage. Returns non-zero values for organizations with metered billing. | [optional] 
**tests** | [**List[TestsInner]**](TestsInner.md) | A breakdown of unit consumption for each test during the current monthly period. Each entry provides information about both the current actual usage and the projected usage. | [optional] 
**endpoint_agents** | [**List[EndpointAgentsInner]**](EndpointAgentsInner.md) | Endpoint agents used by account group. | [optional] 
**endpoint_agents_essentials** | [**List[EndpointAgentsEssentialsInner]**](EndpointAgentsEssentialsInner.md) | Endpoint agents essentials used by account group. | [optional] 
**endpoint_agents_embedded** | [**List[EndpointAgentsEmbeddedInner]**](EndpointAgentsEmbeddedInner.md) | Endpoint agents embedded used by account group. | [optional] 
**enterprise_agents** | [**List[EnterpriseAgentsInner]**](EnterpriseAgentsInner.md) | Enterprise agents used by account group. | [optional] 

## Example

```python
from usage_api.models.usage_usage import UsageUsage

# TODO update the JSON string below
json = "{}"
# create an instance of UsageUsage from a JSON string
usage_usage_instance = UsageUsage.from_json(json)
# print the JSON string representation of the object
print UsageUsage.to_json()

# convert the object into a dict
usage_usage_dict = usage_usage_instance.to_dict()
# create an instance of UsageUsage from a dict
usage_usage_form_dict = usage_usage.from_dict(usage_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


