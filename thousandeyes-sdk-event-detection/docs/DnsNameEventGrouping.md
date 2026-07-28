# DnsNameEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name_suffix** | **str** | Domain name suffix (for dns-name events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.dns_name_event_grouping import DnsNameEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of DnsNameEventGrouping from a JSON string
dns_name_event_grouping_instance = DnsNameEventGrouping.from_json(json)
# print the JSON string representation of the object
print(DnsNameEventGrouping.to_json())

# convert the object into a dict
dns_name_event_grouping_dict = dns_name_event_grouping_instance.to_dict()
# create an instance of DnsNameEventGrouping from a dict
dns_name_event_grouping_from_dict = DnsNameEventGrouping.from_dict(dns_name_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


