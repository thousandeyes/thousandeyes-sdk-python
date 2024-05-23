# PaginationNextAndSelfLink

A links object containing a related link for forward pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.pagination_next_and_self_link import PaginationNextAndSelfLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationNextAndSelfLink from a JSON string
pagination_next_and_self_link_instance = PaginationNextAndSelfLink.from_json(json)
# print the JSON string representation of the object
print(PaginationNextAndSelfLink.to_json())

# convert the object into a dict
pagination_next_and_self_link_dict = pagination_next_and_self_link_instance.to_dict()
# create an instance of PaginationNextAndSelfLink from a dict
pagination_next_and_self_link_from_dict = PaginationNextAndSelfLink.from_dict(pagination_next_and_self_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


