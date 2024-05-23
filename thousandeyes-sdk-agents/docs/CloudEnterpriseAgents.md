# CloudEnterpriseAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[CloudEnterpriseAgent]**](CloudEnterpriseAgent.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.cloud_enterprise_agents import CloudEnterpriseAgents

# TODO update the JSON string below
json = "{}"
# create an instance of CloudEnterpriseAgents from a JSON string
cloud_enterprise_agents_instance = CloudEnterpriseAgents.from_json(json)
# print the JSON string representation of the object
print(CloudEnterpriseAgents.to_json())

# convert the object into a dict
cloud_enterprise_agents_dict = cloud_enterprise_agents_instance.to_dict()
# create an instance of CloudEnterpriseAgents from a dict
cloud_enterprise_agents_from_dict = CloudEnterpriseAgents.from_dict(cloud_enterprise_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


