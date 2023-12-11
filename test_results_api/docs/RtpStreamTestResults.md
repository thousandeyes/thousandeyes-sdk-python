# RtpStreamTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RtpStreamTestResult]**](RtpStreamTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 

## Example

```python
from test_results_api.models.rtp_stream_test_results import RtpStreamTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of RtpStreamTestResults from a JSON string
rtp_stream_test_results_instance = RtpStreamTestResults.from_json(json)
# print the JSON string representation of the object
print RtpStreamTestResults.to_json()

# convert the object into a dict
rtp_stream_test_results_dict = rtp_stream_test_results_instance.to_dict()
# create an instance of RtpStreamTestResults from a dict
rtp_stream_test_results_form_dict = rtp_stream_test_results.from_dict(rtp_stream_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


