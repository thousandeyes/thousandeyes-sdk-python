# AwsMonitoringIntegrations

A HAL resource containing a list of AWS monitoring integrations and navigation links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[AwsMonitoringIntegration]**](AwsMonitoringIntegration.md) | The list of AWS inventory and flow logs monitoring integrations. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.aws_monitoring_integrations import AwsMonitoringIntegrations

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMonitoringIntegrations from a JSON string
aws_monitoring_integrations_instance = AwsMonitoringIntegrations.from_json(json)
# print the JSON string representation of the object
print(AwsMonitoringIntegrations.to_json())

# convert the object into a dict
aws_monitoring_integrations_dict = aws_monitoring_integrations_instance.to_dict()
# create an instance of AwsMonitoringIntegrations from a dict
aws_monitoring_integrations_from_dict = AwsMonitoringIntegrations.from_dict(aws_monitoring_integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


