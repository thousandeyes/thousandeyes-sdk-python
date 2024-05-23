# EndpointHttpDataPointScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_score** | **float** | Fine grained score between 0-100 based on &#x60;time to first byte&#x60; metric | [optional] 
**quality** | [**ApplicationScoreQuality**](ApplicationScoreQuality.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_data_point_score import EndpointHttpDataPointScore

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointHttpDataPointScore from a JSON string
endpoint_http_data_point_score_instance = EndpointHttpDataPointScore.from_json(json)
# print the JSON string representation of the object
print(EndpointHttpDataPointScore.to_json())

# convert the object into a dict
endpoint_http_data_point_score_dict = endpoint_http_data_point_score_instance.to_dict()
# create an instance of EndpointHttpDataPointScore from a dict
endpoint_http_data_point_score_from_dict = EndpointHttpDataPointScore.from_dict(endpoint_http_data_point_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


