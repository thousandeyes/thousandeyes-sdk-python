# ApiContextFilterResponse

Response containing dashboard filter settings and context details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**List[ApiDataSourceFilters]**](ApiDataSourceFilters.md) | List of filters to be applied to a dashboard. | 
**aid** | **str** | Account group ID of the filter. | 
**id** | **str** | Unique ID of the dashboard filter. | 
**name** | **str** | The name of the dashboard filter, this must be unique. | 
**description** | **str** | An optional description of the filter. | [optional] 
**created_by** | [**ApiDashboardFilterUserDetails**](ApiDashboardFilterUserDetails.md) |  | [optional] 
**modified_date** | **datetime** | Timestamp when the filter was last modified. | [optional] 
**created_date** | **datetime** | Timestamp when the filter was created. | [optional] 
**modified_by** | [**ApiDashboardFilterUserDetails**](ApiDashboardFilterUserDetails.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_context_filter_response import ApiContextFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContextFilterResponse from a JSON string
api_context_filter_response_instance = ApiContextFilterResponse.from_json(json)
# print the JSON string representation of the object
print(ApiContextFilterResponse.to_json())

# convert the object into a dict
api_context_filter_response_dict = api_context_filter_response_instance.to_dict()
# create an instance of ApiContextFilterResponse from a dict
api_context_filter_response_from_dict = ApiContextFilterResponse.from_dict(api_context_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


