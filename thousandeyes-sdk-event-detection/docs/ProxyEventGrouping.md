# ProxyEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy** | **str** | Proxy name or IP (for proxy events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.proxy_event_grouping import ProxyEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyEventGrouping from a JSON string
proxy_event_grouping_instance = ProxyEventGrouping.from_json(json)
# print the JSON string representation of the object
print(ProxyEventGrouping.to_json())

# convert the object into a dict
proxy_event_grouping_dict = proxy_event_grouping_instance.to_dict()
# create an instance of ProxyEventGrouping from a dict
proxy_event_grouping_from_dict = ProxyEventGrouping.from_dict(proxy_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


