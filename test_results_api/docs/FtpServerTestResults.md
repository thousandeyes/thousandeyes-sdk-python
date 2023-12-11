# FtpServerTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FtpServerTestResult]**](FtpServerTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 

## Example

```python
from test_results_api.models.ftp_server_test_results import FtpServerTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of FtpServerTestResults from a JSON string
ftp_server_test_results_instance = FtpServerTestResults.from_json(json)
# print the JSON string representation of the object
print FtpServerTestResults.to_json()

# convert the object into a dict
ftp_server_test_results_dict = ftp_server_test_results_instance.to_dict()
# create an instance of FtpServerTestResults from a dict
ftp_server_test_results_form_dict = ftp_server_test_results.from_dict(ftp_server_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


