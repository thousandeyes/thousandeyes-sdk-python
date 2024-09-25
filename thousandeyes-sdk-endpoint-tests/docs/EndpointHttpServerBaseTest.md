# EndpointHttpServerBaseTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**EndpointTestAuthType**](EndpointTestAuthType.md) |  | [optional] 
**has_path_trace_in_session** | **bool** | Enables \&quot;in session\&quot; path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session. | [optional] 
**http_time_limit** | **int** | Maximum amount of time in milliseconds the agents wait before a request times out. | [optional] [default to 5000]
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**username** | **str** | Username for Basic/NTLM authentication. | [optional] 
**ssl_version_id** | [**TestSslVersionId**](TestSslVersionId.md) |  | [optional] 
**tcp_probe_mode** | [**TestProbeModeResponse**](TestProbeModeResponse.md) |  | [optional] 
**verify_certificate** | **bool** | Flag indicating if a certificate should be verified. | [optional] [default to True]
**url** | **str** | The test target URL. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_base_test import EndpointHttpServerBaseTest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointHttpServerBaseTest from a JSON string
endpoint_http_server_base_test_instance = EndpointHttpServerBaseTest.from_json(json)
# print the JSON string representation of the object
print(EndpointHttpServerBaseTest.to_json())

# convert the object into a dict
endpoint_http_server_base_test_dict = endpoint_http_server_base_test_instance.to_dict()
# create an instance of EndpointHttpServerBaseTest from a dict
endpoint_http_server_base_test_from_dict = EndpointHttpServerBaseTest.from_dict(endpoint_http_server_base_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


