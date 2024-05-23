# EndpointClient

Information about the user who has the agent installed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_profile** | [**EndpointUserProfile**](EndpointUserProfile.md) |  | [optional] 
**browser_extensions** | [**List[EndpointBrowserExtension]**](EndpointBrowserExtension.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_client import EndpointClient

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointClient from a JSON string
endpoint_client_instance = EndpointClient.from_json(json)
# print the JSON string representation of the object
print(EndpointClient.to_json())

# convert the object into a dict
endpoint_client_dict = endpoint_client_instance.to_dict()
# create an instance of EndpointClient from a dict
endpoint_client_from_dict = EndpointClient.from_dict(endpoint_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


