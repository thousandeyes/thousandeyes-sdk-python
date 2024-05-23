# DnsTraceTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedDnsTraceTest]**](UnexpandedDnsTraceTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.dns_trace_tests import DnsTraceTests

# TODO update the JSON string below
json = "{}"
# create an instance of DnsTraceTests from a JSON string
dns_trace_tests_instance = DnsTraceTests.from_json(json)
# print the JSON string representation of the object
print(DnsTraceTests.to_json())

# convert the object into a dict
dns_trace_tests_dict = dns_trace_tests_instance.to_dict()
# create an instance of DnsTraceTests from a dict
dns_trace_tests_from_dict = DnsTraceTests.from_dict(dns_trace_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


