# UserEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_events** | [**List[UserEvent]**](UserEvent.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.admin.models.user_events import UserEvents

# TODO update the JSON string below
json = "{}"
# create an instance of UserEvents from a JSON string
user_events_instance = UserEvents.from_json(json)
# print the JSON string representation of the object
print(UserEvents.to_json())

# convert the object into a dict
user_events_dict = user_events_instance.to_dict()
# create an instance of UserEvents from a dict
user_events_from_dict = UserEvents.from_dict(user_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


