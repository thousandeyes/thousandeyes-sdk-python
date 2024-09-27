# EmulatedDeviceResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emulated_devices** | [**List[EmulatedDeviceResponse]**](EmulatedDeviceResponse.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.emulation.models.emulated_device_responses import EmulatedDeviceResponses

# TODO update the JSON string below
json = "{}"
# create an instance of EmulatedDeviceResponses from a JSON string
emulated_device_responses_instance = EmulatedDeviceResponses.from_json(json)
# print the JSON string representation of the object
print(EmulatedDeviceResponses.to_json())

# convert the object into a dict
emulated_device_responses_dict = emulated_device_responses_instance.to_dict()
# create an instance of EmulatedDeviceResponses from a dict
emulated_device_responses_from_dict = EmulatedDeviceResponses.from_dict(emulated_device_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


