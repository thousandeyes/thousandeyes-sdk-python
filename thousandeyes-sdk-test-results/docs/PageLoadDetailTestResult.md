# PageLoadDetailTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**response_time** | **float** | Time to first byte in milliseconds | [optional] [readonly] 
**total_size** | **int** | Sum of wire size of all objects on page in bytes | [optional] [readonly] 
**num_objects** | **int** | Number of objects found on the page | [optional] [readonly] 
**num_errors** | **int** | Number of objects which encountered errors during download | [optional] [readonly] 
**dom_load_time** | **int** | Time to interaction in milliseconds | [optional] [readonly] 
**page_load_time** | **int** | Time to completely load page in milliseconds | [optional] [readonly] 
**har** | **object** | See [HAR specification](http://www.softwareishard.com/blog/har-12-spec/) for details | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.page_load_detail_test_result import PageLoadDetailTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PageLoadDetailTestResult from a JSON string
page_load_detail_test_result_instance = PageLoadDetailTestResult.from_json(json)
# print the JSON string representation of the object
print(PageLoadDetailTestResult.to_json())

# convert the object into a dict
page_load_detail_test_result_dict = page_load_detail_test_result_instance.to_dict()
# create an instance of PageLoadDetailTestResult from a dict
page_load_detail_test_result_from_dict = PageLoadDetailTestResult.from_dict(page_load_detail_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


