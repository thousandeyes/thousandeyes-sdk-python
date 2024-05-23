# AlertSuppressionWindowRequest


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
**tests** | **List[str]** | List of tests to assign to the alert suppression window. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_suppression_window_request import AlertSuppressionWindowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlertSuppressionWindowRequest from a JSON string
alert_suppression_window_request_instance = AlertSuppressionWindowRequest.from_json(json)
# print the JSON string representation of the object
print(AlertSuppressionWindowRequest.to_json())

# convert the object into a dict
alert_suppression_window_request_dict = alert_suppression_window_request_instance.to_dict()
# create an instance of AlertSuppressionWindowRequest from a dict
alert_suppression_window_request_from_dict = AlertSuppressionWindowRequest.from_dict(alert_suppression_window_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


