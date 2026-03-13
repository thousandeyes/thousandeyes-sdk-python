# WebhookOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**category** | [**OperationCategory**](OperationCategory.md) |  | 
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**path** | **str** |  | [optional] 
**payload** | **str** | Handlebars template for the payload. | [optional] 
**headers** | [**List[Header]**](Header.md) |  | [optional] 
**var_query_params** | **str** | Handlebars template for the query params. Most compile into a proper JSON object where each object property will define the query param name and the object property value define the corresponding query param value. | [optional] 
**type** | [**OperationType**](OperationType.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.webhook_operation import WebhookOperation

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOperation from a JSON string
webhook_operation_instance = WebhookOperation.from_json(json)
# print the JSON string representation of the object
print(WebhookOperation.to_json())

# convert the object into a dict
webhook_operation_dict = webhook_operation_instance.to_dict()
# create an instance of WebhookOperation from a dict
webhook_operation_from_dict = WebhookOperation.from_dict(webhook_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


