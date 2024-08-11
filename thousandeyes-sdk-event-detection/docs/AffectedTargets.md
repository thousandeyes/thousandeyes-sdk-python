# AffectedTargets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number affected. | [optional] [readonly] 
**in_account_group** | **int** | Indicates if in the affected account group. | [optional] [readonly] 
**targets** | [**List[ApiAffectedTarget]**](ApiAffectedTarget.md) | List of affected targets. | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.affected_targets import AffectedTargets

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedTargets from a JSON string
affected_targets_instance = AffectedTargets.from_json(json)
# print the JSON string representation of the object
print(AffectedTargets.to_json())

# convert the object into a dict
affected_targets_dict = affected_targets_instance.to_dict()
# create an instance of AffectedTargets from a dict
affected_targets_from_dict = AffectedTargets.from_dict(affected_targets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


