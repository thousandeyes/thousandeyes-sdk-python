# DeploymentInfoItem

A key-value entry containing deployment metadata reported by the endpoint agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Name of the deployment metadata item. | 
**value** | **str** | Agent-reported value associated with &#x60;key&#x60;. | 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.deployment_info_item import DeploymentInfoItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentInfoItem from a JSON string
deployment_info_item_instance = DeploymentInfoItem.from_json(json)
# print the JSON string representation of the object
print(DeploymentInfoItem.to_json())

# convert the object into a dict
deployment_info_item_dict = deployment_info_item_instance.to_dict()
# create an instance of DeploymentInfoItem from a dict
deployment_info_item_from_dict = DeploymentInfoItem.from_dict(deployment_info_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


