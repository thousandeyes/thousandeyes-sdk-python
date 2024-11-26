# ApiRequestDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_call_time** | **float** | Total time specific to the API call. | [optional] 
**assert_error_count** | **int** | Count of assertion errors. | [optional] 
**blocked_time** | **float** | Time to establish a socket connection for this request. | [optional] 
**connect_time** | **float** | Time to establish a TCP connection. | [optional] 
**completion** | **float** | 100 if the request responded with no assertion errors, otherwise 0. | [optional] 
**dns_time** | **float** | Time for the agent to perform a DNS resolution of the hostname in the URL. | [optional] 
**name** | **str** | Name of the API step. | [optional] 
**processing_time** | **float** | Time for the agent to process the API step, including the waitTimeMs delay specified in the post request options. | [optional] 
**receive_time** | **float** | Time to receive the response from the server. | [optional] 
**response_time** | **float** | Time for server to send the response. | [optional] 
**send_time** | **float** | Time to send the request. | [optional] 
**step_number** | **int** | Index of the API step within requests, starting at 1. | [optional] 
**step_time** | **float** | Total time for an API step, including API call time and processing time. | [optional] 
**step_type** | [**ApiRequestStepType**](ApiRequestStepType.md) |  | [optional] 
**url** | **str** | URL of request | [optional] 
**wait_time** | **float** | Total time between when the agent completes sending the HTTP request to the web server and when the agent receives the first byte of the response from the web server. | [optional] 
**assertions** | [**List[ApiRequestDetailAssertion]**](ApiRequestDetailAssertion.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.api_request_detail import ApiRequestDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestDetail from a JSON string
api_request_detail_instance = ApiRequestDetail.from_json(json)
# print the JSON string representation of the object
print(ApiRequestDetail.to_json())

# convert the object into a dict
api_request_detail_dict = api_request_detail_instance.to_dict()
# create an instance of ApiRequestDetail from a dict
api_request_detail_from_dict = ApiRequestDetail.from_dict(api_request_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


