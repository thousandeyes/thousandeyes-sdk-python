# AwsIntegrationPolicySetting

AWS integration policy configuration that controls which resource groups and regions ThousandEyes inventories, and whether CloudTrail is enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_resource_group_types** | [**List[AwsResourceGroupType]**](AwsResourceGroupType.md) | The set of AWS resource group types included in inventory monitoring. | 
**enabled_regions** | [**List[AwsRegion]**](AwsRegion.md) | The AWS regions that ThousandEyes inventories for the account group. | 
**enabled_cloudtrail** | **bool** | Indicates whether CloudTrail integration is enabled for AWS inventory monitoring. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.aws_integration_policy_setting import AwsIntegrationPolicySetting

# TODO update the JSON string below
json = "{}"
# create an instance of AwsIntegrationPolicySetting from a JSON string
aws_integration_policy_setting_instance = AwsIntegrationPolicySetting.from_json(json)
# print the JSON string representation of the object
print(AwsIntegrationPolicySetting.to_json())

# convert the object into a dict
aws_integration_policy_setting_dict = aws_integration_policy_setting_instance.to_dict()
# create an instance of AwsIntegrationPolicySetting from a dict
aws_integration_policy_setting_from_dict = AwsIntegrationPolicySetting.from_dict(aws_integration_policy_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


