# UsageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota** | [**UsageQuota**](UsageQuota.md) |  | [optional] 
**cloud_units_used** | **int** | Number of cloud units consumed thus far in the usage period. | [optional] 
**cloud_units_projected** | **int** | Number of cloud units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. | [optional] 
**cloud_units_next_billing_period** | **int** | Number of cloud units projected in the upcoming usage period, based on configuration of enabled tests. This value is updated hourly. | [optional] 
**enterprise_units_used** | **int** | Number of enterprise units consumed in the usage period. Returns non-zero value only for organizations with metered billing. | [optional] 
**enterprise_units_projected** | **int** | Number of enterprise units projected in the current usage period, based on units consumed to date and configuration of enabled tests. This value is updated hourly. Returns non-zero value only for organizations with metered billing. | [optional] 
**enterprise_units_next_billing_period** | **int** | Projected number of enterprise units for the upcoming usage period, based on the configuration of enabled tests. This value is updated hourly and returns a non-zero value only for organizations with metered billing. | [optional] 
**connected_devices_units_used** | **int** | Number of connected device units consumed in the usage period. | [optional] 
**connected_devices_units_projected** | **int** | Projected number of connected device units for the current usage period. This projection is based on the units consumed to date and the configuration of enabled tests. The value is updated hourly. | [optional] 
**connected_devices_units_next_billing_period** | **int** | Projected number of connected device units for the upcoming usage period. This projection is based on the configuration of enabled tests and is updated hourly. | [optional] 
**endpoint_agents_used** | **int** | Number of endpoint agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**endpoint_agents_essentials_used** | **int** | Number of endpoint agents essentials used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**endpoint_agents_embedded_used** | **int** | Number of embedded endpoint agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**enterprise_agents_used** | **int** | Number of enterprise agents used in the current usage period. This number is calculated by taking the maximum number of agents enabled for any one-hour period in the usage period. Disabled agents are excluded from this calculation. | [optional] 
**enterprise_agent_units** | [**List[EnterpriseAgentUnits]**](EnterpriseAgentUnits.md) | A breakdown of enterprise unit consumption for each agent during the current monthly period. Each entry provides data for both the current actual usage and the projected usage. Returns non-zero values for organizations with metered billing. | [optional] 
**tests** | [**List[TestUsage]**](TestUsage.md) | A breakdown of unit consumption for each test during the current monthly period. Each entry provides information about both the current actual usage and the projected usage. | [optional] 
**endpoint_agents** | [**List[EndpointAgentsUsage]**](EndpointAgentsUsage.md) | Endpoint agents used by account group. | [optional] 
**endpoint_agents_essentials** | [**List[EndpointAgentsEssentials]**](EndpointAgentsEssentials.md) | Endpoint agents essentials used by account group. | [optional] 
**endpoint_agents_embedded** | [**List[EndpointAgentsEmbedded]**](EndpointAgentsEmbedded.md) | Endpoint agents embedded used by account group. | [optional] 
**enterprise_agents** | [**List[EnterpriseAgents]**](EnterpriseAgents.md) | Enterprise agents used by account group. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.usage_details import UsageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UsageDetails from a JSON string
usage_details_instance = UsageDetails.from_json(json)
# print the JSON string representation of the object
print(UsageDetails.to_json())

# convert the object into a dict
usage_details_dict = usage_details_instance.to_dict()
# create an instance of UsageDetails from a dict
usage_details_from_dict = UsageDetails.from_dict(usage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


