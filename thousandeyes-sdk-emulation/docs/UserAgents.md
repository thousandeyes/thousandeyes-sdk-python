# UserAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agents** | [**List[UserAgent]**](UserAgent.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.emulation.models.user_agents import UserAgents

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgents from a JSON string
user_agents_instance = UserAgents.from_json(json)
# print the JSON string representation of the object
print(UserAgents.to_json())

# convert the object into a dict
user_agents_dict = user_agents_instance.to_dict()
# create an instance of UserAgents from a dict
user_agents_from_dict = UserAgents.from_dict(user_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


