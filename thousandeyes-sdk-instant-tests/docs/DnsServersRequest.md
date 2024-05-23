# DnsServersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_servers** | **List[str]** | A list of DNS server FQDN. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.dns_servers_request import DnsServersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServersRequest from a JSON string
dns_servers_request_instance = DnsServersRequest.from_json(json)
# print the JSON string representation of the object
print(DnsServersRequest.to_json())

# convert the object into a dict
dns_servers_request_dict = dns_servers_request_instance.to_dict()
# create an instance of DnsServersRequest from a dict
dns_servers_request_from_dict = DnsServersRequest.from_dict(dns_servers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


