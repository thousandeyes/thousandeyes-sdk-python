# UnitAllocationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** | The total number of allocation units used. | [optional] 
**projected** | **int** | The total number of projected allocation units. | [optional] 
**allocations** | [**List[AllocationUnitUsageBreakdown]**](AllocationUnitUsageBreakdown.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.unit_allocation_summary import UnitAllocationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UnitAllocationSummary from a JSON string
unit_allocation_summary_instance = UnitAllocationSummary.from_json(json)
# print the JSON string representation of the object
print(UnitAllocationSummary.to_json())

# convert the object into a dict
unit_allocation_summary_dict = unit_allocation_summary_instance.to_dict()
# create an instance of UnitAllocationSummary from a dict
unit_allocation_summary_from_dict = UnitAllocationSummary.from_dict(unit_allocation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


