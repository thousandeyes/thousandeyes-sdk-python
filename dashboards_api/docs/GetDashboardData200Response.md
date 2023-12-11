# GetDashboardData200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**group_labels** | [**List[ApiReportDataComponentLabelMap]**](ApiReportDataComponentLabelMap.md) |  | [optional] 
**bin_size** | **int** | Duration of each bin. | [optional] 
**data** | [**ApiWidgetsDataV2**](ApiWidgetsDataV2.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from dashboards_api.models.get_dashboard_data200_response import GetDashboardData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDashboardData200Response from a JSON string
get_dashboard_data200_response_instance = GetDashboardData200Response.from_json(json)
# print the JSON string representation of the object
print GetDashboardData200Response.to_json()

# convert the object into a dict
get_dashboard_data200_response_dict = get_dashboard_data200_response_instance.to_dict()
# create an instance of GetDashboardData200Response from a dict
get_dashboard_data200_response_form_dict = get_dashboard_data200_response.from_dict(get_dashboard_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


