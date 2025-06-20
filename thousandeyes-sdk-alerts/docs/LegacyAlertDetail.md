# LegacyAlertDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**State**](State.md) |  | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.legacy_alert_detail import LegacyAlertDetail

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyAlertDetail from a JSON string
legacy_alert_detail_instance = LegacyAlertDetail.from_json(json)
# print the JSON string representation of the object
print(LegacyAlertDetail.to_json())

# convert the object into a dict
legacy_alert_detail_dict = legacy_alert_detail_instance.to_dict()
# create an instance of LegacyAlertDetail from a dict
legacy_alert_detail_from_dict = LegacyAlertDetail.from_dict(legacy_alert_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


