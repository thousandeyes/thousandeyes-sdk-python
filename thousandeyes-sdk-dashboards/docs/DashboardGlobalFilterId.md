# DashboardGlobalFilterId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_filter_id** | **str** | Default global dashboard filter ID (obtained from &#x60;/dashboards/filters&#x60; endpoint). | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_global_filter_id import DashboardGlobalFilterId

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardGlobalFilterId from a JSON string
dashboard_global_filter_id_instance = DashboardGlobalFilterId.from_json(json)
# print the JSON string representation of the object
print(DashboardGlobalFilterId.to_json())

# convert the object into a dict
dashboard_global_filter_id_dict = dashboard_global_filter_id_instance.to_dict()
# create an instance of DashboardGlobalFilterId from a dict
dashboard_global_filter_id_from_dict = DashboardGlobalFilterId.from_dict(dashboard_global_filter_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


