# UnexpandedInstantTestLinksSelf


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
from snapshots.models.unexpanded_instant_test_links_self import UnexpandedInstantTestLinksSelf

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedInstantTestLinksSelf from a JSON string
unexpanded_instant_test_links_self_instance = UnexpandedInstantTestLinksSelf.from_json(json)
# print the JSON string representation of the object
print(UnexpandedInstantTestLinksSelf.to_json())

# convert the object into a dict
unexpanded_instant_test_links_self_dict = unexpanded_instant_test_links_self_instance.to_dict()
# create an instance of UnexpandedInstantTestLinksSelf from a dict
unexpanded_instant_test_links_self_from_dict = UnexpandedInstantTestLinksSelf.from_dict(unexpanded_instant_test_links_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

