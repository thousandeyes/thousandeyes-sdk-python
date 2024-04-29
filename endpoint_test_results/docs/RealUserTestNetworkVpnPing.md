# RealUserTestNetworkVpnPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_rtt** | **int** | Ping average response time. | [optional] [readonly] 
**max_rtt** | **int** | Ping maximum response time. | [optional] [readonly] 
**mean_dev_rtt** | **int** | Ping mean standard deviation response time. | [optional] [readonly] 
**min_rtt** | **int** | Ping minimum response time. | [optional] [readonly] 
**pkts_received** | **int** | Ping packets received. | [optional] [readonly] 
**pkts_sent** | **int** | Ping packets sent. | [optional] [readonly] 
**error** | **str** | Only present when there is an error. | [optional] [readonly] 
**info_flags** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from endpoint_test_results.models.real_user_test_network_vpn_ping import RealUserTestNetworkVpnPing

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserTestNetworkVpnPing from a JSON string
real_user_test_network_vpn_ping_instance = RealUserTestNetworkVpnPing.from_json(json)
# print the JSON string representation of the object
print(RealUserTestNetworkVpnPing.to_json())

# convert the object into a dict
real_user_test_network_vpn_ping_dict = real_user_test_network_vpn_ping_instance.to_dict()
# create an instance of RealUserTestNetworkVpnPing from a dict
real_user_test_network_vpn_ping_from_dict = RealUserTestNetworkVpnPing.from_dict(real_user_test_network_vpn_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

