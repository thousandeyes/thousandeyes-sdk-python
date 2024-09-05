# Alert


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
**alert_id** | **str** | A unique ID for each individual alert occurrence. | [optional] [readonly] 
**date_start** | **str** | The start date and time for querying alerts. | [optional] [readonly] 
**date_end** | **str** | The end date and time for querying alerts. | [optional] [readonly] 
**rule_id** | **int** | Unique ID of the rule. | [optional] [readonly] 
**state** | **str** | Current state of the alert. Possible values: clear or trigger. | [optional] [readonly] 
**severity** | **str** | The severity of the alert. | [optional] 
**permalink** | **str** | Hyperlink to alerts list, with row expanded | [optional] 
**api_links** | **List[Dict[str, object]]** | List of hyperlinks to other areas of the API | [optional] 
**alert_rule_id** | **str** | Unique ID of the rule. | [optional] [readonly] 
**alert_state** | [**State**](State.md) |  | [optional] 
**alert_severity** | [**Severity**](Severity.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


