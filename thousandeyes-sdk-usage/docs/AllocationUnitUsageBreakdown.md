# AllocationUnitUsageBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | The product name of the allocation. | [optional] 
**allocated_units** | **int** | The number of allocated units for the product. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.allocation_unit_usage_breakdown import AllocationUnitUsageBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationUnitUsageBreakdown from a JSON string
allocation_unit_usage_breakdown_instance = AllocationUnitUsageBreakdown.from_json(json)
# print the JSON string representation of the object
print(AllocationUnitUsageBreakdown.to_json())

# convert the object into a dict
allocation_unit_usage_breakdown_dict = allocation_unit_usage_breakdown_instance.to_dict()
# create an instance of AllocationUnitUsageBreakdown from a dict
allocation_unit_usage_breakdown_from_dict = AllocationUnitUsageBreakdown.from_dict(allocation_unit_usage_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


