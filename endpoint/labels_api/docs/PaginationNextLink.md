# PaginationNextLink

A links object containing a related link for forward pagination.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationNextLinkLinks**](PaginationNextLinkLinks.md) |  | [optional] 

## Example

```python
from labels_api.models.pagination_next_link import PaginationNextLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationNextLink from a JSON string
pagination_next_link_instance = PaginationNextLink.from_json(json)
# print the JSON string representation of the object
print PaginationNextLink.to_json()

# convert the object into a dict
pagination_next_link_dict = pagination_next_link_instance.to_dict()
# create an instance of PaginationNextLink from a dict
pagination_next_link_form_dict = pagination_next_link.from_dict(pagination_next_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


