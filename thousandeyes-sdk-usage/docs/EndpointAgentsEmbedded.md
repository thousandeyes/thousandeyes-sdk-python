# EndpointAgentsEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Unique identifier of the account group that owns the embedded endpoint agents. | [optional] 
**account_group_name** | **str** | Name of the account group that owns the embedded endpoint agents. | [optional] 
**endpoint_agents_embedded_used** | **int** | Number of endpoint agents embedded owned by the specific account group in the usage period. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.endpoint_agents_embedded import EndpointAgentsEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsEmbedded from a JSON string
endpoint_agents_embedded_instance = EndpointAgentsEmbedded.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentsEmbedded.to_json())

# convert the object into a dict
endpoint_agents_embedded_dict = endpoint_agents_embedded_instance.to_dict()
# create an instance of EndpointAgentsEmbedded from a dict
endpoint_agents_embedded_from_dict = EndpointAgentsEmbedded.from_dict(endpoint_agents_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


