# ApiWidgetDataResponse

Response of a widget data request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_labels** | [**List[ApiReportDataComponentLabelMap]**](ApiReportDataComponentLabelMap.md) |  | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**data** | [**ApiWidgetsDataV2**](ApiWidgetsDataV2.md) |  | [optional] 

## Example

```python
from dashboards.models.api_widget_data_response import ApiWidgetDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidgetDataResponse from a JSON string
api_widget_data_response_instance = ApiWidgetDataResponse.from_json(json)
# print the JSON string representation of the object
print(ApiWidgetDataResponse.to_json())

# convert the object into a dict
api_widget_data_response_dict = api_widget_data_response_instance.to_dict()
# create an instance of ApiWidgetDataResponse from a dict
api_widget_data_response_from_dict = ApiWidgetDataResponse.from_dict(api_widget_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


