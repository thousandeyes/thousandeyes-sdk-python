# AlertIntegrationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | Unique ID of the integration. | [optional] 
**integration_name** | **str** | Name of the integration. | [optional] 
**integration_type** | [**AlertIntegrationType**](AlertIntegrationType.md) |  | [optional] 
**target** | **str** | Target URL of the integration. | [optional] 
**auth_method** | **str** | (PagerDuty only) Authentication method. | [optional] 
**auth_user** | **str** | (PagerDuty only) Authentication user. | [optional] 
**auth_token** | **str** | (PagerDuty only) Authentication token. | [optional] 
**channel** | **str** | (Slack only) Slack &#x60;#channel&#x60; or &#x60;@user&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.alert_integration_base import AlertIntegrationBase

# TODO update the JSON string below
json = "{}"
# create an instance of AlertIntegrationBase from a JSON string
alert_integration_base_instance = AlertIntegrationBase.from_json(json)
# print the JSON string representation of the object
print(AlertIntegrationBase.to_json())

# convert the object into a dict
alert_integration_base_dict = alert_integration_base_instance.to_dict()
# create an instance of AlertIntegrationBase from a dict
alert_integration_base_from_dict = AlertIntegrationBase.from_dict(alert_integration_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


