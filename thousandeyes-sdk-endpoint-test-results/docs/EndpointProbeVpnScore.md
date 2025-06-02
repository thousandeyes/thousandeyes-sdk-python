# EndpointProbeVpnScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | A fine-grained score between 0 and 100. | [optional] 
**quality** | [**ApplicationScoreQuality**](ApplicationScoreQuality.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_probe_vpn_score import EndpointProbeVpnScore

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointProbeVpnScore from a JSON string
endpoint_probe_vpn_score_instance = EndpointProbeVpnScore.from_json(json)
# print the JSON string representation of the object
print(EndpointProbeVpnScore.to_json())

# convert the object into a dict
endpoint_probe_vpn_score_dict = endpoint_probe_vpn_score_instance.to_dict()
# create an instance of EndpointProbeVpnScore from a dict
endpoint_probe_vpn_score_from_dict = EndpointProbeVpnScore.from_dict(endpoint_probe_vpn_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


