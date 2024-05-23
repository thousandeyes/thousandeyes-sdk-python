# TestDnsServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** | Unique identifier of the DNS server. | [optional] 
**server_name** | **str** | Fully qualified domain name (FQDN) of DNS server. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_dns_server import TestDnsServer

# TODO update the JSON string below
json = "{}"
# create an instance of TestDnsServer from a JSON string
test_dns_server_instance = TestDnsServer.from_json(json)
# print the JSON string representation of the object
print(TestDnsServer.to_json())

# convert the object into a dict
test_dns_server_dict = test_dns_server_instance.to_dict()
# create an instance of TestDnsServer from a dict
test_dns_server_from_dict = TestDnsServer.from_dict(test_dns_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


