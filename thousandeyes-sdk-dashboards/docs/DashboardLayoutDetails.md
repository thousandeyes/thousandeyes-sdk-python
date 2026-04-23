# DashboardLayoutDetails

Layout details including widget positioning.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_positioning** | [**List[WidgetPosition]**](WidgetPosition.md) | List of widget positions within the layout. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_layout_details import DashboardLayoutDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardLayoutDetails from a JSON string
dashboard_layout_details_instance = DashboardLayoutDetails.from_json(json)
# print the JSON string representation of the object
print(DashboardLayoutDetails.to_json())

# convert the object into a dict
dashboard_layout_details_dict = dashboard_layout_details_instance.to_dict()
# create an instance of DashboardLayoutDetails from a dict
dashboard_layout_details_from_dict = DashboardLayoutDetails.from_dict(dashboard_layout_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


