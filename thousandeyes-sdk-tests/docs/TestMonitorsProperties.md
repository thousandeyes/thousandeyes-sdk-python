# TestMonitorsProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_measurements** | **bool** | Set to &#x60;true&#x60; to enable bgp measurements. | [optional] [default to True]
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]
**monitors** | [**List[Monitor]**](Monitor.md) | Contains list of enabled BGP monitors. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.test_monitors_properties import TestMonitorsProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TestMonitorsProperties from a JSON string
test_monitors_properties_instance = TestMonitorsProperties.from_json(json)
# print the JSON string representation of the object
print(TestMonitorsProperties.to_json())

# convert the object into a dict
test_monitors_properties_dict = test_monitors_properties_instance.to_dict()
# create an instance of TestMonitorsProperties from a dict
test_monitors_properties_from_dict = TestMonitorsProperties.from_dict(test_monitors_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


