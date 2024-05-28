# RealUserTestPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** | Web page ID. The page ID is unique only within an endpoint real user test. | [optional] [readonly] 
**page_title** | **str** | Web page title. | [optional] [readonly] 
**page_url** | **str** | Web page url | [optional] [readonly] 
**load_date** | **datetime** | UTC date when page load started (ISO date-time format). | [optional] [readonly] 
**response_code** | **int** | HTTP response code. | [optional] [readonly] 
**page_timings** | [**RealUserTestPageTimings**](RealUserTestPageTimings.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page import RealUserTestPage

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserTestPage from a JSON string
real_user_test_page_instance = RealUserTestPage.from_json(json)
# print the JSON string representation of the object
print(RealUserTestPage.to_json())

# convert the object into a dict
real_user_test_page_dict = real_user_test_page_instance.to_dict()
# create an instance of RealUserTestPage from a dict
real_user_test_page_from_dict = RealUserTestPage.from_dict(real_user_test_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

