# AwsInventoryIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the AWS inventory monitoring integration. | 
**role_arn** | **str** | The ARN of the AWS role to be monitored. | 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.aws_inventory_integration_request import AwsInventoryIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsInventoryIntegrationRequest from a JSON string
aws_inventory_integration_request_instance = AwsInventoryIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(AwsInventoryIntegrationRequest.to_json())

# convert the object into a dict
aws_inventory_integration_request_dict = aws_inventory_integration_request_instance.to_dict()
# create an instance of AwsInventoryIntegrationRequest from a dict
aws_inventory_integration_request_from_dict = AwsInventoryIntegrationRequest.from_dict(aws_inventory_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


