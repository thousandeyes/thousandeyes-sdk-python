# FtpServerTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedFtpServerTest]**](UnexpandedFtpServerTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.ftp_server_tests import FtpServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of FtpServerTests from a JSON string
ftp_server_tests_instance = FtpServerTests.from_json(json)
# print the JSON string representation of the object
print(FtpServerTests.to_json())

# convert the object into a dict
ftp_server_tests_dict = ftp_server_tests_instance.to_dict()
# create an instance of FtpServerTests from a dict
ftp_server_tests_from_dict = FtpServerTests.from_dict(ftp_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


