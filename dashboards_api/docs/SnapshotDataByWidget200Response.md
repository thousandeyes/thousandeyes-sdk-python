# SnapshotDataByWidget200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_labels** | [**List[ApiReportDataComponentLabelMap]**](ApiReportDataComponentLabelMap.md) |  | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**data** | [**ApiWidgetsDataV2**](ApiWidgetsDataV2.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from dashboards_api.models.snapshot_data_by_widget200_response import SnapshotDataByWidget200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDataByWidget200Response from a JSON string
snapshot_data_by_widget200_response_instance = SnapshotDataByWidget200Response.from_json(json)
# print the JSON string representation of the object
print SnapshotDataByWidget200Response.to_json()

# convert the object into a dict
snapshot_data_by_widget200_response_dict = snapshot_data_by_widget200_response_instance.to_dict()
# create an instance of SnapshotDataByWidget200Response from a dict
snapshot_data_by_widget200_response_form_dict = snapshot_data_by_widget200_response.from_dict(snapshot_data_by_widget200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


