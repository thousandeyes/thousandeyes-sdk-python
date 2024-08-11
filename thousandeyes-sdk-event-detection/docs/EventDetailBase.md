# EventDetailBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each event. | [optional] [readonly] 
**type_name** | **str** | Event type name. Examples include, Local Agent Issue, Network Path Issue, Network Outage, DNS Issue, Server Issue, and Proxy Issue. | [optional] [readonly] 
**state** | [**EventState**](EventState.md) |  | [optional] 
**start_date** | **datetime** | The start date and time (in UTC, ISO 8601 format) when the event was first detected. | [optional] [readonly] 
**end_date** | **datetime** | The end date and time (in UTC, ISO 8601 format) when the event was resolved (due to timeout). This value is populated for \&quot;ongoing\&quot; events. | [optional] [readonly] 
**severity** | [**Severity**](Severity.md) |  | [optional] 
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**summary** | **str** | A brief summary describing the cause of the event. | [optional] [readonly] 
**affected_tests** | [**AffectedTests**](AffectedTests.md) |  | [optional] 
**affected_targets** | [**AffectedTargets**](AffectedTargets.md) |  | [optional] 
**affected_agents** | [**AffectedAgents**](AffectedAgents.md) |  | [optional] 
**cause** | **List[str]** | The cause of the error. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.event_detail_base import EventDetailBase

# TODO update the JSON string below
json = "{}"
# create an instance of EventDetailBase from a JSON string
event_detail_base_instance = EventDetailBase.from_json(json)
# print the JSON string representation of the object
print(EventDetailBase.to_json())

# convert the object into a dict
event_detail_base_dict = event_detail_base_instance.to_dict()
# create an instance of EventDetailBase from a dict
event_detail_base_from_dict = EventDetailBase.from_dict(event_detail_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


