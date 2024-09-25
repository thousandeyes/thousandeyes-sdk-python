# EndpointAgentSelectorConfig

Agents selection object based on agentSelectorType.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_selector_type** | **str** |  | 
**max_machines** | **int** | Maximum number of agents which can execute the test. | [optional] [default to 25]
**endpoint_agent_labels** | **List[str]** | List of endpoint agent label IDs (obtained from &#x60;/endpoint/labels&#x60; endpoint), required when &#x60;agentSelectorType&#x60; is set to &#x60;agent-labels&#x60;. | [optional] 
**agents** | **List[str]** | List of endpoint agent IDs (obtained from &#x60;/endpoint/agents&#x60; endpoint). Required when &#x60;agentSelectorType&#x60; is set to &#x60;specific-agent&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentSelectorConfig from a JSON string
endpoint_agent_selector_config_instance = EndpointAgentSelectorConfig.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentSelectorConfig.to_json())

# convert the object into a dict
endpoint_agent_selector_config_dict = endpoint_agent_selector_config_instance.to_dict()
# create an instance of EndpointAgentSelectorConfig from a dict
endpoint_agent_selector_config_from_dict = EndpointAgentSelectorConfig.from_dict(endpoint_agent_selector_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


