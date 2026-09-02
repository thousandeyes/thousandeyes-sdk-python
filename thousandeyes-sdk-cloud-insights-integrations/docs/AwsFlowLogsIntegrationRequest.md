# AwsFlowLogsIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the AWS flow logs monitoring integration. | 
**role_arn** | **str** | The ARN of the AWS role to be monitored. | 
**sns_topics_arns** | **List[str]** | The array of SNS topics ARNs. | 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.aws_flow_logs_integration_request import AwsFlowLogsIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsFlowLogsIntegrationRequest from a JSON string
aws_flow_logs_integration_request_instance = AwsFlowLogsIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(AwsFlowLogsIntegrationRequest.to_json())

# convert the object into a dict
aws_flow_logs_integration_request_dict = aws_flow_logs_integration_request_instance.to_dict()
# create an instance of AwsFlowLogsIntegrationRequest from a dict
aws_flow_logs_integration_request_from_dict = AwsFlowLogsIntegrationRequest.from_dict(aws_flow_logs_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


