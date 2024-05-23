# BaseTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**alert_rules** | [**List[AlertRule]**](AlertRule.md) | Contains list of enabled alert rule objects. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.base_test import BaseTest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTest from a JSON string
base_test_instance = BaseTest.from_json(json)
# print the JSON string representation of the object
print(BaseTest.to_json())

# convert the object into a dict
base_test_dict = base_test_instance.to_dict()
# create an instance of BaseTest from a dict
base_test_from_dict = BaseTest.from_dict(base_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


