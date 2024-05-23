# EpochTimeWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.epoch_time_window import EpochTimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of EpochTimeWindow from a JSON string
epoch_time_window_instance = EpochTimeWindow.from_json(json)
# print the JSON string representation of the object
print(EpochTimeWindow.to_json())

# convert the object into a dict
epoch_time_window_dict = epoch_time_window_instance.to_dict()
# create an instance of EpochTimeWindow from a dict
epoch_time_window_from_dict = EpochTimeWindow.from_dict(epoch_time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


