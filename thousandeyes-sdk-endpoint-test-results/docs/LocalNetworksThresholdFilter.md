# LocalNetworksThresholdFilter

Filters the metric using the specified operator and threshold value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**LocalNetworksThresholdFilterName**](LocalNetworksThresholdFilterName.md) |  | [optional] 
**value** | **float** | The threshold value. | [optional] 
**operator** | [**ThresholdFilterOperator**](ThresholdFilterOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.local_networks_threshold_filter import LocalNetworksThresholdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworksThresholdFilter from a JSON string
local_networks_threshold_filter_instance = LocalNetworksThresholdFilter.from_json(json)
# print the JSON string representation of the object
print(LocalNetworksThresholdFilter.to_json())

# convert the object into a dict
local_networks_threshold_filter_dict = local_networks_threshold_filter_instance.to_dict()
# create an instance of LocalNetworksThresholdFilter from a dict
local_networks_threshold_filter_from_dict = LocalNetworksThresholdFilter.from_dict(local_networks_threshold_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


