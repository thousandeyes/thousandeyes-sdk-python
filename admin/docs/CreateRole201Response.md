# CreateRole201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the role. | [optional] 
**role_id** | **str** | Unique ID representing the role. | [optional] 
**is_builtin** | **bool** | Flag indicating if the role is built-in (Account Admin, Organization Admin, Regular User). | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from admin.models.create_role201_response import CreateRole201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRole201Response from a JSON string
create_role201_response_instance = CreateRole201Response.from_json(json)
# print the JSON string representation of the object
print(CreateRole201Response.to_json())

# convert the object into a dict
create_role201_response_dict = create_role201_response_instance.to_dict()
# create an instance of CreateRole201Response from a dict
create_role201_response_from_dict = CreateRole201Response.from_dict(create_role201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


