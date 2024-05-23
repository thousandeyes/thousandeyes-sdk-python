# NetworkProxyProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Proxy profile method. | [optional] [readonly] 
**proxies** | [**List[NetworkProxy]**](NetworkProxy.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_proxy_profile import NetworkProxyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProxyProfile from a JSON string
network_proxy_profile_instance = NetworkProxyProfile.from_json(json)
# print the JSON string representation of the object
print(NetworkProxyProfile.to_json())

# convert the object into a dict
network_proxy_profile_dict = network_proxy_profile_instance.to_dict()
# create an instance of NetworkProxyProfile from a dict
network_proxy_profile_from_dict = NetworkProxyProfile.from_dict(network_proxy_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


