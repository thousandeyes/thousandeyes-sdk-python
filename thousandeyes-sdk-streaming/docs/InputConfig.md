# InputConfig

Configuration that specifies which input data is included for each signal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**InputConfigMetric**](InputConfigMetric.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.input_config import InputConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InputConfig from a JSON string
input_config_instance = InputConfig.from_json(json)
# print the JSON string representation of the object
print(InputConfig.to_json())

# convert the object into a dict
input_config_dict = input_config_instance.to_dict()
# create an instance of InputConfig from a dict
input_config_from_dict = InputConfig.from_dict(input_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


