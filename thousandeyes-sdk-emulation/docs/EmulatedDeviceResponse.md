# EmulatedDeviceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**EmulatedDeviceCategory**](EmulatedDeviceCategory.md) |  | 
**width** | **int** | The width of the display of the emulated device. | 
**height** | **int** | The height of the display of the emulated device. | 
**name** | **str** | The device name | [optional] 
**code_name** | **str** | A code corresponding to the device name. | [optional] 
**id** | **str** | ID of the emulated device. | [optional] 
**available_user_agents** | **List[str]** | A list of user-agent strings for this emulated device. | [optional] 
**default_user_agent_template** | **str** | The default user-agent template to use for this device. | [optional] 

## Example

```python
from thousandeyes_sdk.emulation.models.emulated_device_response import EmulatedDeviceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmulatedDeviceResponse from a JSON string
emulated_device_response_instance = EmulatedDeviceResponse.from_json(json)
# print the JSON string representation of the object
print(EmulatedDeviceResponse.to_json())

# convert the object into a dict
emulated_device_response_dict = emulated_device_response_instance.to_dict()
# create an instance of EmulatedDeviceResponse from a dict
emulated_device_response_from_dict = EmulatedDeviceResponse.from_dict(emulated_device_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


