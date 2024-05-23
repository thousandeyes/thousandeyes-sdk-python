# ApiWidgetDataSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_labels** | [**List[ApiReportDataComponentLabelMap]**](ApiReportDataComponentLabelMap.md) |  | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**data** | [**ApiWidgetsDataV2**](ApiWidgetsDataV2.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_widget_data_snapshot_response import ApiWidgetDataSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidgetDataSnapshotResponse from a JSON string
api_widget_data_snapshot_response_instance = ApiWidgetDataSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(ApiWidgetDataSnapshotResponse.to_json())

# convert the object into a dict
api_widget_data_snapshot_response_dict = api_widget_data_snapshot_response_instance.to_dict()
# create an instance of ApiWidgetDataSnapshotResponse from a dict
api_widget_data_snapshot_response_from_dict = ApiWidgetDataSnapshotResponse.from_dict(api_widget_data_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


