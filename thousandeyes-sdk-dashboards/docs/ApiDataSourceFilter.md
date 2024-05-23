# ApiDataSourceFilter

List of different filter properties for a single datasource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | Data source property to filter by. | 
**values** | **List[str]** | Values to filter by based on the specified &#x60;filterId&#x60;. | 
**metric_ids** | **List[str]** | Dashboard metric associated with the filter property. | 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_data_source_filter import ApiDataSourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataSourceFilter from a JSON string
api_data_source_filter_instance = ApiDataSourceFilter.from_json(json)
# print the JSON string representation of the object
print(ApiDataSourceFilter.to_json())

# convert the object into a dict
api_data_source_filter_dict = api_data_source_filter_instance.to_dict()
# create an instance of ApiDataSourceFilter from a dict
api_data_source_filter_from_dict = ApiDataSourceFilter.from_dict(api_data_source_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


