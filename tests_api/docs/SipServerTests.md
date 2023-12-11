# SipServerTests


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[SipServerTest]**](SipServerTest.md) |  | [optional] 

## Example

```python
from tests_api.models.sip_server_tests import SipServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of SipServerTests from a JSON string
sip_server_tests_instance = SipServerTests.from_json(json)
# print the JSON string representation of the object
print SipServerTests.to_json()

# convert the object into a dict
sip_server_tests_dict = sip_server_tests_instance.to_dict()
# create an instance of SipServerTests from a dict
sip_server_tests_form_dict = sip_server_tests.from_dict(sip_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


