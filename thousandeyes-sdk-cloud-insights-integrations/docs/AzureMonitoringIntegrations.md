# AzureMonitoringIntegrations

A HAL resource containing a list of Azure inventory and flow logs monitoring integrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[AzureMonitoringIntegration]**](AzureMonitoringIntegration.md) | The list of Azure inventory and flow logs monitoring integrations. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integrations import AzureMonitoringIntegrations

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMonitoringIntegrations from a JSON string
azure_monitoring_integrations_instance = AzureMonitoringIntegrations.from_json(json)
# print the JSON string representation of the object
print(AzureMonitoringIntegrations.to_json())

# convert the object into a dict
azure_monitoring_integrations_dict = azure_monitoring_integrations_instance.to_dict()
# create an instance of AzureMonitoringIntegrations from a dict
azure_monitoring_integrations_from_dict = AzureMonitoringIntegrations.from_dict(azure_monitoring_integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


