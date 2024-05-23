# EndpointDynamicTestUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**tcp_probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**application** | **str** | Which supported application to monitor, can be one of &#x60;webex&#x60;, &#x60;zoom&#x60;, &#x60;microsoft-teams&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_dynamic_test_update import EndpointDynamicTestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDynamicTestUpdate from a JSON string
endpoint_dynamic_test_update_instance = EndpointDynamicTestUpdate.from_json(json)
# print the JSON string representation of the object
print(EndpointDynamicTestUpdate.to_json())

# convert the object into a dict
endpoint_dynamic_test_update_dict = endpoint_dynamic_test_update_instance.to_dict()
# create an instance of EndpointDynamicTestUpdate from a dict
endpoint_dynamic_test_update_from_dict = EndpointDynamicTestUpdate.from_dict(endpoint_dynamic_test_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


