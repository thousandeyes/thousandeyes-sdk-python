# DnsSecTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedDnsSecTest]**](UnexpandedDnsSecTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.dns_sec_tests import DnsSecTests

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecTests from a JSON string
dns_sec_tests_instance = DnsSecTests.from_json(json)
# print the JSON string representation of the object
print(DnsSecTests.to_json())

# convert the object into a dict
dns_sec_tests_dict = dns_sec_tests_instance.to_dict()
# create an instance of DnsSecTests from a dict
dns_sec_tests_from_dict = DnsSecTests.from_dict(dns_sec_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


