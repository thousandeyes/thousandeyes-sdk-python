# DynamicBaseTestResultWebex

Contains object with webex conference information. Only returned when `application` == `webex`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **str** | Webex conference ID. | [optional] [readonly] 
**correlation_id** | **str** | Webex conference correlation ID. | [optional] [readonly] 

## Example

```python
from test_results_api.models.dynamic_base_test_result_webex import DynamicBaseTestResultWebex

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicBaseTestResultWebex from a JSON string
dynamic_base_test_result_webex_instance = DynamicBaseTestResultWebex.from_json(json)
# print the JSON string representation of the object
print DynamicBaseTestResultWebex.to_json()

# convert the object into a dict
dynamic_base_test_result_webex_dict = dynamic_base_test_result_webex_instance.to_dict()
# create an instance of DynamicBaseTestResultWebex from a dict
dynamic_base_test_result_webex_form_dict = dynamic_base_test_result_webex.from_dict(dynamic_base_test_result_webex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


