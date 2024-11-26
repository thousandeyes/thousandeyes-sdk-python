# DnsServerInstantTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 
**bandwidth_measurements** | **bool** | Set to &#x60;true&#x60; to enable bandwidth measurements, only applies to Enterprise agents assigned to the test. | [optional] 
**dns_servers** | **List[str]** | A list of DNS server FQDN. | 
**dns_transport_protocol** | [**TestDnsTransportProtocol**](TestDnsTransportProtocol.md) |  | [optional] 
**domain** | **str** | The target record for the test, with the record type suffixed. If no record type is specified, the test defaults to an ANY record. | 
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**recursive_queries** | **bool** | Set true to run query with RD (recursion desired) flag enabled. | [optional] 
**ipv6_policy** | [**TestIpv6Policy**](TestIpv6Policy.md) |  | [optional] 
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**dns_query_class** | [**DnsQueryClass**](DnsQueryClass.md) |  | [optional] 
**agents** | [**List[TestAgent]**](TestAgent.md) | A list of objects with &#x60;agentId&#x60; (required) and &#x60;sourceIpAddress&#x60; (optional). | 

## Example

```python
from thousandeyes_sdk.instant_tests.models.dns_server_instant_test_request import DnsServerInstantTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerInstantTestRequest from a JSON string
dns_server_instant_test_request_instance = DnsServerInstantTestRequest.from_json(json)
# print the JSON string representation of the object
print(DnsServerInstantTestRequest.to_json())

# convert the object into a dict
dns_server_instant_test_request_dict = dns_server_instant_test_request_instance.to_dict()
# create an instance of DnsServerInstantTestRequest from a dict
dns_server_instant_test_request_from_dict = DnsServerInstantTestRequest.from_dict(dns_server_instant_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


