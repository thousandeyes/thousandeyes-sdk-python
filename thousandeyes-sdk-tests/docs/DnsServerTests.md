# DnsServerTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedDnsServerTest]**](UnexpandedDnsServerTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.dns_server_tests import DnsServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerTests from a JSON string
dns_server_tests_instance = DnsServerTests.from_json(json)
# print the JSON string representation of the object
print(DnsServerTests.to_json())

# convert the object into a dict
dns_server_tests_dict = dns_server_tests_instance.to_dict()
# create an instance of DnsServerTests from a dict
dns_server_tests_from_dict = DnsServerTests.from_dict(dns_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


