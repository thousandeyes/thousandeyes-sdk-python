# AzureMonitoringIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for the Azure inventory or flow logs monitoring integration. | 
**name** | **str** | The name of the Azure inventory or flow logs monitoring integration. | 
**app_id** | **str** | The Application (client) ID of the service principal. | 
**password** | **str** | The client secret value. For security reasons, the client secret value is masked. | 
**azure_tenant_id** | **str** | The Azure Active Directory tenant ID. | 
**service_bus_queue_url** | **str** | The URL of the Service Bus Queue. Relevant only for flow logs monitoring integrations. | [optional] 
**monitoring_type** | **str** | The type of monitoring integration. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integration import AzureMonitoringIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMonitoringIntegration from a JSON string
azure_monitoring_integration_instance = AzureMonitoringIntegration.from_json(json)
# print the JSON string representation of the object
print(AzureMonitoringIntegration.to_json())

# convert the object into a dict
azure_monitoring_integration_dict = azure_monitoring_integration_instance.to_dict()
# create an instance of AzureMonitoringIntegration from a dict
azure_monitoring_integration_from_dict = AzureMonitoringIntegration.from_dict(azure_monitoring_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


