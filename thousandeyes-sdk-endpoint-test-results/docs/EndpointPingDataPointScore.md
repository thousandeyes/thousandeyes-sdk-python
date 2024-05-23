# EndpointPingDataPointScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_score** | **float** | Fine grained score between 0-100 based on metrics (latency, jitter, loss) | [optional] 
**quality** | [**ApplicationScoreQuality**](ApplicationScoreQuality.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_ping_data_point_score import EndpointPingDataPointScore

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointPingDataPointScore from a JSON string
endpoint_ping_data_point_score_instance = EndpointPingDataPointScore.from_json(json)
# print the JSON string representation of the object
print(EndpointPingDataPointScore.to_json())

# convert the object into a dict
endpoint_ping_data_point_score_dict = endpoint_ping_data_point_score_instance.to_dict()
# create an instance of EndpointPingDataPointScore from a dict
endpoint_ping_data_point_score_from_dict = EndpointPingDataPointScore.from_dict(endpoint_ping_data_point_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


