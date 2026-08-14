# CloneDashboardRequest

Optional values that override settings inherited from the source dashboard. Omit the request body or send an empty object (`{}`) to clone the dashboard without overrides.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the cloned dashboard. If omitted, the API generates a unique title. | [optional] 
**tag_ids** | **List[str]** | Dashboard tag identifiers. An empty array clears tags from the clone; omission preserves the source dashboard&#39;s tags. | [optional] 
**description** | **str** | Description for the cloned dashboard. | [optional] 
**layout** | [**DashboardLayout**](DashboardLayout.md) |  | [optional] 
**default_timespan** | [**DefaultTimespan**](DefaultTimespan.md) |  | [optional] 
**is_global_override** | **bool** | If &#x60;true&#x60;, the dashboard time range overrides local widget time settings. | [optional] 
**refresh_rate** | [**CloneDashboardRefreshRate**](CloneDashboardRefreshRate.md) |  | [optional] 
**global_filter_id** | **str** | Global filter applied to the cloned dashboard. If omitted, the source dashboard&#39;s filter is preserved when cloning within the same account group. When cloning across account groups, the filter is cleared. | [optional] 
**shared_account_ids** | **List[str]** | Account group IDs with which to share the cloned dashboard. An empty array limits sharing to current account group. Omission does not share with other account groups. The &#x60;isPrivate&#x60; setting controls visibility within the current account group. Cannot be used together with &#x60;isSharedWithAllAccountGroups&#x3D;true&#x60; | [optional] 
**is_shared_with_all_account_groups** | **bool** | When &#x60;true&#x60;, shares the cloned dashboard with all account groups available to the user. Cannot be used together with &#x60;sharedAccountIds&#x60;. | [optional] 
**is_private** | **bool** | When &#x60;true&#x60;, only the creator can view the cloned dashboard. Combining this property with &#x60;sharedAccountIds&#x60; or &#x60;isSharedWithAllAccountGroups&#x3D;true&#x60; returns &#x60;400 Bad Request&#x60;. Defaults to &#x60;false&#x60;. | [optional] [default to False]
**is_default_for_user** | **bool** | When &#x60;true&#x60;, sets the cloned dashboard as the current user&#39;s default dashboard. | [optional] 
**is_default_for_account** | **bool** | When &#x60;true&#x60;, sets the cloned dashboard as the current account group&#39;s default dashboard. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.clone_dashboard_request import CloneDashboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneDashboardRequest from a JSON string
clone_dashboard_request_instance = CloneDashboardRequest.from_json(json)
# print the JSON string representation of the object
print(CloneDashboardRequest.to_json())

# convert the object into a dict
clone_dashboard_request_dict = clone_dashboard_request_instance.to_dict()
# create an instance of CloneDashboardRequest from a dict
clone_dashboard_request_from_dict = CloneDashboardRequest.from_dict(clone_dashboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


