# UpdateBgpTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**labels** | **List[str]** | Contains list of test label IDs (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint) | [optional] 
**shared_with_accounts** | **List[str]** | Contains list of account group IDs. Test is shared with the listed account groups (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint) | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**monitors** | **List[str]** | Contains list of BGP monitor IDs (get &#x60;monitorId&#x60; from &#x60;/monitors&#x60; endpoint) | [optional] 
**include_covered_prefixes** | **bool** | Indicate if queries for subprefixes detected under this prefix should included. | [optional] 
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**alert_rules** | **List[str]** | List of alert rules IDs to apply to the test (get &#x60;ruleId&#x60; from &#x60;/alerts/rules&#x60; endpoint. If &#x60;alertsEnabled&#x60; is set to &#x60;true&#x60; and &#x60;alertRules&#x60; is not included on test creation or update, applicable user default alert rules will be used) | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.update_bgp_test_request import UpdateBgpTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBgpTestRequest from a JSON string
update_bgp_test_request_instance = UpdateBgpTestRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBgpTestRequest.to_json())

# convert the object into a dict
update_bgp_test_request_dict = update_bgp_test_request_instance.to_dict()
# create an instance of UpdateBgpTestRequest from a dict
update_bgp_test_request_from_dict = UpdateBgpTestRequest.from_dict(update_bgp_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


