# GetTestUnitsUsage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**List[UnitsByTestsBreakdownsInner]**](UnitsByTestsBreakdownsInner.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from usage.models.get_test_units_usage200_response import GetTestUnitsUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestUnitsUsage200Response from a JSON string
get_test_units_usage200_response_instance = GetTestUnitsUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetTestUnitsUsage200Response.to_json())

# convert the object into a dict
get_test_units_usage200_response_dict = get_test_units_usage200_response_instance.to_dict()
# create an instance of GetTestUnitsUsage200Response from a dict
get_test_units_usage200_response_from_dict = GetTestUnitsUsage200Response.from_dict(get_test_units_usage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


