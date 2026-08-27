# WirelessOnboarding

Wireless onboarding timing metrics for a Wi-Fi connection attempt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dot11_auth_time_ms** | **int** | Time spent in the initial 802.11 authentication phase, in milliseconds. | [optional] [readonly] 
**dot11_assoc_time_ms** | **int** | Time spent in the 802.11 association phase, in milliseconds. | [optional] [readonly] 
**dot1x_auth_time_ms** | **int** | Time spent in the 802.1X authentication phase, in milliseconds. | [optional] [readonly] 
**eapol_key_time_ms** | **int** | Time spent in the four-way EAPOL key handshake, in milliseconds. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.wireless_onboarding import WirelessOnboarding

# TODO update the JSON string below
json = "{}"
# create an instance of WirelessOnboarding from a JSON string
wireless_onboarding_instance = WirelessOnboarding.from_json(json)
# print the JSON string representation of the object
print(WirelessOnboarding.to_json())

# convert the object into a dict
wireless_onboarding_dict = wireless_onboarding_instance.to_dict()
# create an instance of WirelessOnboarding from a dict
wireless_onboarding_from_dict = WirelessOnboarding.from_dict(wireless_onboarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


