# TestUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**tcp_probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.test_update import TestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TestUpdate from a JSON string
test_update_instance = TestUpdate.from_json(json)
# print the JSON string representation of the object
print(TestUpdate.to_json())

# convert the object into a dict
test_update_dict = test_update_instance.to_dict()
# create an instance of TestUpdate from a dict
test_update_from_dict = TestUpdate.from_dict(test_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


