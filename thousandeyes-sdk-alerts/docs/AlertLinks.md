# AlertLinks

An object containing the alert links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | [**Link**](Link.md) |  | [optional] 
**rule** | [**Link**](Link.md) |  | [optional] 
**app_link** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_links import AlertLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertLinks from a JSON string
alert_links_instance = AlertLinks.from_json(json)
# print the JSON string representation of the object
print(AlertLinks.to_json())

# convert the object into a dict
alert_links_dict = alert_links_instance.to_dict()
# create an instance of AlertLinks from a dict
alert_links_from_dict = AlertLinks.from_dict(alert_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


