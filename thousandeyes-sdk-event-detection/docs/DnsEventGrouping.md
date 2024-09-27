# DnsEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_domain** | **str** | Root domain name (for dns events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.dns_event_grouping import DnsEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of DnsEventGrouping from a JSON string
dns_event_grouping_instance = DnsEventGrouping.from_json(json)
# print the JSON string representation of the object
print(DnsEventGrouping.to_json())

# convert the object into a dict
dns_event_grouping_dict = dns_event_grouping_instance.to_dict()
# create an instance of DnsEventGrouping from a dict
dns_event_grouping_from_dict = DnsEventGrouping.from_dict(dns_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


