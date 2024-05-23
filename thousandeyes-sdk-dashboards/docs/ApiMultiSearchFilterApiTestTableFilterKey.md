# ApiMultiSearchFilterApiTestTableFilterKey

A multi search filter key within the Multi-Metric table widget. The key represents the filter name, and the value specifies the filter value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**TestTableFilterKey**](TestTableFilterKey.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_multi_search_filter_api_test_table_filter_key import ApiMultiSearchFilterApiTestTableFilterKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMultiSearchFilterApiTestTableFilterKey from a JSON string
api_multi_search_filter_api_test_table_filter_key_instance = ApiMultiSearchFilterApiTestTableFilterKey.from_json(json)
# print the JSON string representation of the object
print(ApiMultiSearchFilterApiTestTableFilterKey.to_json())

# convert the object into a dict
api_multi_search_filter_api_test_table_filter_key_dict = api_multi_search_filter_api_test_table_filter_key_instance.to_dict()
# create an instance of ApiMultiSearchFilterApiTestTableFilterKey from a dict
api_multi_search_filter_api_test_table_filter_key_from_dict = ApiMultiSearchFilterApiTestTableFilterKey.from_dict(api_multi_search_filter_api_test_table_filter_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


