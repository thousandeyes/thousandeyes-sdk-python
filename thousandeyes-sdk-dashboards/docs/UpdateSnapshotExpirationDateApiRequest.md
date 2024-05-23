# UpdateSnapshotExpirationDateApiRequest

Request to update the expiration date of a snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_expiration_date** | **datetime** | Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date and adhere to the ISO date-time format. | [optional] 
**expiration_date** | **str** | Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.update_snapshot_expiration_date_api_request import UpdateSnapshotExpirationDateApiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotExpirationDateApiRequest from a JSON string
update_snapshot_expiration_date_api_request_instance = UpdateSnapshotExpirationDateApiRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotExpirationDateApiRequest.to_json())

# convert the object into a dict
update_snapshot_expiration_date_api_request_dict = update_snapshot_expiration_date_api_request_instance.to_dict()
# create an instance of UpdateSnapshotExpirationDateApiRequest from a dict
update_snapshot_expiration_date_api_request_from_dict = UpdateSnapshotExpirationDateApiRequest.from_dict(update_snapshot_expiration_date_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


