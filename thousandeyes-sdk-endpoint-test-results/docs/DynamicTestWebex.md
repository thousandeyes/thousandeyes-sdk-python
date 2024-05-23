# DynamicTestWebex

Contains object with webex information. Only returned for webex applications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **str** | Webex conference ID. | [optional] [readonly] 
**correlation_id** | **str** | Webex conference correlation ID. | [optional] [readonly] 
**local_sip_session_id** | **str** | Webex calling local sip session ID. | [optional] [readonly] 
**remote_sip_session_id** | **str** | Webex calling remote sip session ID. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_webex import DynamicTestWebex

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTestWebex from a JSON string
dynamic_test_webex_instance = DynamicTestWebex.from_json(json)
# print the JSON string representation of the object
print(DynamicTestWebex.to_json())

# convert the object into a dict
dynamic_test_webex_dict = dynamic_test_webex_instance.to_dict()
# create an instance of DynamicTestWebex from a dict
dynamic_test_webex_from_dict = DynamicTestWebex.from_dict(dynamic_test_webex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


