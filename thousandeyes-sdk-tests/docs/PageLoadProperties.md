# PageLoadProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**TestAuthType**](TestAuthType.md) |  | [optional] 
**bandwidth_measurements** | **bool** | Set to &#x60;true&#x60; to enable bandwidth measurements, only applies to Enterprise agents assigned to the test. | [optional] 
**client_certificate** | **str** | String representation (containing newline characters) of client certificate, the private key must be placed first, then the certificate. | [optional] 
**content_regex** | **str** | Verify content using a regular expression. This field does not require escaping. | [optional] 
**custom_headers** | [**TestCustomHeaders**](TestCustomHeaders.md) |  | [optional] 
**desired_status_code** | **str** | Specify the HTTP status code value that indicates a successful response. | [optional] [default to '200']
**emulated_device_id** | **str** | id of the emulated device, if one was given when the test was created | [optional] 
**follow_redirects** | **bool** | To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to false. | [optional] [default to True]
**http_target_time** | **int** | Target time for HTTP server completion, specified in milliseconds. | [optional] 
**http_time_limit** | **int** | HTTP time limit in seconds. | [optional] [default to 5]
**http_version** | **int** | HTTP protocol version. Set to &#39;2&#39; to prefer HTTP/2, or &#39;1&#39; to use only HTTP/1.1. | [optional] [default to 2]
**include_headers** | **bool** | Set to &#x60;true&#x60; to capture response headers for objects loaded by the test. | [optional] [default to True]
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**page_load_target_time** | **int** | Target time for page load completion, specified in seconds and cannot exceed the &#x60;pageLoadTimeLimit&#x60;. | [optional] 
**page_load_time_limit** | **int** | Page load time limit. Must be larger than the &#x60;httpTimeLimit&#x60;. | [optional] [default to 10]
**password** | **str** | Password for Basic/NTLM authentication. | [optional] 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**ssl_version** | **str** | Reflects the verbose SSL protocol version used by a test. | [optional] [readonly] 
**ssl_version_id** | [**TestSslVersionId**](TestSslVersionId.md) |  | [optional] 
**url** | **str** | Target for the test. | 
**use_ntlm** | **bool** | Set to true to use NTLM, false to use Basic Authentication. Requires username and password to be set. | [optional] 
**user_agent** | **str** | User-agent string to be provided during the test. | [optional] 
**username** | **str** | Username for Basic/NTLM authentication. | [optional] 
**verify_certificate** | **bool** | Ignore or acknowledge certificate errors. Set to false to ignore certificate errors. | [optional] [default to False]
**allow_unsafe_legacy_renegotiation** | **bool** | Allows TLS renegotiation with servers not supporting RFC 5746. Default Set to true to allow unsafe legacy renegotiation. | [optional] [default to True]
**block_domains** | **str** | Domains or full object URLs to be excluded from metrics and waterfall data for transaction tests. | [optional] 
**disable_screenshot** | **bool** | Enables or disables screenshots on error. Set true to not capture | [optional] [default to False]
**allow_mic_and_camera** | **bool** | Set true allow the use of a fake mic and camera in the browser. | [optional] [default to False]
**allow_geolocation** | **bool** | Set true to use the agent’s geolocation by the web page. | [optional] [default to False]
**browser_language** | **str** | Set one of the available browser language that you want to use to configure the browser. | [optional] 
**page_loading_strategy** | [**TestPageLoadingStrategy**](TestPageLoadingStrategy.md) |  | [optional] 
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.page_load_properties import PageLoadProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PageLoadProperties from a JSON string
page_load_properties_instance = PageLoadProperties.from_json(json)
# print the JSON string representation of the object
print(PageLoadProperties.to_json())

# convert the object into a dict
page_load_properties_dict = page_load_properties_instance.to_dict()
# create an instance of PageLoadProperties from a dict
page_load_properties_from_dict = PageLoadProperties.from_dict(page_load_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


