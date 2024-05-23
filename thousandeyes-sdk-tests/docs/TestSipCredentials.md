# TestSipCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_user** | **str** | Username for authentication with SIP server. | [optional] 
**password** | **str** | Password for Basic/NTLM authentication. | [optional] 
**port** | **int** | Target port. | [default to 49153]
**protocol** | [**SipTestProtocol**](SipTestProtocol.md) |  | [optional] 
**sip_registrar** | **str** | SIP server to be tested, specified by domain name or IP address. | [optional] 
**user** | **str** | Username for SIP registration, should be unique within a ThousandEyes account group. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_sip_credentials import TestSipCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TestSipCredentials from a JSON string
test_sip_credentials_instance = TestSipCredentials.from_json(json)
# print the JSON string representation of the object
print(TestSipCredentials.to_json())

# convert the object into a dict
test_sip_credentials_dict = test_sip_credentials_instance.to_dict()
# create an instance of TestSipCredentials from a dict
test_sip_credentials_from_dict = TestSipCredentials.from_dict(test_sip_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


