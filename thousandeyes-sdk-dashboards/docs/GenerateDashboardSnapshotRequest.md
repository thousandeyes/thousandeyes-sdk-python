# GenerateDashboardSnapshotRequest

Request to generate a snapshot from a dashboard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Date and time to start aggregating data (ISO date-time format). | [optional] 
**end_date** | **datetime** | Date and time to end aggregating data (ISO date-time format). | [optional] 
**display_name** | **str** | The name of the snapshot, does not have to be unique. | [optional] 
**dashboard_id** | **str** | TheIdentifierof the dashboard to generate a snapshot from | [optional] 
**anonymize_data** | **bool** | Set to &#x60;true&#x60; to anonymize the data in the snapshot. | [optional] 
**timezone** | **str** | Specifies the timezone used for date and time fields. | [optional] 
**expiration_date** | **datetime** | Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date and adhere to the ISO date-time format. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.generate_dashboard_snapshot_request import GenerateDashboardSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDashboardSnapshotRequest from a JSON string
generate_dashboard_snapshot_request_instance = GenerateDashboardSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateDashboardSnapshotRequest.to_json())

# convert the object into a dict
generate_dashboard_snapshot_request_dict = generate_dashboard_snapshot_request_instance.to_dict()
# create an instance of GenerateDashboardSnapshotRequest from a dict
generate_dashboard_snapshot_request_from_dict = GenerateDashboardSnapshotRequest.from_dict(generate_dashboard_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


