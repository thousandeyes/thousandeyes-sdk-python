# InstantTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 
**agents** | [**List[TestAgent]**](TestAgent.md) | A list of objects with &#x60;agentId&#x60; (required) and &#x60;sourceIpAddress&#x60; (optional). | 

## Example

```python
from thousandeyes_sdk.instant_tests.models.instant_test_request import InstantTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantTestRequest from a JSON string
instant_test_request_instance = InstantTestRequest.from_json(json)
# print the JSON string representation of the object
print(InstantTestRequest.to_json())

# convert the object into a dict
instant_test_request_dict = instant_test_request_instance.to_dict()
# create an instance of InstantTestRequest from a dict
instant_test_request_from_dict = InstantTestRequest.from_dict(instant_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


