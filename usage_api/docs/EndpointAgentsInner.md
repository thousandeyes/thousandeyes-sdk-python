# EndpointAgentsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **object** | Unique identifier of the account group owning the endpoint agents. | [optional] 
**account_group_name** | **object** | Name of the account group which owns the endpoint agents. | [optional] 
**endpoint_agents_used** | **int** | Number of endpoint agents owned by the specific account group in the usage period. | [optional] 

## Example

```python
from usage_api.models.endpoint_agents_inner import EndpointAgentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsInner from a JSON string
endpoint_agents_inner_instance = EndpointAgentsInner.from_json(json)
# print the JSON string representation of the object
print EndpointAgentsInner.to_json()

# convert the object into a dict
endpoint_agents_inner_dict = endpoint_agents_inner_instance.to_dict()
# create an instance of EndpointAgentsInner from a dict
endpoint_agents_inner_form_dict = endpoint_agents_inner.from_dict(endpoint_agents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


