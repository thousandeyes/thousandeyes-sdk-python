# SnapshotLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.snapshots.models.snapshot_links import SnapshotLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotLinks from a JSON string
snapshot_links_instance = SnapshotLinks.from_json(json)
# print the JSON string representation of the object
print(SnapshotLinks.to_json())

# convert the object into a dict
snapshot_links_dict = snapshot_links_instance.to_dict()
# create an instance of SnapshotLinks from a dict
snapshot_links_from_dict = SnapshotLinks.from_dict(snapshot_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


