# PaginationNextAndSelfLinkLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.pagination_next_and_self_link_links import PaginationNextAndSelfLinkLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationNextAndSelfLinkLinks from a JSON string
pagination_next_and_self_link_links_instance = PaginationNextAndSelfLinkLinks.from_json(json)
# print the JSON string representation of the object
print(PaginationNextAndSelfLinkLinks.to_json())

# convert the object into a dict
pagination_next_and_self_link_links_dict = pagination_next_and_self_link_links_instance.to_dict()
# create an instance of PaginationNextAndSelfLinkLinks from a dict
pagination_next_and_self_link_links_from_dict = PaginationNextAndSelfLinkLinks.from_dict(pagination_next_and_self_link_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


