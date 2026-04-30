# DashboardLayout

Dashboard layout configuration for arranging widgets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout_id** | **str** | Unique identifier for the layout. | [optional] 
**type** | [**DashboardLayoutType**](DashboardLayoutType.md) |  | 
**details** | [**DashboardLayoutDetails**](DashboardLayoutDetails.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_layout import DashboardLayout

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardLayout from a JSON string
dashboard_layout_instance = DashboardLayout.from_json(json)
# print the JSON string representation of the object
print(DashboardLayout.to_json())

# convert the object into a dict
dashboard_layout_dict = dashboard_layout_instance.to_dict()
# create an instance of DashboardLayout from a dict
dashboard_layout_from_dict = DashboardLayout.from_dict(dashboard_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


