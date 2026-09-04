# AzureInventoryIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Azure inventory monitoring integration. | 
**app_id** | **str** | The Application (client) ID of the service principal. | 
**password** | **str** | The client secret value. | 
**azure_tenant_id** | **str** | The Azure Active Directory tenant ID. | 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.azure_inventory_integration_request import AzureInventoryIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureInventoryIntegrationRequest from a JSON string
azure_inventory_integration_request_instance = AzureInventoryIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(AzureInventoryIntegrationRequest.to_json())

# convert the object into a dict
azure_inventory_integration_request_dict = azure_inventory_integration_request_instance.to_dict()
# create an instance of AzureInventoryIntegrationRequest from a dict
azure_inventory_integration_request_from_dict = AzureInventoryIntegrationRequest.from_dict(azure_inventory_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


