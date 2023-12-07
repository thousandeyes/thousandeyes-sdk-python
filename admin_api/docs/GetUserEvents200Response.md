# GetUserEvents200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**audit_events** | [**List[UserEvent]**](UserEvent.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin_api.models.get_user_events200_response import GetUserEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserEvents200Response from a JSON string
get_user_events200_response_instance = GetUserEvents200Response.from_json(json)
# print the JSON string representation of the object
print GetUserEvents200Response.to_json()

# convert the object into a dict
get_user_events200_response_dict = get_user_events200_response_instance.to_dict()
# create an instance of GetUserEvents200Response from a dict
get_user_events200_response_form_dict = get_user_events200_response.from_dict(get_user_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


