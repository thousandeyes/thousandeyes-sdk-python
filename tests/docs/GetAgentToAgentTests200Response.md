# GetAgentToAgentTests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedAgentToAgentTest]**](UnexpandedAgentToAgentTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests.models.get_agent_to_agent_tests200_response import GetAgentToAgentTests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentToAgentTests200Response from a JSON string
get_agent_to_agent_tests200_response_instance = GetAgentToAgentTests200Response.from_json(json)
# print the JSON string representation of the object
print(GetAgentToAgentTests200Response.to_json())

# convert the object into a dict
get_agent_to_agent_tests200_response_dict = get_agent_to_agent_tests200_response_instance.to_dict()
# create an instance of GetAgentToAgentTests200Response from a dict
get_agent_to_agent_tests200_response_from_dict = GetAgentToAgentTests200Response.from_dict(get_agent_to_agent_tests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


