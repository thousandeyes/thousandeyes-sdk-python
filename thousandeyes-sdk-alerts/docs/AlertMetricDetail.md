# AlertMetricDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | [**EndAlertMetrics**](EndAlertMetrics.md) |  | [optional] 
**id** | **str** | Unique metric detail id. | [optional] 
**name** | **str** | Geolocation of the alert. | [optional] 
**start** | [**StartAlertMetrics**](StartAlertMetrics.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**type** | **str** | Type of the alert metric. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_metric_detail import AlertMetricDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AlertMetricDetail from a JSON string
alert_metric_detail_instance = AlertMetricDetail.from_json(json)
# print the JSON string representation of the object
print(AlertMetricDetail.to_json())

# convert the object into a dict
alert_metric_detail_dict = alert_metric_detail_instance.to_dict()
# create an instance of AlertMetricDetail from a dict
alert_metric_detail_from_dict = AlertMetricDetail.from_dict(alert_metric_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


