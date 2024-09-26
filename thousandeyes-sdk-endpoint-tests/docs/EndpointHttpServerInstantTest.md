# EndpointHttpServerInstantTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_selector_type** | [**EndpointTestAgentSelectorType**](EndpointTestAgentSelectorType.md) |  | [optional] 
**agents** | **List[str]** | List of endpoint agent IDs (obtained from &#x60;/endpoint/agents&#x60; endpoint). Required when &#x60;agentSelectorType&#x60; is set to &#x60;specific-agent&#x60;. | [optional] 
**endpoint_agent_labels** | **List[str]** | List of endpoint agent label IDs (obtained from &#x60;/endpoint/labels&#x60; endpoint), required when &#x60;agentSelectorType&#x60; is set to &#x60;agent-labels&#x60;. | [optional] 
**max_machines** | **int** | Maximum number of agents which can execute the test. | [optional] [default to 25]
**test_name** | **str** | Name of the test. | 
**auth_type** | [**EndpointTestAuthType**](EndpointTestAuthType.md) |  | [optional] 
**has_path_trace_in_session** | **bool** | Enables \&quot;in session\&quot; path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session. | [optional] 
**http_time_limit** | **int** | Maximum amount of time in milliseconds the agents wait before a request times out. | [optional] [default to 5000]
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**username** | **str** | Username for Basic/NTLM authentication. | [optional] 
**ssl_version_id** | [**TestSslVersionId**](TestSslVersionId.md) |  | [optional] 
**tcp_probe_mode** | [**TestProbeModeResponse**](TestProbeModeResponse.md) |  | [optional] 
**verify_certificate** | **bool** | Flag indicating if a certificate should be verified. | [optional] [default to True]
**url** | **str** | The test target URL. You can optionally specify the protocol (&#x60;http&#x60; or &#x60;https&#x60;).   - **Default Protocol:** If no protocol is specified, &#x60;https&#x60; is used by default.  - **Port Number:** To specify a port, append it to the URL with a colon after the hostname or IP address (e.g., &#x60;https://example.com:443&#x60;).      - If no port is specified in the URL, the &#x60;port&#x60; is determined by the default for protocol (HTTP: 80, HTTPS: 443).  | 
**has_ping** | **bool** | Optional flag indicating if the test should run ping. | [optional] [default to True]
**has_traceroute** | **bool** | Optional flag indicating if the test should run traceroute. | [optional] [default to True]
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**target_response_time** | **int** | Response time target in milliseconds. Affects the colors of agents and legends on the view page. The value is compared with actual response time in order to determine the color scale (from green to red). | [optional] [default to 1000]
**password** | **str** | Password for Basic/NTLM authentication. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_instant_test import EndpointHttpServerInstantTest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointHttpServerInstantTest from a JSON string
endpoint_http_server_instant_test_instance = EndpointHttpServerInstantTest.from_json(json)
# print the JSON string representation of the object
print(EndpointHttpServerInstantTest.to_json())

# convert the object into a dict
endpoint_http_server_instant_test_dict = endpoint_http_server_instant_test_instance.to_dict()
# create an instance of EndpointHttpServerInstantTest from a dict
endpoint_http_server_instant_test_from_dict = EndpointHttpServerInstantTest.from_dict(endpoint_http_server_instant_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


