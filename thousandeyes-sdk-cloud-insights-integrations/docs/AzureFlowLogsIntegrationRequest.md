# AzureFlowLogsIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Azure flow logs monitoring integration. | 
**app_id** | **str** | The Application (client) ID of the service principal. | 
**password** | **str** | The client secret value. | 
**azure_tenant_id** | **str** | The Azure Active Directory tenant ID. | 
**service_bus_queue_url** | **str** | The URL of the Service Bus Queue. | 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.azure_flow_logs_integration_request import AzureFlowLogsIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureFlowLogsIntegrationRequest from a JSON string
azure_flow_logs_integration_request_instance = AzureFlowLogsIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(AzureFlowLogsIntegrationRequest.to_json())

# convert the object into a dict
azure_flow_logs_integration_request_dict = azure_flow_logs_integration_request_instance.to_dict()
# create an instance of AzureFlowLogsIntegrationRequest from a dict
azure_flow_logs_integration_request_from_dict = AzureFlowLogsIntegrationRequest.from_dict(azure_flow_logs_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


