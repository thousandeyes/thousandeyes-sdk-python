# ApiMultiMetricColumnData

The data presented within a single column of a Multi-Metric table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **str** | Identifier of the column. | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**points** | [**List[ApiWidgetDataPoint]**](ApiWidgetDataPoint.md) |  | [optional] 
**status** | **str** | Message for not fully configured card or no data. | [optional] 
**alert_suppression_windows** | [**List[ApiDashboardAsw]**](ApiDashboardAsw.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_multi_metric_column_data import ApiMultiMetricColumnData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMultiMetricColumnData from a JSON string
api_multi_metric_column_data_instance = ApiMultiMetricColumnData.from_json(json)
# print the JSON string representation of the object
print(ApiMultiMetricColumnData.to_json())

# convert the object into a dict
api_multi_metric_column_data_dict = api_multi_metric_column_data_instance.to_dict()
# create an instance of ApiMultiMetricColumnData from a dict
api_multi_metric_column_data_from_dict = ApiMultiMetricColumnData.from_dict(api_multi_metric_column_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


