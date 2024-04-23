# NetworkProxyProfileProxiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass** | **str** | Proxy bypass expression. | [optional] [readonly] 
**proxy** | **str** | Proxy mode. | [optional] [readonly] 

## Example

```python
from endpoint_test_results.models.network_proxy_profile_proxies_inner import NetworkProxyProfileProxiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProxyProfileProxiesInner from a JSON string
network_proxy_profile_proxies_inner_instance = NetworkProxyProfileProxiesInner.from_json(json)
# print the JSON string representation of the object
print(NetworkProxyProfileProxiesInner.to_json())

# convert the object into a dict
network_proxy_profile_proxies_inner_dict = network_proxy_profile_proxies_inner_instance.to_dict()
# create an instance of NetworkProxyProfileProxiesInner from a dict
network_proxy_profile_proxies_inner_from_dict = NetworkProxyProfileProxiesInner.from_dict(network_proxy_profile_proxies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


