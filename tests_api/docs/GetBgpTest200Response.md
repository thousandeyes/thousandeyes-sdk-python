# GetBgpTest200Response


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
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**labels** | [**List[TestLabelsInner]**](TestLabelsInner.md) |  | [optional] [readonly] 
**shared_with_accounts** | [**List[TestSharedAccountsInner]**](TestSharedAccountsInner.md) |  | [optional] [readonly] 
**monitors** | [**List[Monitor]**](Monitor.md) | Contains list of enabled BGP monitors. | [optional] [readonly] 
**include_covered_prefixes** | **bool** | Indicate if queries for subprefixes detected under this prefix should included. | [optional] 
**prefix** | **str** | a.b.c.d is a network address, with the prefix length defined as e. Prefixes can be any length from 8 to 24. | 
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used. | [optional] 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**alert_rules** | [**List[AlertRule]**](AlertRule.md) | A list of enabled alert rule objects. | [optional] 

## Example

```python
from tests_api.models.get_bgp_test200_response import GetBgpTest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBgpTest200Response from a JSON string
get_bgp_test200_response_instance = GetBgpTest200Response.from_json(json)
# print the JSON string representation of the object
print GetBgpTest200Response.to_json()

# convert the object into a dict
get_bgp_test200_response_dict = get_bgp_test200_response_instance.to_dict()
# create an instance of GetBgpTest200Response from a dict
get_bgp_test200_response_form_dict = get_bgp_test200_response.from_dict(get_bgp_test200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


