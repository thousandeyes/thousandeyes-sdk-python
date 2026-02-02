# WebhookOperations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebhookOperation]**](WebhookOperation.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.webhook_operations import WebhookOperations

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOperations from a JSON string
webhook_operations_instance = WebhookOperations.from_json(json)
# print the JSON string representation of the object
print(WebhookOperations.to_json())

# convert the object into a dict
webhook_operations_dict = webhook_operations_instance.to_dict()
# create an instance of WebhookOperations from a dict
webhook_operations_from_dict = WebhookOperations.from_dict(webhook_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


