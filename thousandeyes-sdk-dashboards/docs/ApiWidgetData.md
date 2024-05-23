# ApiWidgetData

Response of a widget data request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_labels** | [**List[ApiReportDataComponentLabelMap]**](ApiReportDataComponentLabelMap.md) |  | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**data** | [**ApiWidgetsDataV2**](ApiWidgetsDataV2.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_widget_data import ApiWidgetData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidgetData from a JSON string
api_widget_data_instance = ApiWidgetData.from_json(json)
# print the JSON string representation of the object
print(ApiWidgetData.to_json())

# convert the object into a dict
api_widget_data_dict = api_widget_data_instance.to_dict()
# create an instance of ApiWidgetData from a dict
api_widget_data_from_dict = ApiWidgetData.from_dict(api_widget_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


