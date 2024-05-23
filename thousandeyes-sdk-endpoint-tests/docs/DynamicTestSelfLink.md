# DynamicTestSelfLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Its value is either a URI [RFC3986] or a URI template [RFC6570]. | 
**templated** | **bool** | Should be true when the link object&#39;s \&quot;href\&quot; property is a URI template. | [optional] 
**type** | **str** | Used as a hint to indicate the media type expected when dereferencing the target resource. | [optional] 
**deprecation** | **str** | Its presence indicates that the link is to be deprecated at a future date. Its value is a URL that should provide further information about the deprecation. | [optional] 
**name** | **str** | Its value may be used as a secondary key for selecting link objects that share the same relation type. | [optional] 
**profile** | **str** | A URI that hints about the profile of the target resource. | [optional] 
**title** | **str** | Intended for labelling the link with a human-readable identifier | [optional] 
**hreflang** | **str** | Indicates the language of the target resource | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.dynamic_test_self_link import DynamicTestSelfLink

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTestSelfLink from a JSON string
dynamic_test_self_link_instance = DynamicTestSelfLink.from_json(json)
# print the JSON string representation of the object
print(DynamicTestSelfLink.to_json())

# convert the object into a dict
dynamic_test_self_link_dict = dynamic_test_self_link_instance.to_dict()
# create an instance of DynamicTestSelfLink from a dict
dynamic_test_self_link_from_dict = DynamicTestSelfLink.from_dict(dynamic_test_self_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


