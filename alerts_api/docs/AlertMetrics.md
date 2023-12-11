# AlertMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **str** |  | [optional] 

## Example

```python
from alerts_api.models.alert_metrics import AlertMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of AlertMetrics from a JSON string
alert_metrics_instance = AlertMetrics.from_json(json)
# print the JSON string representation of the object
print AlertMetrics.to_json()

# convert the object into a dict
alert_metrics_dict = alert_metrics_instance.to_dict()
# create an instance of AlertMetrics from a dict
alert_metrics_form_dict = alert_metrics.from_dict(alert_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


