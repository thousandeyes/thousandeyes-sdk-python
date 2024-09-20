# AlertDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each individual alert occurrence. | [optional] [readonly] 
**alert_type** | [**AlertType**](AlertType.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**violation_count** | **int** | Number of sources that meet the alert criteria. | [optional] 
**duration** | **int** | Duration in seconds the alert was active | [optional] 
**suppressed** | **bool** | Indicates whether the alert is currently suppressed by a real-time ASW. | [optional] 
**meta** | [**AlertMeta**](AlertMeta.md) |  | [optional] 
**links** | [**AlertLinks**](AlertLinks.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 
**details** | [**List[AlertMetricDetail]**](AlertMetricDetail.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_detail import AlertDetail

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


