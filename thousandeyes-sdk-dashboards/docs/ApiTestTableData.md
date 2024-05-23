# ApiTestTableData

Data shown in a test table widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** | Identifier of the test. | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**target** | **str** | Configured target of the test. | [optional] 
**test_type** | **str** | Type of the test. | [optional] 
**alert_count** | **int** | Number of active alerts of the test. | [optional] 
**is_shared** | **bool** | Set to &#x60;true&#x60; if test is shared, &#x60;false&#x60; otherwise. | [optional] 
**graphlets** | [**List[ApiTestTableGraphletsData]**](ApiTestTableGraphletsData.md) | List of time series points for test metrics in the last 12 hours. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_test_table_data import ApiTestTableData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTestTableData from a JSON string
api_test_table_data_instance = ApiTestTableData.from_json(json)
# print the JSON string representation of the object
print(ApiTestTableData.to_json())

# convert the object into a dict
api_test_table_data_dict = api_test_table_data_instance.to_dict()
# create an instance of ApiTestTableData from a dict
api_test_table_data_from_dict = ApiTestTableData.from_dict(api_test_table_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


