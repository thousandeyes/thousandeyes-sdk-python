# RoleRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the role. | [optional] 
**permissions** | **List[str]** | Contains list of test permission IDs (get &#x60;permissionId&#x60; from &#x60;/permissions&#x60; operation) | [optional] 

## Example

```python
from thousandeyes_sdk.administrative.models.role_request_body import RoleRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RoleRequestBody from a JSON string
role_request_body_instance = RoleRequestBody.from_json(json)
# print the JSON string representation of the object
print(RoleRequestBody.to_json())

# convert the object into a dict
role_request_body_dict = role_request_body_instance.to_dict()
# create an instance of RoleRequestBody from a dict
role_request_body_from_dict = RoleRequestBody.from_dict(role_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


