# Monitors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitors** | [**List[Monitor]**](Monitor.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.bgp_monitors.models.monitors import Monitors

# TODO update the JSON string below
json = "{}"
# create an instance of Monitors from a JSON string
monitors_instance = Monitors.from_json(json)
# print the JSON string representation of the object
print(Monitors.to_json())

# convert the object into a dict
monitors_dict = monitors_instance.to_dict()
# create an instance of Monitors from a dict
monitors_from_dict = Monitors.from_dict(monitors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


