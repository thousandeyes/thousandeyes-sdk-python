# LocalNetworkTopologyDnsServerTest

DNS server test details. This object is only available when the topology `type` is `dns`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_time** | **int** | How long it took to resolve the DNS query in milliseconds. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_dns_server_test import LocalNetworkTopologyDnsServerTest

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworkTopologyDnsServerTest from a JSON string
local_network_topology_dns_server_test_instance = LocalNetworkTopologyDnsServerTest.from_json(json)
# print the JSON string representation of the object
print(LocalNetworkTopologyDnsServerTest.to_json())

# convert the object into a dict
local_network_topology_dns_server_test_dict = local_network_topology_dns_server_test_instance.to_dict()
# create an instance of LocalNetworkTopologyDnsServerTest from a dict
local_network_topology_dns_server_test_from_dict = LocalNetworkTopologyDnsServerTest.from_dict(local_network_topology_dns_server_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


