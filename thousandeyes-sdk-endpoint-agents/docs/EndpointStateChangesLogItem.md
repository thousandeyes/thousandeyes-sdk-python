# EndpointStateChangesLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_item_type** | [**EndpointStateChangesLogItemType**](EndpointStateChangesLogItemType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_state_changes_log_item import EndpointStateChangesLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStateChangesLogItem from a JSON string
endpoint_state_changes_log_item_instance = EndpointStateChangesLogItem.from_json(json)
# print the JSON string representation of the object
print(EndpointStateChangesLogItem.to_json())

# convert the object into a dict
endpoint_state_changes_log_item_dict = endpoint_state_changes_log_item_instance.to_dict()
# create an instance of EndpointStateChangesLogItem from a dict
endpoint_state_changes_log_item_from_dict = EndpointStateChangesLogItem.from_dict(endpoint_state_changes_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


