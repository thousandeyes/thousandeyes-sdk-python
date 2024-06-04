# ApiProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follow_redirects** | **bool** | To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to &#x60;false&#x60;. | [optional] [default to True]
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**predefined_variables** | [**List[ApiPredefinedVariable]**](ApiPredefinedVariable.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**requests** | [**List[ApiRequest]**](ApiRequest.md) |  | 
**ssl_version_id** | [**TestSslVersionId**](TestSslVersionId.md) |  | [optional] 
**target_time** | **int** | Target time for completion metric, defaults to 50% of time limit specified in seconds. (0 means default behavior) | [optional] 
**time_limit** | **int** | Time limit for transaction in seconds. Exceeding this limit will result in a Timeout error. | [optional] [default to 30]
**url** | **str** | Target for the test. | 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.api_properties import ApiProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProperties from a JSON string
api_properties_instance = ApiProperties.from_json(json)
# print the JSON string representation of the object
print(ApiProperties.to_json())

# convert the object into a dict
api_properties_dict = api_properties_instance.to_dict()
# create an instance of ApiProperties from a dict
api_properties_from_dict = ApiProperties.from_dict(api_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


