# DnsServerEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | DNS server IP address (for dns-server events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.dns_server_event_grouping import DnsServerEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerEventGrouping from a JSON string
dns_server_event_grouping_instance = DnsServerEventGrouping.from_json(json)
# print the JSON string representation of the object
print(DnsServerEventGrouping.to_json())

# convert the object into a dict
dns_server_event_grouping_dict = dns_server_event_grouping_instance.to_dict()
# create an instance of DnsServerEventGrouping from a dict
dns_server_event_grouping_from_dict = DnsServerEventGrouping.from_dict(dns_server_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


