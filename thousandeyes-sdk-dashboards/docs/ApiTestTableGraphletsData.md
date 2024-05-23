# ApiTestTableGraphletsData

Information displayed within a mini-graph associated with a specific test in a table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | Name of the metric. | [optional] 
**test_id** | **str** | Identifier of the test. | [optional] 
**points** | [**List[ApiGraphletPoint]**](ApiGraphletPoint.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_test_table_graphlets_data import ApiTestTableGraphletsData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTestTableGraphletsData from a JSON string
api_test_table_graphlets_data_instance = ApiTestTableGraphletsData.from_json(json)
# print the JSON string representation of the object
print(ApiTestTableGraphletsData.to_json())

# convert the object into a dict
api_test_table_graphlets_data_dict = api_test_table_graphlets_data_instance.to_dict()
# create an instance of ApiTestTableGraphletsData from a dict
api_test_table_graphlets_data_from_dict = ApiTestTableGraphletsData.from_dict(api_test_table_graphlets_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


