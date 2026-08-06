# DomainEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Fully qualified domain name (for domain events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.domain_event_grouping import DomainEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of DomainEventGrouping from a JSON string
domain_event_grouping_instance = DomainEventGrouping.from_json(json)
# print the JSON string representation of the object
print(DomainEventGrouping.to_json())

# convert the object into a dict
domain_event_grouping_dict = domain_event_grouping_instance.to_dict()
# create an instance of DomainEventGrouping from a dict
domain_event_grouping_from_dict = DomainEventGrouping.from_dict(domain_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


