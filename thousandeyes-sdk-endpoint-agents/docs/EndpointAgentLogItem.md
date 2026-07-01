# EndpointAgentLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the log item. | [optional] [readonly] 
**agent_log_item_type** | [**EndpointAgentLogItemType**](EndpointAgentLogItemType.md) |  | [optional] 
**timestamp_ms** | **int** | Time when the log item was recorded, in milliseconds since the Unix epoch. | [optional] [readonly] 
**wifi_log_item** | [**EndpointWifiLogItem**](EndpointWifiLogItem.md) |  | [optional] 
**vpn_log_item** | [**EndpointVpnLogItem**](EndpointVpnLogItem.md) |  | [optional] 
**online_offline_log_item** | [**EndpointOnlineOfflineLogItem**](EndpointOnlineOfflineLogItem.md) |  | [optional] 
**state_changes_log_item** | [**EndpointStateChangesLogItem**](EndpointStateChangesLogItem.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_log_item import EndpointAgentLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentLogItem from a JSON string
endpoint_agent_log_item_instance = EndpointAgentLogItem.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentLogItem.to_json())

# convert the object into a dict
endpoint_agent_log_item_dict = endpoint_agent_log_item_instance.to_dict()
# create an instance of EndpointAgentLogItem from a dict
endpoint_agent_log_item_from_dict = EndpointAgentLogItem.from_dict(endpoint_agent_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


