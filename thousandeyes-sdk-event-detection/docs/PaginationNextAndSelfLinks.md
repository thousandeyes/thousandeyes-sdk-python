# PaginationNextAndSelfLinks

A links object containing pagination-related links, including only next and self.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.pagination_next_and_self_links import PaginationNextAndSelfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationNextAndSelfLinks from a JSON string
pagination_next_and_self_links_instance = PaginationNextAndSelfLinks.from_json(json)
# print the JSON string representation of the object
print(PaginationNextAndSelfLinks.to_json())

# convert the object into a dict
pagination_next_and_self_links_dict = pagination_next_and_self_links_instance.to_dict()
# create an instance of PaginationNextAndSelfLinks from a dict
pagination_next_and_self_links_from_dict = PaginationNextAndSelfLinks.from_dict(pagination_next_and_self_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


