# BgpTestRouteInformationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BgpTestRouteInformationResult]**](BgpTestRouteInformationResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.bgp_test_route_information_results import BgpTestRouteInformationResults

# TODO update the JSON string below
json = "{}"
# create an instance of BgpTestRouteInformationResults from a JSON string
bgp_test_route_information_results_instance = BgpTestRouteInformationResults.from_json(json)
# print the JSON string representation of the object
print(BgpTestRouteInformationResults.to_json())

# convert the object into a dict
bgp_test_route_information_results_dict = bgp_test_route_information_results_instance.to_dict()
# create an instance of BgpTestRouteInformationResults from a dict
bgp_test_route_information_results_from_dict = BgpTestRouteInformationResults.from_dict(bgp_test_route_information_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


