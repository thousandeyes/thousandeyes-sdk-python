# AuditUserEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_events** | [**List[UserEvent]**](UserEvent.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.audit_user_events import AuditUserEvents

# TODO update the JSON string below
json = "{}"
# create an instance of AuditUserEvents from a JSON string
audit_user_events_instance = AuditUserEvents.from_json(json)
# print the JSON string representation of the object
print(AuditUserEvents.to_json())

# convert the object into a dict
audit_user_events_dict = audit_user_events_instance.to_dict()
# create an instance of AuditUserEvents from a dict
audit_user_events_from_dict = AuditUserEvents.from_dict(audit_user_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


