# AuditOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** | ID of the user who created the integration | [optional] 
**created_date** | **int** | Creation date of the integration | [optional] 

## Example

```python
from streaming_api.models.audit_operation import AuditOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AuditOperation from a JSON string
audit_operation_instance = AuditOperation.from_json(json)
# print the JSON string representation of the object
print AuditOperation.to_json()

# convert the object into a dict
audit_operation_dict = audit_operation_instance.to_dict()
# create an instance of AuditOperation from a dict
audit_operation_form_dict = audit_operation.from_dict(audit_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


