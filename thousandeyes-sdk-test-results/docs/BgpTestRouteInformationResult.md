# BgpTestRouteInformationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**monitor** | [**TestResultMonitor**](TestResultMonitor.md) |  | [optional] 
**prefix_id** | **str** | Internally tracked prefix ID. | [optional] 
**prefix** | **str** | Prefix being tracked. | [optional] 
**is_active** | **bool** | Represents whether the route is active or inactive. An inactive route was an active route in the previous test round and is now superseded by another active (preferred) route. When requesting data for the test round in which a route change happened, both routes (active and inactive one) are included in the response. | [optional] 
**hops** | [**List[BgpHop]**](BgpHop.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.bgp_test_route_information_result import BgpTestRouteInformationResult

# TODO update the JSON string below
json = "{}"
# create an instance of BgpTestRouteInformationResult from a JSON string
bgp_test_route_information_result_instance = BgpTestRouteInformationResult.from_json(json)
# print the JSON string representation of the object
print(BgpTestRouteInformationResult.to_json())

# convert the object into a dict
bgp_test_route_information_result_dict = bgp_test_route_information_result_instance.to_dict()
# create an instance of BgpTestRouteInformationResult from a dict
bgp_test_route_information_result_from_dict = BgpTestRouteInformationResult.from_dict(bgp_test_route_information_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


