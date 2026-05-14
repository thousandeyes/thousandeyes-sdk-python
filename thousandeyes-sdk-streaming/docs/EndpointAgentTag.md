# EndpointAgentTag

Endpoint Agent tag configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The tag ID of Endpoint Agent tags. | 

## Example

```python
from thousandeyes_sdk.streaming.models.endpoint_agent_tag import EndpointAgentTag

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentTag from a JSON string
endpoint_agent_tag_instance = EndpointAgentTag.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentTag.to_json())

# convert the object into a dict
endpoint_agent_tag_dict = endpoint_agent_tag_instance.to_dict()
# create an instance of EndpointAgentTag from a dict
endpoint_agent_tag_from_dict = EndpointAgentTag.from_dict(endpoint_agent_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


