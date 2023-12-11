# DnsTraceInstantTestRequest


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
**links** | [**UnexpandedInstantTestLinks**](UnexpandedInstantTestLinks.md) |  | [optional] 
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 
**agents** | [**List[InstantTestRequestAgentsInner]**](InstantTestRequestAgentsInner.md) | A list of objects with &#x60;agentId&#x60; (required) and &#x60;sourceIpAddress&#x60; (optional). | 
**dns_transport_protocol** | [**TestDnsTransportProtocol**](TestDnsTransportProtocol.md) |  | [optional] 
**domain** | **str** | The target record for the test, with the record type suffixed. If no record type is specified, the test defaults to an ANY record. | 
**dns_query_class** | [**DnsQueryClass**](DnsQueryClass.md) |  | [optional] 

## Example

```python
from instant_tests_api.models.dns_trace_instant_test_request import DnsTraceInstantTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DnsTraceInstantTestRequest from a JSON string
dns_trace_instant_test_request_instance = DnsTraceInstantTestRequest.from_json(json)
# print the JSON string representation of the object
print DnsTraceInstantTestRequest.to_json()

# convert the object into a dict
dns_trace_instant_test_request_dict = dns_trace_instant_test_request_instance.to_dict()
# create an instance of DnsTraceInstantTestRequest from a dict
dns_trace_instant_test_request_form_dict = dns_trace_instant_test_request.from_dict(dns_trace_instant_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


