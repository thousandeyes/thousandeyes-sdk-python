# VoiceTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedVoiceTest]**](UnexpandedVoiceTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.voice_tests import VoiceTests

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceTests from a JSON string
voice_tests_instance = VoiceTests.from_json(json)
# print the JSON string representation of the object
print(VoiceTests.to_json())

# convert the object into a dict
voice_tests_dict = voice_tests_instance.to_dict()
# create an instance of VoiceTests from a dict
voice_tests_from_dict = VoiceTests.from_dict(voice_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


