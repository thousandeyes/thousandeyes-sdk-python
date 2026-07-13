# DnsServerMeasurement

DNS resolution details collected while locating the HTTP test target. Present when the agent captured DNS server measurement data for the round. The order of `unusedDnsResponses` matches the order returned by the DNS resolver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_dns_response** | [**DnsServerResponse**](DnsServerResponse.md) |  | [optional] 
**unused_dns_responses** | [**List[DnsServerResponse]**](DnsServerResponse.md) | Additional DNS responses received while resolving the target. | [optional] 
**used_hosts_file** | **bool** | Indicates whether the hosts file (for example, &#x60;/etc/hosts&#x60;) was used to resolve the target. | [optional] [readonly] 
**resolved_ip** | **str** | IP address resolved for the target, from DNS or the hosts file. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_server_measurement import DnsServerMeasurement

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerMeasurement from a JSON string
dns_server_measurement_instance = DnsServerMeasurement.from_json(json)
# print the JSON string representation of the object
print(DnsServerMeasurement.to_json())

# convert the object into a dict
dns_server_measurement_dict = dns_server_measurement_instance.to_dict()
# create an instance of DnsServerMeasurement from a dict
dns_server_measurement_from_dict = DnsServerMeasurement.from_dict(dns_server_measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


