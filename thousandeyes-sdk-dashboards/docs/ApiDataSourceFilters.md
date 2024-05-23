# ApiDataSourceFilters

List of different datasource filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source_id** | **str** | Types of data source. | 
**filters** | [**List[ApiDataSourceFilter]**](ApiDataSourceFilter.md) | List of different filter properties. | 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_data_source_filters import ApiDataSourceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataSourceFilters from a JSON string
api_data_source_filters_instance = ApiDataSourceFilters.from_json(json)
# print the JSON string representation of the object
print(ApiDataSourceFilters.to_json())

# convert the object into a dict
api_data_source_filters_dict = api_data_source_filters_instance.to_dict()
# create an instance of ApiDataSourceFilters from a dict
api_data_source_filters_from_dict = ApiDataSourceFilters.from_dict(api_data_source_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


