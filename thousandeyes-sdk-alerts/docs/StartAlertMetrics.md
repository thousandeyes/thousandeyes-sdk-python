# StartAlertMetrics

String representation of the metric at the time that the source began alerting.   Note that the alert `start` and `startDate` for a particular source do not need to be the same,  as sources may change alerting status throughout an alert's lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.start_alert_metrics import StartAlertMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of StartAlertMetrics from a JSON string
start_alert_metrics_instance = StartAlertMetrics.from_json(json)
# print the JSON string representation of the object
print(StartAlertMetrics.to_json())

# convert the object into a dict
start_alert_metrics_dict = start_alert_metrics_instance.to_dict()
# create an instance of StartAlertMetrics from a dict
start_alert_metrics_from_dict = StartAlertMetrics.from_dict(start_alert_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


