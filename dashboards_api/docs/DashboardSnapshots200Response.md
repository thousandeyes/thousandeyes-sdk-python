# DashboardSnapshots200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_snapshots** | [**List[ApiDashboardSnapshot]**](ApiDashboardSnapshot.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from dashboards_api.models.dashboard_snapshots200_response import DashboardSnapshots200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSnapshots200Response from a JSON string
dashboard_snapshots200_response_instance = DashboardSnapshots200Response.from_json(json)
# print the JSON string representation of the object
print DashboardSnapshots200Response.to_json()

# convert the object into a dict
dashboard_snapshots200_response_dict = dashboard_snapshots200_response_instance.to_dict()
# create an instance of DashboardSnapshots200Response from a dict
dashboard_snapshots200_response_form_dict = dashboard_snapshots200_response.from_dict(dashboard_snapshots200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


