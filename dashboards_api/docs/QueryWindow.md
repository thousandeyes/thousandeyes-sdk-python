# QueryWindow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 

## Example

```python
from dashboards_api.models.query_window import QueryWindow

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWindow from a JSON string
query_window_instance = QueryWindow.from_json(json)
# print the JSON string representation of the object
print QueryWindow.to_json()

# convert the object into a dict
query_window_dict = query_window_instance.to_dict()
# create an instance of QueryWindow from a dict
query_window_form_dict = query_window.from_dict(query_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


