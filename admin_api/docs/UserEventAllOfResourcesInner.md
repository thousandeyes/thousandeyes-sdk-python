# UserEventAllOfResourcesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of resource affected. Can be “testName”, “reportTitle”, “userDisplayName”, “alertRuleName”, etc. | [optional] 
**name** | **str** | Name of the affected resource. | [optional] 

## Example

```python
from admin_api.models.user_event_all_of_resources_inner import UserEventAllOfResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventAllOfResourcesInner from a JSON string
user_event_all_of_resources_inner_instance = UserEventAllOfResourcesInner.from_json(json)
# print the JSON string representation of the object
print UserEventAllOfResourcesInner.to_json()

# convert the object into a dict
user_event_all_of_resources_inner_dict = user_event_all_of_resources_inner_instance.to_dict()
# create an instance of UserEventAllOfResourcesInner from a dict
user_event_all_of_resources_inner_form_dict = user_event_all_of_resources_inner.from_dict(user_event_all_of_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


