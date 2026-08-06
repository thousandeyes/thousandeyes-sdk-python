# ConnectedDevices

Configuration for Connected Devices metric data in the stream integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag to enable or disable Connected Devices data. | [default to False]

## Example

```python
from thousandeyes_sdk.streaming.models.connected_devices import ConnectedDevices

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedDevices from a JSON string
connected_devices_instance = ConnectedDevices.from_json(json)
# print the JSON string representation of the object
print(ConnectedDevices.to_json())

# convert the object into a dict
connected_devices_dict = connected_devices_instance.to_dict()
# create an instance of ConnectedDevices from a dict
connected_devices_from_dict = ConnectedDevices.from_dict(connected_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


