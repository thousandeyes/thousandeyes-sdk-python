# AzureIntegrationPolicySetting

Azure integration policy configuration that defines the monitored Azure resource groups and the subscription policy that ThousandEyes enforces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_resource_group_types** | [**List[AzureResourceGroupType]**](AzureResourceGroupType.md) | The set of Azure resource group types included in inventory monitoring. | 
**subscriptions_policy** | [**SubscriptionsPolicy**](SubscriptionsPolicy.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.azure_integration_policy_setting import AzureIntegrationPolicySetting

# TODO update the JSON string below
json = "{}"
# create an instance of AzureIntegrationPolicySetting from a JSON string
azure_integration_policy_setting_instance = AzureIntegrationPolicySetting.from_json(json)
# print the JSON string representation of the object
print(AzureIntegrationPolicySetting.to_json())

# convert the object into a dict
azure_integration_policy_setting_dict = azure_integration_policy_setting_instance.to_dict()
# create an instance of AzureIntegrationPolicySetting from a dict
azure_integration_policy_setting_from_dict = AzureIntegrationPolicySetting.from_dict(azure_integration_policy_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


