# SourceInterfaceInstantTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**tags** | **List[str]** | A list of test tag identifiers (get &#x60;id&#x60; from &#x60;/tags&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 
**agents** | [**List[TestAgentWithSourceIpAddress]**](TestAgentWithSourceIpAddress.md) | Agents assigned to the test. To select a source interface, set &#x60;sourceIpAddress&#x60; on the same object as its &#x60;agentId&#x60;. | 

## Example

```python
from thousandeyes_sdk.instant_tests.models.source_interface_instant_test_request import SourceInterfaceInstantTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SourceInterfaceInstantTestRequest from a JSON string
source_interface_instant_test_request_instance = SourceInterfaceInstantTestRequest.from_json(json)
# print the JSON string representation of the object
print(SourceInterfaceInstantTestRequest.to_json())

# convert the object into a dict
source_interface_instant_test_request_dict = source_interface_instant_test_request_instance.to_dict()
# create an instance of SourceInterfaceInstantTestRequest from a dict
source_interface_instant_test_request_from_dict = SourceInterfaceInstantTestRequest.from_dict(source_interface_instant_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


