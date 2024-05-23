# ApiNumbersCardData

The data displayed on a numbers card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Identifier of the card. | [optional] 
**start_date** | **datetime** | UTC start date of the data shown in the API output (ISO date-time format). | [optional] 
**end_date** | **datetime** | UTC end date of the data shown in the API output (ISO date-time format). | [optional] 
**previous_value** | **float** | Previous value if &#x60;compareToPreviousValue &#x3D;&#x3D; true&#x60; in configuration. | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**timestamp** | **int** | Timestamp of the aggregated data point. | [optional] 
**number_of_data_points** | **int** | Number of points aggregated into the data point | [optional] 
**value** | **float** | Aggregated value. | [optional] 
**status** | **str** | Message for not fully configured card or no data. | [optional] 
**alert_suppression_windows** | [**List[ApiDashboardAsw]**](ApiDashboardAsw.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_numbers_card_data import ApiNumbersCardData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNumbersCardData from a JSON string
api_numbers_card_data_instance = ApiNumbersCardData.from_json(json)
# print the JSON string representation of the object
print(ApiNumbersCardData.to_json())

# convert the object into a dict
api_numbers_card_data_dict = api_numbers_card_data_instance.to_dict()
# create an instance of ApiNumbersCardData from a dict
api_numbers_card_data_from_dict = ApiNumbersCardData.from_dict(api_numbers_card_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


