# ApiContextFiltersResponse

All global dashboard filters saved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_filters** | [**List[ApiContextFilterResponse]**](ApiContextFilterResponse.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_context_filters_response import ApiContextFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContextFiltersResponse from a JSON string
api_context_filters_response_instance = ApiContextFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(ApiContextFiltersResponse.to_json())

# convert the object into a dict
api_context_filters_response_dict = api_context_filters_response_instance.to_dict()
# create an instance of ApiContextFiltersResponse from a dict
api_context_filters_response_from_dict = ApiContextFiltersResponse.from_dict(api_context_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


