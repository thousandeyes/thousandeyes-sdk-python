# LegacyApiDashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Identifier for the account group associated with a dashboard. | [optional] [readonly] 
**created_by** | **int** | Identifier for the user that created a dashboard. | [optional] [readonly] 
**modified_by** | **int** | Identifier for the user that last modified a dashboard. | [optional] [readonly] 
**modified_date** | **str** | UTC date/time when a dashboard was last modified. | [optional] [readonly] 
**global_override** | **bool** | When set to &#x60;true&#x60;, the defaultTimespan is used and overrides the widget&#39;s timespan. If set to &#x60;false&#x60;, the the widget&#39;s timespan is used. | [optional] 
**migrated_report** | **bool** | True if this dashboard was previously a report. | [optional] [readonly] 
**api_link** | **List[Dict[str, object]]** | A links array containing the self and the snapshots links. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.legacy_api_dashboard import LegacyApiDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyApiDashboard from a JSON string
legacy_api_dashboard_instance = LegacyApiDashboard.from_json(json)
# print the JSON string representation of the object
print(LegacyApiDashboard.to_json())

# convert the object into a dict
legacy_api_dashboard_dict = legacy_api_dashboard_instance.to_dict()
# create an instance of LegacyApiDashboard from a dict
legacy_api_dashboard_from_dict = LegacyApiDashboard.from_dict(legacy_api_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


