# EndpointProxiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxies** | [**List[EndpointProxy]**](EndpointProxy.md) | Proxy settings configured for endpoint agents. | 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_proxies_response import EndpointProxiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointProxiesResponse from a JSON string
endpoint_proxies_response_instance = EndpointProxiesResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointProxiesResponse.to_json())

# convert the object into a dict
endpoint_proxies_response_dict = endpoint_proxies_response_instance.to_dict()
# create an instance of EndpointProxiesResponse from a dict
endpoint_proxies_response_from_dict = EndpointProxiesResponse.from_dict(endpoint_proxies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


