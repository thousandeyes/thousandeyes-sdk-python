# ApiAffectedAgent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from internet_insights_api.models.api_affected_agent import ApiAffectedAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAffectedAgent from a JSON string
api_affected_agent_instance = ApiAffectedAgent.from_json(json)
# print the JSON string representation of the object
print ApiAffectedAgent.to_json()

# convert the object into a dict
api_affected_agent_dict = api_affected_agent_instance.to_dict()
# create an instance of ApiAffectedAgent from a dict
api_affected_agent_form_dict = api_affected_agent.from_dict(api_affected_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


