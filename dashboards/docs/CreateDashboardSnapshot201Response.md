# CreateDashboardSnapshot201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | Identifier of the dashboard snapshot. | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from dashboards.models.create_dashboard_snapshot201_response import CreateDashboardSnapshot201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardSnapshot201Response from a JSON string
create_dashboard_snapshot201_response_instance = CreateDashboardSnapshot201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardSnapshot201Response.to_json())

# convert the object into a dict
create_dashboard_snapshot201_response_dict = create_dashboard_snapshot201_response_instance.to_dict()
# create an instance of CreateDashboardSnapshot201Response from a dict
create_dashboard_snapshot201_response_from_dict = CreateDashboardSnapshot201Response.from_dict(create_dashboard_snapshot201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


