# EndpointAgentToServerTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[EndpointAgentToServerTest]**](EndpointAgentToServerTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_agent_to_server_tests import EndpointAgentToServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentToServerTests from a JSON string
endpoint_agent_to_server_tests_instance = EndpointAgentToServerTests.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentToServerTests.to_json())

# convert the object into a dict
endpoint_agent_to_server_tests_dict = endpoint_agent_to_server_tests_instance.to_dict()
# create an instance of EndpointAgentToServerTests from a dict
endpoint_agent_to_server_tests_from_dict = EndpointAgentToServerTests.from_dict(endpoint_agent_to_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


