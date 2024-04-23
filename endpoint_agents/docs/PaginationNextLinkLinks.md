# PaginationNextLinkLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from endpoint_agents.models.pagination_next_link_links import PaginationNextLinkLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationNextLinkLinks from a JSON string
pagination_next_link_links_instance = PaginationNextLinkLinks.from_json(json)
# print the JSON string representation of the object
print(PaginationNextLinkLinks.to_json())

# convert the object into a dict
pagination_next_link_links_dict = pagination_next_link_links_instance.to_dict()
# create an instance of PaginationNextLinkLinks from a dict
pagination_next_link_links_from_dict = PaginationNextLinkLinks.from_dict(pagination_next_link_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


