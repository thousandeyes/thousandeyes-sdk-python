# TagFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Filter key used for filtering.  When &#x60;scope&#x60; is &#x60;default&#x60;, accepted values are &#x60;agent-id&#x60;, &#x60;location&#x60;, &#x60;serial-number&#x60;, &#x60;public-network&#x60;, &#x60;local-network&#x60;, &#x60;connection&#x60;, &#x60;gateway&#x60;, &#x60;platform&#x60;, &#x60;nic-model&#x60;, &#x60;nic-driver-version&#x60;, &#x60;agent-type&#x60;, &#x60;proxy-target&#x60;, &#x60;vpn-vendor&#x60;, &#x60;vpn-gateway-address&#x60;, &#x60;vpn-target&#x60;, &#x60;vpn-client-network&#x60;, &#x60;vpn-client-address&#x60;, &#x60;ip-address-family&#x60;, &#x60;ssid&#x60;, &#x60;bssid&#x60;, &#x60;hostname&#x60;, &#x60;username&#x60;, and &#x60;asn&#x60;.  When &#x60;scope&#x60; is &#x60;custom&#x60;, use a user-defined check-in metadata key.  | [optional] 
**values** | **List[str]** |  | [optional] 
**mode** | [**TagFilterMode**](TagFilterMode.md) |  | [optional] 
**scope** | [**TagFilterScope**](TagFilterScope.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.tag_filter import TagFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TagFilter from a JSON string
tag_filter_instance = TagFilter.from_json(json)
# print the JSON string representation of the object
print(TagFilter.to_json())

# convert the object into a dict
tag_filter_dict = tag_filter_instance.to_dict()
# create an instance of TagFilter from a dict
tag_filter_from_dict = TagFilter.from_dict(tag_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


