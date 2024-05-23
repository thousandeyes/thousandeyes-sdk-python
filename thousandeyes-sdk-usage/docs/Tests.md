# Tests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Unique identifier of the account group which owns the test. | [optional] 
**account_group_name** | **str** | Name of the account group which owns the test. | [optional] 
**test_id** | **str** | Unique identifier of the test generating usage. | [optional] 
**test_name** | **str** | Name of the test generating usage. | [optional] 
**test_type** | **str** | The type of test that generated the usage data. Note that this parameter provides a user-friendly description of the test type and should not be parsed to determine the endpoint for querying configuration details. | [optional] 
**cloud_units_used** | **int** | Number of cloud units that the test has consumed in the usage period. | [optional] 
**cloud_units_projected** | **int** | The estimated number of cloud units that the test is expected to consume during the usage period. This estimate is determined by considering the units consumed up to the current time and the test&#39;s configuration. It&#39;s important to note that this value is updated every hour. For new tests, the &#x60;cloudUnitsProjected&#x60; parameter is absent until the projection is calculated. | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.tests import Tests

# TODO update the JSON string below
json = "{}"
# create an instance of Tests from a JSON string
tests_instance = Tests.from_json(json)
# print the JSON string representation of the object
print(Tests.to_json())

# convert the object into a dict
tests_dict = tests_instance.to_dict()
# create an instance of Tests from a dict
tests_from_dict = Tests.from_dict(tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


