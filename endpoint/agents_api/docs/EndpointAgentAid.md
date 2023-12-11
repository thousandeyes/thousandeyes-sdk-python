# EndpointAgentAid


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 

## Example

```python
from agents_api.models.endpoint_agent_aid import EndpointAgentAid

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentAid from a JSON string
endpoint_agent_aid_instance = EndpointAgentAid.from_json(json)
# print the JSON string representation of the object
print EndpointAgentAid.to_json()

# convert the object into a dict
endpoint_agent_aid_dict = endpoint_agent_aid_instance.to_dict()
# create an instance of EndpointAgentAid from a dict
endpoint_agent_aid_form_dict = endpoint_agent_aid.from_dict(endpoint_agent_aid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


