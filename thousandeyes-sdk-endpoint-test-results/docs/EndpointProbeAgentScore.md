# EndpointProbeAgentScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | A fine-grained score between 0 and 100. | [optional] 
**quality** | [**ApplicationScoreQuality**](ApplicationScoreQuality.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_probe_agent_score import EndpointProbeAgentScore

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointProbeAgentScore from a JSON string
endpoint_probe_agent_score_instance = EndpointProbeAgentScore.from_json(json)
# print the JSON string representation of the object
print(EndpointProbeAgentScore.to_json())

# convert the object into a dict
endpoint_probe_agent_score_dict = endpoint_probe_agent_score_instance.to_dict()
# create an instance of EndpointProbeAgentScore from a dict
endpoint_probe_agent_score_from_dict = EndpointProbeAgentScore.from_dict(endpoint_probe_agent_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


