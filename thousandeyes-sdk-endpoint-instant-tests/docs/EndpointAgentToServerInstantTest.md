# EndpointAgentToServerInstantTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_selector_type** | [**EndpointTestAgentSelectorType**](EndpointTestAgentSelectorType.md) |  | [optional] 
**agents** | **List[str]** | List of endpoint agent IDs (obtained from &#x60;/endpoint/agents&#x60; endpoint). Required when &#x60;agentSelectorType&#x60; is set to &#x60;specific-agent&#x60;. | [optional] 
**endpoint_agent_labels** | **List[str]** | List of endpoint agent label IDs (obtained from &#x60;/endpoint/labels&#x60; endpoint), required when &#x60;agentSelectorType&#x60; is set to &#x60;agent-labels&#x60;. | [optional] 
**max_machines** | **int** | Maximum number of agents which can execute the test. | [optional] [default to 25]
**test_name** | **str** | Name of the test. | 
**server_name** | **str** | A server address without a protocol or IP address. | 
**port** | **int** | Port number. | [optional] [default to 443]

## Example

```python
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_instant_test import EndpointAgentToServerInstantTest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentToServerInstantTest from a JSON string
endpoint_agent_to_server_instant_test_instance = EndpointAgentToServerInstantTest.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentToServerInstantTest.to_json())

# convert the object into a dict
endpoint_agent_to_server_instant_test_dict = endpoint_agent_to_server_instant_test_instance.to_dict()
# create an instance of EndpointAgentToServerInstantTest from a dict
endpoint_agent_to_server_instant_test_from_dict = EndpointAgentToServerInstantTest.from_dict(endpoint_agent_to_server_instant_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


