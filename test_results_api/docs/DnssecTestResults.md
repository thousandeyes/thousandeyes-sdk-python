# DnssecTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DnssecTestResult]**](DnssecTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 

## Example

```python
from test_results_api.models.dnssec_test_results import DnssecTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecTestResults from a JSON string
dnssec_test_results_instance = DnssecTestResults.from_json(json)
# print the JSON string representation of the object
print DnssecTestResults.to_json()

# convert the object into a dict
dnssec_test_results_dict = dnssec_test_results_instance.to_dict()
# create an instance of DnssecTestResults from a dict
dnssec_test_results_form_dict = dnssec_test_results.from_dict(dnssec_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


