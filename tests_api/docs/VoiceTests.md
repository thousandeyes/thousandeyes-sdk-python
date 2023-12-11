# VoiceTests


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[VoiceTest]**](VoiceTest.md) |  | [optional] 

## Example

```python
from tests_api.models.voice_tests import VoiceTests

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceTests from a JSON string
voice_tests_instance = VoiceTests.from_json(json)
# print the JSON string representation of the object
print VoiceTests.to_json()

# convert the object into a dict
voice_tests_dict = voice_tests_instance.to_dict()
# create an instance of VoiceTests from a dict
voice_tests_form_dict = voice_tests.from_dict(voice_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


