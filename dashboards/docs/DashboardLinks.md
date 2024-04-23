# DashboardLinks

A links object containing the self and the snapshots links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DashboardLinksLinks**](DashboardLinksLinks.md) |  | [optional] 

## Example

```python
from dashboards.models.dashboard_links import DashboardLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardLinks from a JSON string
dashboard_links_instance = DashboardLinks.from_json(json)
# print the JSON string representation of the object
print(DashboardLinks.to_json())

# convert the object into a dict
dashboard_links_dict = dashboard_links_instance.to_dict()
# create an instance of DashboardLinks from a dict
dashboard_links_from_dict = DashboardLinks.from_dict(dashboard_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


