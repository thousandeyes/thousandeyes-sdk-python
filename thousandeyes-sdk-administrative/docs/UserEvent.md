# UserEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**account_group_name** | **str** | Account group name | [optional] 
**var_date** | **datetime** | UTC event date (ISO date-time format). | [optional] 
**event** | **str** | Event type. | [optional] 
**ip_address** | **str** | Source IP address of the user. | [optional] 
**uid** | **str** | Unique id representing the user. | [optional] 
**user** | **str** | The name and email address of the user. | [optional] 
**resources** | [**List[Resource]**](Resource.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.user_event import UserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserEvent from a JSON string
user_event_instance = UserEvent.from_json(json)
# print the JSON string representation of the object
print(UserEvent.to_json())

# convert the object into a dict
user_event_dict = user_event_instance.to_dict()
# create an instance of UserEvent from a dict
user_event_from_dict = UserEvent.from_dict(user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


