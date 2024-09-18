# EndpointSpecificAgentsSelectorConfig

Specific agents selection object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_selector_type** | **str** |  | 
**max_machines** | **int** | Maximum number of agents which can execute the test. | [optional] [default to 25]
**agents** | **List[str]** | List of endpoint agent IDs (obtained from &#x60;/endpoint/agents&#x60; endpoint). Required when &#x60;agentSelectorType&#x60; is set to &#x60;specific-agent&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointSpecificAgentsSelectorConfig from a JSON string
endpoint_specific_agents_selector_config_instance = EndpointSpecificAgentsSelectorConfig.from_json(json)
# print the JSON string representation of the object
print(EndpointSpecificAgentsSelectorConfig.to_json())

# convert the object into a dict
endpoint_specific_agents_selector_config_dict = endpoint_specific_agents_selector_config_instance.to_dict()
# create an instance of EndpointSpecificAgentsSelectorConfig from a dict
endpoint_specific_agents_selector_config_from_dict = EndpointSpecificAgentsSelectorConfig.from_dict(endpoint_specific_agents_selector_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


