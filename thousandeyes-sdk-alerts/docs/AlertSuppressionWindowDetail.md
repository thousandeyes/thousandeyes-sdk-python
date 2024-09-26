# AlertSuppressionWindowDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_suppression_window_id** | **str** | Unique ID of the alert suppression window. | [optional] [readonly] 
**name** | **str** | Name of the alert suppression window. | [optional] 
**is_enabled** | **bool** | Set to &#x60;false&#x60; for &#x60;disabled&#x60;, &#x60;true&#x60; for &#x60;enabled&#x60;. | [optional] 
**status** | [**AlertSuppressionWindowState**](AlertSuppressionWindowState.md) |  | [optional] 
**start_date** | **datetime** | The date/time when the alert suppression window starts (ISO date-time format). | [optional] 
**duration** | **int** | Duration in seconds the suppression window is active. | [optional] 
**repeat** | [**Repeat**](Repeat.md) |  | [optional] 
**end_repeat** | [**EndRepeat**](EndRepeat.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 
**tests** | [**List[SimpleTest]**](SimpleTest.md) | List of tests assigned to the alert suppression window. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_suppression_window_detail import AlertSuppressionWindowDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AlertSuppressionWindowDetail from a JSON string
alert_suppression_window_detail_instance = AlertSuppressionWindowDetail.from_json(json)
# print the JSON string representation of the object
print(AlertSuppressionWindowDetail.to_json())

# convert the object into a dict
alert_suppression_window_detail_dict = alert_suppression_window_detail_instance.to_dict()
# create an instance of AlertSuppressionWindowDetail from a dict
alert_suppression_window_detail_from_dict = AlertSuppressionWindowDetail.from_dict(alert_suppression_window_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


