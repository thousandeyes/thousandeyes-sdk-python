# ApiDashboardFilterUserDetails

Details of user who created or modified the filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique ID of the user. | [optional] 
**name** | **str** | Name of the user. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_dashboard_filter_user_details import ApiDashboardFilterUserDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDashboardFilterUserDetails from a JSON string
api_dashboard_filter_user_details_instance = ApiDashboardFilterUserDetails.from_json(json)
# print the JSON string representation of the object
print(ApiDashboardFilterUserDetails.to_json())

# convert the object into a dict
api_dashboard_filter_user_details_dict = api_dashboard_filter_user_details_instance.to_dict()
# create an instance of ApiDashboardFilterUserDetails from a dict
api_dashboard_filter_user_details_from_dict = ApiDashboardFilterUserDetails.from_dict(api_dashboard_filter_user_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


