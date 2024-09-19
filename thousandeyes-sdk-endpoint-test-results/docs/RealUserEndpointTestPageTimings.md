# RealUserEndpointTestPageTimings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_content_load** | **int** | DOM load time in milliseconds. | [optional] [readonly] 
**on_load** | **int** | Page load time in milliseconds. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_timings import RealUserEndpointTestPageTimings

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestPageTimings from a JSON string
real_user_endpoint_test_page_timings_instance = RealUserEndpointTestPageTimings.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestPageTimings.to_json())

# convert the object into a dict
real_user_endpoint_test_page_timings_dict = real_user_endpoint_test_page_timings_instance.to_dict()
# create an instance of RealUserEndpointTestPageTimings from a dict
real_user_endpoint_test_page_timings_from_dict = RealUserEndpointTestPageTimings.from_dict(real_user_endpoint_test_page_timings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


