# DynamicBaseTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | Which supported application to monitor, can be one of &#x60;webex&#x60;, &#x60;zoom&#x60;, &#x60;microsoft-teams&#x60;. | [optional] 
**protocol** | [**EndpointTestResultProtocol**](EndpointTestResultProtocol.md) |  | [optional] 
**tcp_probe_mode** | [**TestProbeModeResponse**](TestProbeModeResponse.md) |  | [optional] 
**udp_probe_mode** | [**UdpProbeModeResponse**](UdpProbeModeResponse.md) |  | [optional] 
**webex** | [**DynamicTestWebex**](DynamicTestWebex.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.dynamic_base_test_result import DynamicBaseTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicBaseTestResult from a JSON string
dynamic_base_test_result_instance = DynamicBaseTestResult.from_json(json)
# print the JSON string representation of the object
print(DynamicBaseTestResult.to_json())

# convert the object into a dict
dynamic_base_test_result_dict = dynamic_base_test_result_instance.to_dict()
# create an instance of DynamicBaseTestResult from a dict
dynamic_base_test_result_from_dict = DynamicBaseTestResult.from_dict(dynamic_base_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


