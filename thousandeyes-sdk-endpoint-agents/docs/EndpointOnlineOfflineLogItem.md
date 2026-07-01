# EndpointOnlineOfflineLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_item_type** | [**EndpointOnlineOfflineLogItemType**](EndpointOnlineOfflineLogItemType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_online_offline_log_item import EndpointOnlineOfflineLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointOnlineOfflineLogItem from a JSON string
endpoint_online_offline_log_item_instance = EndpointOnlineOfflineLogItem.from_json(json)
# print the JSON string representation of the object
print(EndpointOnlineOfflineLogItem.to_json())

# convert the object into a dict
endpoint_online_offline_log_item_dict = endpoint_online_offline_log_item_instance.to_dict()
# create an instance of EndpointOnlineOfflineLogItem from a dict
endpoint_online_offline_log_item_from_dict = EndpointOnlineOfflineLogItem.from_dict(endpoint_online_offline_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


