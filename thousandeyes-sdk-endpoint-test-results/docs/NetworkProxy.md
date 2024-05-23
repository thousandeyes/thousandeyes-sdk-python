# NetworkProxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass** | **str** | Proxy bypass expression. | [optional] [readonly] 
**proxy** | **str** | Proxy mode. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_proxy import NetworkProxy

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProxy from a JSON string
network_proxy_instance = NetworkProxy.from_json(json)
# print the JSON string representation of the object
print(NetworkProxy.to_json())

# convert the object into a dict
network_proxy_dict = network_proxy_instance.to_dict()
# create an instance of NetworkProxy from a dict
network_proxy_from_dict = NetworkProxy.from_dict(network_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


