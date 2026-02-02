# Assignments

A list of assigned items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.assignments import Assignments

# TODO update the JSON string below
json = "{}"
# create an instance of Assignments from a JSON string
assignments_instance = Assignments.from_json(json)
# print the JSON string representation of the object
print(Assignments.to_json())

# convert the object into a dict
assignments_dict = assignments_instance.to_dict()
# create an instance of Assignments from a dict
assignments_from_dict = Assignments.from_dict(assignments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


