# SipServerTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SipServerTestResult]**](SipServerTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 

## Example

```python
from test_results.models.sip_server_test_results import SipServerTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of SipServerTestResults from a JSON string
sip_server_test_results_instance = SipServerTestResults.from_json(json)
# print the JSON string representation of the object
print(SipServerTestResults.to_json())

# convert the object into a dict
sip_server_test_results_dict = sip_server_test_results_instance.to_dict()
# create an instance of SipServerTestResults from a dict
sip_server_test_results_from_dict = SipServerTestResults.from_dict(sip_server_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


