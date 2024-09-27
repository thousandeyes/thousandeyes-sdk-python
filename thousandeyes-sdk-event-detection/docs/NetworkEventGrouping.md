# NetworkEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_asn** | **int** | AS number of the source network (for network-pop and network events). | [optional] [readonly] 
**dest_asn** | **int** | AS number of the destination network (for network events). | [optional] [readonly] 
**source_country_code** | **str** | The source network&#39;s country code (for network-pop and network events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.network_event_grouping import NetworkEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkEventGrouping from a JSON string
network_event_grouping_instance = NetworkEventGrouping.from_json(json)
# print the JSON string representation of the object
print(NetworkEventGrouping.to_json())

# convert the object into a dict
network_event_grouping_dict = network_event_grouping_instance.to_dict()
# create an instance of NetworkEventGrouping from a dict
network_event_grouping_from_dict = NetworkEventGrouping.from_dict(network_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


