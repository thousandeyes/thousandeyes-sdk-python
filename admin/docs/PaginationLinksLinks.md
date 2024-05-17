# PaginationLinksLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | [**Link**](Link.md) |  | [optional] 
**next** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.admin.models.pagination_links_links import PaginationLinksLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinksLinks from a JSON string
pagination_links_links_instance = PaginationLinksLinks.from_json(json)
# print the JSON string representation of the object
print(PaginationLinksLinks.to_json())

# convert the object into a dict
pagination_links_links_dict = pagination_links_links_instance.to_dict()
# create an instance of PaginationLinksLinks from a dict
pagination_links_links_from_dict = PaginationLinksLinks.from_dict(pagination_links_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


