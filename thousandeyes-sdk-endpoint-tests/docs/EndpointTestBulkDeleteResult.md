# EndpointTestBulkDeleteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_test_ids** | **List[str]** | IDs of tests deleted by this request. Empty when no tests were deleted. | 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_bulk_delete_result import EndpointTestBulkDeleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestBulkDeleteResult from a JSON string
endpoint_test_bulk_delete_result_instance = EndpointTestBulkDeleteResult.from_json(json)
# print the JSON string representation of the object
print(EndpointTestBulkDeleteResult.to_json())

# convert the object into a dict
endpoint_test_bulk_delete_result_dict = endpoint_test_bulk_delete_result_instance.to_dict()
# create an instance of EndpointTestBulkDeleteResult from a dict
endpoint_test_bulk_delete_result_from_dict = EndpointTestBulkDeleteResult.from_dict(endpoint_test_bulk_delete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


