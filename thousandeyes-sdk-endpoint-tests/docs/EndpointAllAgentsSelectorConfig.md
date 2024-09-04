# EndpointAllAgentsSelectorConfig

Any agent selection object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_selector_type** | **str** |  | 
**max_machines** | **int** | Maximum number of agents which can execute the test. | [optional] [default to 25]

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAllAgentsSelectorConfig from a JSON string
endpoint_all_agents_selector_config_instance = EndpointAllAgentsSelectorConfig.from_json(json)
# print the JSON string representation of the object
print(EndpointAllAgentsSelectorConfig.to_json())

# convert the object into a dict
endpoint_all_agents_selector_config_dict = endpoint_all_agents_selector_config_instance.to_dict()
# create an instance of EndpointAllAgentsSelectorConfig from a dict
endpoint_all_agents_selector_config_from_dict = EndpointAllAgentsSelectorConfig.from_dict(endpoint_all_agents_selector_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


