# UnexpandedBgpTest


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
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**include_covered_prefixes** | **bool** | Indicate if queries for subprefixes detected under this prefix should included. | [optional] 
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**prefix** | **str** | a.b.c.d is a network address, with the prefix length defined as e. Prefixes can be any length from 8 to 24. | 

## Example

```python
from thousandeyes_sdk.tests.models.unexpanded_bgp_test import UnexpandedBgpTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedBgpTest from a JSON string
unexpanded_bgp_test_instance = UnexpandedBgpTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedBgpTest.to_json())

# convert the object into a dict
unexpanded_bgp_test_dict = unexpanded_bgp_test_instance.to_dict()
# create an instance of UnexpandedBgpTest from a dict
unexpanded_bgp_test_from_dict = UnexpandedBgpTest.from_dict(unexpanded_bgp_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


