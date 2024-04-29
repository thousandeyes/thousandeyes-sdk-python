# Agents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 

## Example

```python
from agents.models.agents import Agents

# TODO update the JSON string below
json = "{}"
# create an instance of Agents from a JSON string
agents_instance = Agents.from_json(json)
# print the JSON string representation of the object
print(Agents.to_json())

# convert the object into a dict
agents_dict = agents_instance.to_dict()
# create an instance of Agents from a dict
agents_from_dict = Agents.from_dict(agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


