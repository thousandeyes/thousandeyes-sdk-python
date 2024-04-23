# AgentSearchRequestSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[str]** | Returns only agents that are an exact match of the provided identifiers. | [optional] 
**agent_name** | **List[str]** | Returns only agents with the given name.  This is an exact match only.  | [optional] 
**computer_name** | **List[str]** | Returns only agents with the given computer name. This is an exact match only.  | [optional] 
**username** | **List[str]** | Returns only agents that have at least one user with a name. starting with the provided string. This is a case-insensitive prefix match.  | [optional] 
**platform** | [**List[Platform]**](Platform.md) | Filter on the platform on which the agent is running.  | [optional] 
**os_version** | **List[str]** | Case-insensitive prefix filter on the OS version. | [optional] 
**location_country_iso** | **List[str]** | Filter using the ISO country code of the location.  | [optional] 
**location_subdivision1_code** | **List[str]** | Filter using the code for the first level administrative division within  the country. In US/Canada this is the State, in UK it&#39;s the country e.g. &#x60;ENG&#x60;  | [optional] 
**location_city** | **List[str]** | This is a prefix match on the city name field. The endpoint expects this to contain the  name of the city in English. e.g. &#39;Paris&#39; or &#39;&#39;  | [optional] 

## Example

```python
from endpoint_agents.models.agent_search_request_search_filters import AgentSearchRequestSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchRequestSearchFilters from a JSON string
agent_search_request_search_filters_instance = AgentSearchRequestSearchFilters.from_json(json)
# print the JSON string representation of the object
print(AgentSearchRequestSearchFilters.to_json())

# convert the object into a dict
agent_search_request_search_filters_dict = agent_search_request_search_filters_instance.to_dict()
# create an instance of AgentSearchRequestSearchFilters from a dict
agent_search_request_search_filters_from_dict = AgentSearchRequestSearchFilters.from_dict(agent_search_request_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


