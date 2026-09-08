# InstantTestRequestProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**tags** | **List[str]** | A list of test tag identifiers (get &#x60;id&#x60; from &#x60;/tags&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.instant_test_request_properties import InstantTestRequestProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InstantTestRequestProperties from a JSON string
instant_test_request_properties_instance = InstantTestRequestProperties.from_json(json)
# print the JSON string representation of the object
print(InstantTestRequestProperties.to_json())

# convert the object into a dict
instant_test_request_properties_dict = instant_test_request_properties_instance.to_dict()
# create an instance of InstantTestRequestProperties from a dict
instant_test_request_properties_from_dict = InstantTestRequestProperties.from_dict(instant_test_request_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


