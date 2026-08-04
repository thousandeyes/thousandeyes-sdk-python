# InputConfigMetric

Configuration for metric input data in the stream integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_devices** | [**ConnectedDevices**](ConnectedDevices.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.input_config_metric import InputConfigMetric

# TODO update the JSON string below
json = "{}"
# create an instance of InputConfigMetric from a JSON string
input_config_metric_instance = InputConfigMetric.from_json(json)
# print the JSON string representation of the object
print(InputConfigMetric.to_json())

# convert the object into a dict
input_config_metric_dict = input_config_metric_instance.to_dict()
# create an instance of InputConfigMetric from a dict
input_config_metric_from_dict = InputConfigMetric.from_dict(input_config_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


