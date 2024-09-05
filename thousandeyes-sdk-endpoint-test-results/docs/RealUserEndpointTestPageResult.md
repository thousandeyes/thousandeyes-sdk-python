# RealUserEndpointTestPageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** | Web page ID. The page ID is unique only within an endpoint real user test. | [optional] [readonly] 
**page_title** | **str** | Web page title. | [optional] [readonly] 
**page_url** | **str** | Web page url | [optional] [readonly] 
**load_date** | **datetime** | UTC date when page load started (ISO date-time format). | [optional] [readonly] 
**response_code** | **int** | HTTP response code. | [optional] [readonly] 
**page_timings** | [**RealUserEndpointTestPageTimings**](RealUserEndpointTestPageTimings.md) |  | [optional] 
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**id** | **str** | Endpoint real user test ID. Each endpoint real user test occurrence has a unique ID. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**response_time** | **int** | HTTP server response in milliseconds. | [optional] [readonly] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_result import RealUserEndpointTestPageResult

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestPageResult from a JSON string
real_user_endpoint_test_page_result_instance = RealUserEndpointTestPageResult.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestPageResult.to_json())

# convert the object into a dict
real_user_endpoint_test_page_result_dict = real_user_endpoint_test_page_result_instance.to_dict()
# create an instance of RealUserEndpointTestPageResult from a dict
real_user_endpoint_test_page_result_from_dict = RealUserEndpointTestPageResult.from_dict(real_user_endpoint_test_page_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


