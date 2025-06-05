# EndpointProbeProxyScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | A fine-grained score between 0 and 100. | [optional] 
**quality** | [**ApplicationScoreQuality**](ApplicationScoreQuality.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_probe_proxy_score import EndpointProbeProxyScore

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointProbeProxyScore from a JSON string
endpoint_probe_proxy_score_instance = EndpointProbeProxyScore.from_json(json)
# print the JSON string representation of the object
print(EndpointProbeProxyScore.to_json())

# convert the object into a dict
endpoint_probe_proxy_score_dict = endpoint_probe_proxy_score_instance.to_dict()
# create an instance of EndpointProbeProxyScore from a dict
endpoint_probe_proxy_score_from_dict = EndpointProbeProxyScore.from_dict(endpoint_probe_proxy_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


