# HttpServerBaseProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**TestAuthType**](TestAuthType.md) |  | [optional] 
**agent_interfaces** | [**AgentInterfaces**](AgentInterfaces.md) |  | [optional] 
**bandwidth_measurements** | **bool** | Set to &#x60;true&#x60; to enable bandwidth measurements, only applies to Enterprise agents assigned to the test. | [optional] 
**client_certificate** | **str** | String representation (containing newline characters) of client certificate, the private key must be placed first, then the certificate. | [optional] 
**content_regex** | **str** | Content regex, this field does not require escaping. | [optional] 
**custom_headers** | [**TestCustomHeaders**](TestCustomHeaders.md) |  | [optional] 
**desired_status_code** | **str** | Specify the HTTP status code value that indicates a successful response. The default value accepts any 2xx or 3xx status code. | [optional] [default to 'default']
**download_limit** | **int** | Specifies maximum number of bytes to download from the target object. | [optional] 
**dns_override** | **str** | IP address to use for DNS override. | [optional] 
**http_target_time** | **int** | Target time for HTTP server completion, specified in milliseconds. | [optional] 
**http_time_limit** | **int** | HTTP time limit in seconds. | [optional] [default to 5]
**http_version** | **int** | HTTP protocol version. Set to &#39;2&#39; to prefer HTTP/2, or &#39;1&#39; to use only HTTP/1.1. | [optional] [default to 2]
**include_headers** | **bool** | Set to &#x60;true&#x60; to capture response headers for objects loaded by the test. | [optional] [default to True]
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**o_auth** | [**OAuth**](OAuth.md) |  | [optional] 
**password** | **str** | Password for Basic/NTLM authentication. | [optional] 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**ssl_version** | **str** | Reflects the verbose SSL protocol version used by a test. | [optional] [readonly] 
**ssl_version_id** | [**TestSslVersionId**](TestSslVersionId.md) |  | [optional] 
**url** | **str** | Target for the test. | [optional] 
**use_ntlm** | **bool** | Set to true to use NTLM, false to use Basic Authentication. Requires username and password to be set. | [optional] 
**user_agent** | **str** | User-agent string to be provided during the test. | [optional] 
**username** | **str** | Username for Basic/NTLM authentication. | [optional] 
**verify_certificate** | **bool** | Ignore or acknowledge certificate errors. Set to false to ignore certificate errors. | [optional] [default to False]
**allow_unsafe_legacy_renegotiation** | **bool** | Allows TLS renegotiation with servers not supporting RFC 5746. Default Set to true to allow unsafe legacy renegotiation. | [optional] [default to True]
**follow_redirects** | **bool** | To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to &#x60;false&#x60;. | [optional] [default to True]
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**override_agent_proxy** | **bool** | Flag indicating if a proxy other than the default should be used. To override the default proxy for agents, set to &#x60;true&#x60; and specify a value for &#x60;overrideProxyId&#x60;. | [optional] [default to False]
**override_proxy_id** | **str** | ID of the proxy to be used if the default proxy is overridden. | [optional] 
**collect_proxy_network_data** | **bool** | Indicates whether network data to the proxy should be collected. | [optional] [default to False]

## Example

```python
from thousandeyes_sdk.tests.models.http_server_base_properties import HttpServerBaseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of HttpServerBaseProperties from a JSON string
http_server_base_properties_instance = HttpServerBaseProperties.from_json(json)
# print the JSON string representation of the object
print(HttpServerBaseProperties.to_json())

# convert the object into a dict
http_server_base_properties_dict = http_server_base_properties_instance.to_dict()
# create an instance of HttpServerBaseProperties from a dict
http_server_base_properties_from_dict = HttpServerBaseProperties.from_dict(http_server_base_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


