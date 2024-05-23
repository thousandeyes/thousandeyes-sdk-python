# ApiReportDataComponentLabelMap

Map of group labels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_property** | **str** | Defines the criterion used to aggregate data points under specific group values. | [optional] 
**group_labels** | [**List[ApiReportDataComponentLabelMapEntry]**](ApiReportDataComponentLabelMapEntry.md) | List of group labels. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_report_data_component_label_map import ApiReportDataComponentLabelMap

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReportDataComponentLabelMap from a JSON string
api_report_data_component_label_map_instance = ApiReportDataComponentLabelMap.from_json(json)
# print the JSON string representation of the object
print(ApiReportDataComponentLabelMap.to_json())

# convert the object into a dict
api_report_data_component_label_map_dict = api_report_data_component_label_map_instance.to_dict()
# create an instance of ApiReportDataComponentLabelMap from a dict
api_report_data_component_label_map_from_dict = ApiReportDataComponentLabelMap.from_dict(api_report_data_component_label_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


