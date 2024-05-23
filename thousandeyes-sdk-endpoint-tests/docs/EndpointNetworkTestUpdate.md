# EndpointNetworkTestUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**tcp_probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**port** | **int** | Target port. | [optional] [default to 49153]
**server** | **str** | Target domain name or IP address. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_network_test_update import EndpointNetworkTestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointNetworkTestUpdate from a JSON string
endpoint_network_test_update_instance = EndpointNetworkTestUpdate.from_json(json)
# print the JSON string representation of the object
print(EndpointNetworkTestUpdate.to_json())

# convert the object into a dict
endpoint_network_test_update_dict = endpoint_network_test_update_instance.to_dict()
# create an instance of EndpointNetworkTestUpdate from a dict
endpoint_network_test_update_from_dict = EndpointNetworkTestUpdate.from_dict(endpoint_network_test_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


