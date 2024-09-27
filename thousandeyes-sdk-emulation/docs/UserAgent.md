# UserAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** | The name of the web browser. | [optional] 
**os** | **str** | The operating system for the user-agent HTTP header. | [optional] 
**value** | **str** | The text of the user-agent header. | [optional] 

## Example

```python
from thousandeyes_sdk.emulation.models.user_agent import UserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgent from a JSON string
user_agent_instance = UserAgent.from_json(json)
# print the JSON string representation of the object
print(UserAgent.to_json())

# convert the object into a dict
user_agent_dict = user_agent_instance.to_dict()
# create an instance of UserAgent from a dict
user_agent_from_dict = UserAgent.from_dict(user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


