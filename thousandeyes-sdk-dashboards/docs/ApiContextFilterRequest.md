# ApiContextFilterRequest

Request containing dashboard filter name, description and context details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**List[ApiDataSourceFilters]**](ApiDataSourceFilters.md) | List of filters to be applied to a dashboard. | 
**name** | **str** | The name of the dashboard filter, this must be unique. | 
**description** | **str** | An optional description of the filter. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_context_filter_request import ApiContextFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContextFilterRequest from a JSON string
api_context_filter_request_instance = ApiContextFilterRequest.from_json(json)
# print the JSON string representation of the object
print(ApiContextFilterRequest.to_json())

# convert the object into a dict
api_context_filter_request_dict = api_context_filter_request_instance.to_dict()
# create an instance of ApiContextFilterRequest from a dict
api_context_filter_request_from_dict = ApiContextFilterRequest.from_dict(api_context_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


