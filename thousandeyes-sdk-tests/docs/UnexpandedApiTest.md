# UnexpandedApiTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event.  **Note**: **Saved Events** are now called **Private Snapshots** in the user interface. This change does not affect API.  | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**client_certificate** | **str** | String representation (containing newline characters) of client certificate, the private key must be placed first, then the certificate. | [optional] 
**client_cert_domains_allow_list** | **str** | Comma separated list of domains to send the client certificate. | [optional] 
**collect_proxy_network_data** | **bool** | Indicates whether network data to the proxy should be collected. | [optional] [default to False]
**distributed_tracing** | **bool** | Adds distributed tracing headers to API requests using B3 and W3C standards. | [optional] 
**follow_redirects** | **bool** | To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to &#x60;false&#x60;. | [optional] [default to True]
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**override_agent_proxy** | **bool** | Flag indicating if a proxy other than the default should be used. To override the default proxy for agents, set to &#x60;true&#x60; and specify a value for &#x60;overrideProxyId&#x60;. | [optional] [default to False]
**override_proxy_id** | **str** | ID of the proxy to be used if the default proxy is overridden. | [optional] 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**predefined_variables** | [**List[ApiPredefinedVariable]**](ApiPredefinedVariable.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**requests** | [**List[ApiRequest]**](ApiRequest.md) |  | 
**ssl_version_id** | [**TestSslVersionId**](TestSslVersionId.md) |  | [optional] 
**target_time** | **int** | Target time for completion metric, defaults to 50% of time limit specified in seconds. (0 means default behavior) | [optional] 
**time_limit** | **int** | Time limit for transaction in seconds. Exceeding this limit will result in a Timeout error. | [optional] [default to 30]
**url** | **str** | Target for the test. | 
**bgp_measurements** | **bool** | Set to &#x60;true&#x60; to enable bgp measurements. | [optional] [default to True]
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]

## Example

```python
from thousandeyes_sdk.tests.models.unexpanded_api_test import UnexpandedApiTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedApiTest from a JSON string
unexpanded_api_test_instance = UnexpandedApiTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedApiTest.to_json())

# convert the object into a dict
unexpanded_api_test_dict = unexpanded_api_test_instance.to_dict()
# create an instance of UnexpandedApiTest from a dict
unexpanded_api_test_from_dict = UnexpandedApiTest.from_dict(unexpanded_api_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


