# ApiWidgetsDataV2

Data of a widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[ApiNumbersCardData]**](ApiNumbersCardData.md) |  | [optional] 
**columns** | [**List[ApiMultiMetricColumnData]**](ApiMultiMetricColumnData.md) |  | [optional] 
**points** | [**List[ApiWidgetDataPoint]**](ApiWidgetDataPoint.md) |  | [optional] 
**tests** | [**List[ApiTestTableData]**](ApiTestTableData.md) |  | [optional] 
**start_round** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] 
**alert_suppression_windows** | [**List[ApiDashboardAsw]**](ApiDashboardAsw.md) |  | [optional] 
**total_alerts** | **int** | Total number of active alerts within configured timespan. | [optional] 
**active_alerts** | **int** | Total number of currently active alerts. | [optional] 
**alerts** | [**List[ApiAlertListAlert]**](ApiAlertListAlert.md) |  | [optional] 
**summary** | [**ApiAgentStatusSummary**](ApiAgentStatusSummary.md) |  | [optional] 
**agents** | [**List[ApiAgentStatusAgent]**](ApiAgentStatusAgent.md) |  | [optional] 
**status** | **str** | Message for not fully configured card or no data. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_widgets_data_v2 import ApiWidgetsDataV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidgetsDataV2 from a JSON string
api_widgets_data_v2_instance = ApiWidgetsDataV2.from_json(json)
# print the JSON string representation of the object
print(ApiWidgetsDataV2.to_json())

# convert the object into a dict
api_widgets_data_v2_dict = api_widgets_data_v2_instance.to_dict()
# create an instance of ApiWidgetsDataV2 from a dict
api_widgets_data_v2_from_dict = ApiWidgetsDataV2.from_dict(api_widgets_data_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


