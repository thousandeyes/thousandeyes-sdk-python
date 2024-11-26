# DnsServerProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_measurements** | **bool** | Set to &#x60;true&#x60; to enable bandwidth measurements, only applies to Enterprise agents assigned to the test. | [optional] 
**dns_servers** | [**List[TestDnsServer]**](TestDnsServer.md) |  | 
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
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.dns_server_properties import DnsServerProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerProperties from a JSON string
dns_server_properties_instance = DnsServerProperties.from_json(json)
# print the JSON string representation of the object
print(DnsServerProperties.to_json())

# convert the object into a dict
dns_server_properties_dict = dns_server_properties_instance.to_dict()
# create an instance of DnsServerProperties from a dict
dns_server_properties_from_dict = DnsServerProperties.from_dict(dns_server_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


