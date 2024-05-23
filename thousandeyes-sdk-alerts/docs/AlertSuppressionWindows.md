# AlertSuppressionWindows

Alert suppression windows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_suppression_windows** | [**List[AlertSuppressionWindow]**](AlertSuppressionWindow.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_suppression_windows import AlertSuppressionWindows

# TODO update the JSON string below
json = "{}"
# create an instance of AlertSuppressionWindows from a JSON string
alert_suppression_windows_instance = AlertSuppressionWindows.from_json(json)
# print the JSON string representation of the object
print(AlertSuppressionWindows.to_json())

# convert the object into a dict
alert_suppression_windows_dict = alert_suppression_windows_instance.to_dict()
# create an instance of AlertSuppressionWindows from a dict
alert_suppression_windows_from_dict = AlertSuppressionWindows.from_dict(alert_suppression_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


