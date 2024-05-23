# ApiReportDataComponentLabelMapEntry

Represents a mapping entry of a group label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Identifier of the group. | [optional] 
**group_label** | **str** | Label of the group. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_report_data_component_label_map_entry import ApiReportDataComponentLabelMapEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReportDataComponentLabelMapEntry from a JSON string
api_report_data_component_label_map_entry_instance = ApiReportDataComponentLabelMapEntry.from_json(json)
# print the JSON string representation of the object
print(ApiReportDataComponentLabelMapEntry.to_json())

# convert the object into a dict
api_report_data_component_label_map_entry_dict = api_report_data_component_label_map_entry_instance.to_dict()
# create an instance of ApiReportDataComponentLabelMapEntry from a dict
api_report_data_component_label_map_entry_from_dict = ApiReportDataComponentLabelMapEntry.from_dict(api_report_data_component_label_map_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


