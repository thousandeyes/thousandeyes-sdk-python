# TargetNetworkEventDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each event. | [optional] [readonly] 
**type_name** | **str** | Event type name. Examples include, Local Agent Issue, Network Path Issue, Network Outage, DNS Issue, Server Issue, and Proxy Issue. | [optional] [readonly] 
**state** | [**EventState**](EventState.md) |  | [optional] 
**start_date** | **datetime** | The start date and time (in UTC, ISO 8601 format) when the event was first detected. | [optional] [readonly] 
**end_date** | **datetime** | The end date and time (in UTC, ISO 8601 format) when the event was resolved (due to timeout). This value is populated for \&quot;ongoing\&quot; events. | [optional] [readonly] 
**severity** | [**EventAlertSeverity**](EventAlertSeverity.md) |  | [optional] 
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**summary** | **str** | A brief summary describing the cause of the event. | [optional] [readonly] 
**affected_tests** | [**AffectedTests**](AffectedTests.md) |  | [optional] 
**affected_targets** | [**AffectedTargets**](AffectedTargets.md) |  | [optional] 
**affected_agents** | [**AffectedAgents**](AffectedAgents.md) |  | [optional] 
**cause** | **List[str]** | The cause of the error. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 
**type** | **str** | Target network event type. | 
**grouping** | [**TargetNetworkEventGrouping**](TargetNetworkEventGrouping.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.target_network_event_detail import TargetNetworkEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TargetNetworkEventDetail from a JSON string
target_network_event_detail_instance = TargetNetworkEventDetail.from_json(json)
# print the JSON string representation of the object
print(TargetNetworkEventDetail.to_json())

# convert the object into a dict
target_network_event_detail_dict = target_network_event_detail_instance.to_dict()
# create an instance of TargetNetworkEventDetail from a dict
target_network_event_detail_from_dict = TargetNetworkEventDetail.from_dict(target_network_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


