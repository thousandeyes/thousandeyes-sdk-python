# DnsTraceProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_transport_protocol** | [**TestDnsTransportProtocol**](TestDnsTransportProtocol.md) |  | [optional] 
**domain** | **str** | The target record for the test, with the record type suffixed. If no record type is specified, the test defaults to an ANY record. | 
**dns_query_class** | [**DnsQueryClass**](DnsQueryClass.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.dns_trace_properties import DnsTraceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DnsTraceProperties from a JSON string
dns_trace_properties_instance = DnsTraceProperties.from_json(json)
# print the JSON string representation of the object
print(DnsTraceProperties.to_json())

# convert the object into a dict
dns_trace_properties_dict = dns_trace_properties_instance.to_dict()
# create an instance of DnsTraceProperties from a dict
dns_trace_properties_from_dict = DnsTraceProperties.from_dict(dns_trace_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


