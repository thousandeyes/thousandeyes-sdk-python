# EndpointHttpTestUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**tcp_probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**url** | **str** | Target for the test. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_test_update import EndpointHttpTestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointHttpTestUpdate from a JSON string
endpoint_http_test_update_instance = EndpointHttpTestUpdate.from_json(json)
# print the JSON string representation of the object
print(EndpointHttpTestUpdate.to_json())

# convert the object into a dict
endpoint_http_test_update_dict = endpoint_http_test_update_instance.to_dict()
# create an instance of EndpointHttpTestUpdate from a dict
endpoint_http_test_update_from_dict = EndpointHttpTestUpdate.from_dict(endpoint_http_test_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


