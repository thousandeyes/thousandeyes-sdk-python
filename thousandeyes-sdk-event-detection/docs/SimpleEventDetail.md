# SimpleEventDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each event. | [optional] [readonly] 
**type_name** | **str** | Event type name. Examples include, Local Agent Issue, Network Path Issue, Network Outage, DNS Issue, Server Issue, and Proxy Issue. | [optional] [readonly] 
**state** | [**EventState**](EventState.md) |  | [optional] 
**start_date** | **datetime** | The start date and time (in UTC, ISO 8601 format) when the event was first detected. | [optional] [readonly] 
**end_date** | **datetime** | The end date and time (in UTC, ISO 8601 format) when the event was resolved (due to timeout). This value is populated for \&quot;ongoing\&quot; events. | [optional] [readonly] 
**severity** | [**EventAlertSeverity**](EventAlertSeverity.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.simple_event_detail import SimpleEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleEventDetail from a JSON string
simple_event_detail_instance = SimpleEventDetail.from_json(json)
# print the JSON string representation of the object
print(SimpleEventDetail.to_json())

# convert the object into a dict
simple_event_detail_dict = simple_event_detail_instance.to_dict()
# create an instance of SimpleEventDetail from a dict
simple_event_detail_from_dict = SimpleEventDetail.from_dict(simple_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


