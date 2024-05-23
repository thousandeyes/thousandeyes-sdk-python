# AuditOperationWithUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** | ID of the user who created the integration | [optional] 
**created_date** | **int** | Creation date of the integration | [optional] 
**updated_by** | **int** | ID of the user who last updated the integration | [optional] 
**updated_date** | **int** | Date of the last update to the integration | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.audit_operation_with_update import AuditOperationWithUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AuditOperationWithUpdate from a JSON string
audit_operation_with_update_instance = AuditOperationWithUpdate.from_json(json)
# print the JSON string representation of the object
print(AuditOperationWithUpdate.to_json())

# convert the object into a dict
audit_operation_with_update_dict = audit_operation_with_update_instance.to_dict()
# create an instance of AuditOperationWithUpdate from a dict
audit_operation_with_update_from_dict = AuditOperationWithUpdate.from_dict(audit_operation_with_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


