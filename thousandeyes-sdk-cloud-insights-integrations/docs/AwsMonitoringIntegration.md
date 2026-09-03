# AwsMonitoringIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for the AWS inventory or flow logs monitoring integration. | 
**name** | **str** | The name of the AWS inventory or flow logs monitoring integration. | 
**role_arn** | **str** | The ARN of the AWS role to be monitored. | 
**external_id** | **str** | The external ID associated with the account group. | 
**monitoring_type** | **str** | The type of monitoring integration. | 
**sns_topics_arns** | **List[str]** | The array of SNS topic ARNs. Relevant only for flow logs monitoring integrations. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.aws_monitoring_integration import AwsMonitoringIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMonitoringIntegration from a JSON string
aws_monitoring_integration_instance = AwsMonitoringIntegration.from_json(json)
# print the JSON string representation of the object
print(AwsMonitoringIntegration.to_json())

# convert the object into a dict
aws_monitoring_integration_dict = aws_monitoring_integration_instance.to_dict()
# create an instance of AwsMonitoringIntegration from a dict
aws_monitoring_integration_from_dict = AwsMonitoringIntegration.from_dict(aws_monitoring_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


