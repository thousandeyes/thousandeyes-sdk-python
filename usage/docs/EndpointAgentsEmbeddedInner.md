# EndpointAgentsEmbeddedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **object** | Unique identifier of the account group that owns the embedded endpoint agents. | [optional] 
**account_group_name** | **object** | Name of the account group that owns the embedded endpoint agents. | [optional] 
**endpoint_agents_embedded_used** | **int** | Number of endpoint agents embedded owned by the specific account group in the usage period. | [optional] 

## Example

```python
from usage.models.endpoint_agents_embedded_inner import EndpointAgentsEmbeddedInner

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsEmbeddedInner from a JSON string
endpoint_agents_embedded_inner_instance = EndpointAgentsEmbeddedInner.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentsEmbeddedInner.to_json())

# convert the object into a dict
endpoint_agents_embedded_inner_dict = endpoint_agents_embedded_inner_instance.to_dict()
# create an instance of EndpointAgentsEmbeddedInner from a dict
endpoint_agents_embedded_inner_from_dict = EndpointAgentsEmbeddedInner.from_dict(endpoint_agents_embedded_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


