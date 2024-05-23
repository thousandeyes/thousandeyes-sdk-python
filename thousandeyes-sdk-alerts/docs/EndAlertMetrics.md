# EndAlertMetrics

String representation of the metric or metrics being considered in the alert rule at the point that the alert was cleared.  If the alert is not yet cleared, this field reflects the last round of data gathered from the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.end_alert_metrics import EndAlertMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of EndAlertMetrics from a JSON string
end_alert_metrics_instance = EndAlertMetrics.from_json(json)
# print the JSON string representation of the object
print(EndAlertMetrics.to_json())

# convert the object into a dict
end_alert_metrics_dict = end_alert_metrics_instance.to_dict()
# create an instance of EndAlertMetrics from a dict
end_alert_metrics_from_dict = EndAlertMetrics.from_dict(end_alert_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


