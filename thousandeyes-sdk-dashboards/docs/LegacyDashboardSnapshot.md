# LegacyDashboardSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Identifier of the account group that the snapshot belongs to. | [optional] 
**created_date** | **str** | UTC date when dashboard snapshot was created. | [optional] 
**expiration_date** | **str** | Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date. | [optional] 
**permalink** | **str** | Hyperlink to dashboard snapshot in ThousandEyes Application | [optional] 
**api_links** | **List[Dict[str, object]]** | A links array containing the self link. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.legacy_dashboard_snapshot import LegacyDashboardSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDashboardSnapshot from a JSON string
legacy_dashboard_snapshot_instance = LegacyDashboardSnapshot.from_json(json)
# print the JSON string representation of the object
print(LegacyDashboardSnapshot.to_json())

# convert the object into a dict
legacy_dashboard_snapshot_dict = legacy_dashboard_snapshot_instance.to_dict()
# create an instance of LegacyDashboardSnapshot from a dict
legacy_dashboard_snapshot_from_dict = LegacyDashboardSnapshot.from_dict(legacy_dashboard_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


