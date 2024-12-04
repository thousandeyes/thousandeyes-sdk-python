# UnexpandedDnsTraceTest


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
**saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**dns_transport_protocol** | [**TestDnsTransportProtocol**](TestDnsTransportProtocol.md) |  | [optional] 
**domain** | **str** | The target record for the test, with the record type suffixed. If no record type is specified, the test defaults to an ANY record. | 
**dns_query_class** | [**DnsQueryClass**](DnsQueryClass.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]

## Example

```python
from thousandeyes_sdk.tests.models.unexpanded_dns_trace_test import UnexpandedDnsTraceTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedDnsTraceTest from a JSON string
unexpanded_dns_trace_test_instance = UnexpandedDnsTraceTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedDnsTraceTest.to_json())

# convert the object into a dict
unexpanded_dns_trace_test_dict = unexpanded_dns_trace_test_instance.to_dict()
# create an instance of UnexpandedDnsTraceTest from a dict
unexpanded_dns_trace_test_from_dict = UnexpandedDnsTraceTest.from_dict(unexpanded_dns_trace_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


