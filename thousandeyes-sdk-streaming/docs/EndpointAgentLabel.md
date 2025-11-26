# EndpointAgentLabel

Endpoint Agent label configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The label ID of Endpoint Agent labels. | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.endpoint_agent_label import EndpointAgentLabel

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentLabel from a JSON string
endpoint_agent_label_instance = EndpointAgentLabel.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentLabel.to_json())

# convert the object into a dict
endpoint_agent_label_dict = endpoint_agent_label_instance.to_dict()
# create an instance of EndpointAgentLabel from a dict
endpoint_agent_label_from_dict = EndpointAgentLabel.from_dict(endpoint_agent_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


