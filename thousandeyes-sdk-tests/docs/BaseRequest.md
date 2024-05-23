# BaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | Contains list of test label IDs (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint) | [optional] 
**shared_with_accounts** | **List[str]** | Contains list of account group IDs. Test is shared with the listed account groups (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint) | [optional] 
**alert_rules** | **List[str]** | List of alert rules IDs to apply to the test (get &#x60;ruleId&#x60; from &#x60;/alerts/rules&#x60; endpoint. If &#x60;alertsEnabled&#x60; is set to &#x60;true&#x60; and &#x60;alertRules&#x60; is not included on test creation or update, applicable user default alert rules will be used) | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.base_request import BaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRequest from a JSON string
base_request_instance = BaseRequest.from_json(json)
# print the JSON string representation of the object
print(BaseRequest.to_json())

# convert the object into a dict
base_request_dict = base_request_instance.to_dict()
# create an instance of BaseRequest from a dict
base_request_from_dict = BaseRequest.from_dict(base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


