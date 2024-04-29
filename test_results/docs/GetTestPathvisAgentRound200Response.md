# GetTestPathvisAgentRound200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDetailTestResult]**](PathVisDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from test_results.models.get_test_pathvis_agent_round200_response import GetTestPathvisAgentRound200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestPathvisAgentRound200Response from a JSON string
get_test_pathvis_agent_round200_response_instance = GetTestPathvisAgentRound200Response.from_json(json)
# print the JSON string representation of the object
print(GetTestPathvisAgentRound200Response.to_json())

# convert the object into a dict
get_test_pathvis_agent_round200_response_dict = get_test_pathvis_agent_round200_response_instance.to_dict()
# create an instance of GetTestPathvisAgentRound200Response from a dict
get_test_pathvis_agent_round200_response_from_dict = GetTestPathvisAgentRound200Response.from_dict(get_test_pathvis_agent_round200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

