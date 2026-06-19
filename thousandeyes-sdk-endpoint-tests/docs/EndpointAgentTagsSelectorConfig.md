# EndpointAgentTagsSelectorConfig

Agent tags selection object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_selector_type** | **str** |  | 
**max_machines** | **int** | Maximum number of agents which can execute the test. | [optional] [default to 25]
**endpoint_agent_labels** | **List[str]** | Deprecated. Use &#x60;tagIds&#x60; instead.  List of endpoint agent label IDs (obtained from &#x60;/endpoint/labels&#x60; endpoint), required when &#x60;agentSelectorType&#x60; is set to &#x60;agent-labels&#x60;.  | [optional] 
**tag_ids** | **List[str]** | List of tag IDs (obtained from &#x60;/tags&#x60; endpoint). | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_agent_tags_selector_config import EndpointAgentTagsSelectorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentTagsSelectorConfig from a JSON string
endpoint_agent_tags_selector_config_instance = EndpointAgentTagsSelectorConfig.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentTagsSelectorConfig.to_json())

# convert the object into a dict
endpoint_agent_tags_selector_config_dict = endpoint_agent_tags_selector_config_instance.to_dict()
# create an instance of EndpointAgentTagsSelectorConfig from a dict
endpoint_agent_tags_selector_config_from_dict = EndpointAgentTagsSelectorConfig.from_dict(endpoint_agent_tags_selector_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


