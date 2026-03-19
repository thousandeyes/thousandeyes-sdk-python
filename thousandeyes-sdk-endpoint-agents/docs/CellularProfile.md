# CellularProfile

Cellular network profile information for a mobile endpoint agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_name** | **str** | Carrier name | [optional] 
**network_gen** | **str** | Cellular network generation. | [optional] 
**network_subtype** | **str** | A real network subtype. It may be different from an advertised network type. | [optional] 
**advertised_network_gen** | **str** | Cellular network generation. | [optional] 
**advertised_network_subtype** | **str** | Advertised Network subtype | [optional] 
**rssi** | **float** | Received Signal Strength Indicator in dBm. Values are always negative. | [optional] 
**rsrp** | **float** | Reference Signal Received Power in dBm. Values are always negative. | [optional] 
**rscp** | **float** | Received Signal Code Power in dBm. Values are always negative or zero. | [optional] 
**rsrq** | **float** | Reference Signal Received Quality in dBm. Values are always negative. | [optional] 
**sinr** | **float** | Signal to Interference and Noise Ratio in dBm. It can be negative or positive. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.cellular_profile import CellularProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CellularProfile from a JSON string
cellular_profile_instance = CellularProfile.from_json(json)
# print the JSON string representation of the object
print(CellularProfile.to_json())

# convert the object into a dict
cellular_profile_dict = cellular_profile_instance.to_dict()
# create an instance of CellularProfile from a dict
cellular_profile_from_dict = CellularProfile.from_dict(cellular_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


