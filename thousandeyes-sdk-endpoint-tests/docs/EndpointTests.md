# EndpointTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[EndpointTest]**](EndpointTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_tests import EndpointTests

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTests from a JSON string
endpoint_tests_instance = EndpointTests.from_json(json)
# print the JSON string representation of the object
print(EndpointTests.to_json())

# convert the object into a dict
endpoint_tests_dict = endpoint_tests_instance.to_dict()
# create an instance of EndpointTests from a dict
endpoint_tests_from_dict = EndpointTests.from_dict(endpoint_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


