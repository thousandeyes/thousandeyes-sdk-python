# ApiDashboardAsw

Alert suppression window shown in a widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the alert suppression window. | [optional] 
**name** | **str** | Name of the alert suppression window. | [optional] 
**test_ids** | **List[str]** |  | [optional] 
**start_times** | **List[datetime]** |  | [optional] 
**duration_in_seconds** | **int** |  | [optional] 
**repeat** | [**AswRepeat**](AswRepeat.md) |  | [optional] 
**repeat_every** | **int** |  | [optional] 
**repeat_unit** | [**AswRepeatUnit**](AswRepeatUnit.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_dashboard_asw import ApiDashboardAsw

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDashboardAsw from a JSON string
api_dashboard_asw_instance = ApiDashboardAsw.from_json(json)
# print the JSON string representation of the object
print(ApiDashboardAsw.to_json())

# convert the object into a dict
api_dashboard_asw_dict = api_dashboard_asw_instance.to_dict()
# create an instance of ApiDashboardAsw from a dict
api_dashboard_asw_from_dict = ApiDashboardAsw.from_dict(api_dashboard_asw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


