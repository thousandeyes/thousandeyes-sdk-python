# AlertSuppressionWindows

Alert suppression windows.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_suppression_windows** | [**List[AlertSuppressionWindowsAlertSuppressionWindowsInner]**](AlertSuppressionWindowsAlertSuppressionWindowsInner.md) |  | [optional] 

## Example

```python
from alerts_api.models.alert_suppression_windows import AlertSuppressionWindows

# TODO update the JSON string below
json = "{}"
# create an instance of AlertSuppressionWindows from a JSON string
alert_suppression_windows_instance = AlertSuppressionWindows.from_json(json)
# print the JSON string representation of the object
print AlertSuppressionWindows.to_json()

# convert the object into a dict
alert_suppression_windows_dict = alert_suppression_windows_instance.to_dict()
# create an instance of AlertSuppressionWindows from a dict
alert_suppression_windows_form_dict = alert_suppression_windows.from_dict(alert_suppression_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


