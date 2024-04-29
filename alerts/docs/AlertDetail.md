# AlertDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each individual alert occurrence. | [optional] [readonly] 
**alert_type** | [**AlertType**](AlertType.md) |  | [optional] 
**start_date** | **datetime** | The start date and time (in UTC, ISO 8601 format) for querying alerts. | [optional] [readonly] 
**end_date** | **datetime** | The end date and time (in UTC, ISO 8601 format) for querying alerts. | [optional] [readonly] 
**violation_count** | **int** | Number of sources that meet the alert criteria. | [optional] 
**duration** | **float** | Duration in seconds the alert was active | [optional] 
**suppressed** | **bool** | Indicates whether the alert is currently suppressed by a real-time ASW. | [optional] 
**meta** | [**BaseAlertAllOfMeta**](BaseAlertAllOfMeta.md) |  | [optional] 
**links** | [**AlertLinksLinks**](AlertLinksLinks.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 
**details** | [**List[AlertMetricDetail]**](AlertMetricDetail.md) |  | [optional] 

## Example

```python
from alerts.models.alert_detail import AlertDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AlertDetail from a JSON string
alert_detail_instance = AlertDetail.from_json(json)
# print the JSON string representation of the object
print(AlertDetail.to_json())

# convert the object into a dict
alert_detail_dict = alert_detail_instance.to_dict()
# create an instance of AlertDetail from a dict
alert_detail_from_dict = AlertDetail.from_dict(alert_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

