# GetDynamicTestResultPathvisAgentRound200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDetailDynamicTestResult]**](PathVisDetailDynamicTestResult.md) |  | [optional] 
**test** | [**DynamicTest**](DynamicTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.get_dynamic_test_result_pathvis_agent_round200_response import GetDynamicTestResultPathvisAgentRound200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDynamicTestResultPathvisAgentRound200Response from a JSON string
get_dynamic_test_result_pathvis_agent_round200_response_instance = GetDynamicTestResultPathvisAgentRound200Response.from_json(json)
# print the JSON string representation of the object
print(GetDynamicTestResultPathvisAgentRound200Response.to_json())

# convert the object into a dict
get_dynamic_test_result_pathvis_agent_round200_response_dict = get_dynamic_test_result_pathvis_agent_round200_response_instance.to_dict()
# create an instance of GetDynamicTestResultPathvisAgentRound200Response from a dict
get_dynamic_test_result_pathvis_agent_round200_response_from_dict = GetDynamicTestResultPathvisAgentRound200Response.from_dict(get_dynamic_test_result_pathvis_agent_round200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


