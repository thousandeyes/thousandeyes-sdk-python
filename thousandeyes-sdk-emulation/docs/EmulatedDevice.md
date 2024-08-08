# EmulatedDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**EmulatedDeviceCategory**](EmulatedDeviceCategory.md) |  | 
**width** | **int** | The width of the display of the emulated device. | 
**height** | **int** | The height of the display of the emulated device. | 

## Example

```python
from thousandeyes_sdk.emulation.models.emulated_device import EmulatedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of EmulatedDevice from a JSON string
emulated_device_instance = EmulatedDevice.from_json(json)
# print the JSON string representation of the object
print(EmulatedDevice.to_json())

# convert the object into a dict
emulated_device_dict = emulated_device_instance.to_dict()
# create an instance of EmulatedDevice from a dict
emulated_device_from_dict = EmulatedDevice.from_dict(emulated_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


