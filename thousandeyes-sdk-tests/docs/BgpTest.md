# BgpTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event.  **Note**: **Saved Events** are now called **Private Snapshots** in the user interface. This change does not affect API.  | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**labels** | [**List[TestLabel]**](TestLabel.md) | Labels to which the test is assigned. This field is not returned for Instant Tests. | [optional] [readonly] 
**shared_with_accounts** | [**List[SharedWithAccount]**](SharedWithAccount.md) |  | [optional] [readonly] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**monitors** | [**List[Monitor]**](Monitor.md) | Contains list of enabled BGP monitors. | [optional] [readonly] 
**include_covered_prefixes** | **bool** | Indicate if queries for subprefixes detected under this prefix should included. | [optional] 
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**alert_rules** | [**List[AlertRule]**](AlertRule.md) | A list of enabled alert rule objects. | [optional] 
**prefix** | **str** | a.b.c.d is a network address, with the prefix length defined as e. Prefixes can be any length from 8 to 24. | 

## Example

```python
from thousandeyes_sdk.tests.models.bgp_test import BgpTest

# TODO update the JSON string below
json = "{}"
# create an instance of BgpTest from a JSON string
bgp_test_instance = BgpTest.from_json(json)
# print the JSON string representation of the object
print(BgpTest.to_json())

# convert the object into a dict
bgp_test_dict = bgp_test_instance.to_dict()
# create an instance of BgpTest from a dict
bgp_test_from_dict = BgpTest.from_dict(bgp_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


