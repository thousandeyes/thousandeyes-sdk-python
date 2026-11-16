# OptimizationDataUnavailableDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**OptimizationDataUnavailableCode**](OptimizationDataUnavailableCode.md) |  | 
**status** | **int** |  | 

## Example

```python
from thousandeyes_sdk.alerts.models.optimization_data_unavailable_details import OptimizationDataUnavailableDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationDataUnavailableDetails from a JSON string
optimization_data_unavailable_details_instance = OptimizationDataUnavailableDetails.from_json(json)
# print the JSON string representation of the object
print(OptimizationDataUnavailableDetails.to_json())

# convert the object into a dict
optimization_data_unavailable_details_dict = optimization_data_unavailable_details_instance.to_dict()
# create an instance of OptimizationDataUnavailableDetails from a dict
optimization_data_unavailable_details_from_dict = OptimizationDataUnavailableDetails.from_dict(optimization_data_unavailable_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


