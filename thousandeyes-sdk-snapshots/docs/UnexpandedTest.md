# UnexpandedTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]

## Example

```python
from thousandeyes_sdk.snapshots.models.unexpanded_test import UnexpandedTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedTest from a JSON string
unexpanded_test_instance = UnexpandedTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedTest.to_json())

# convert the object into a dict
unexpanded_test_dict = unexpanded_test_instance.to_dict()
# create an instance of UnexpandedTest from a dict
unexpanded_test_from_dict = UnexpandedTest.from_dict(unexpanded_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


