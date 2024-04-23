# BaseAlertAllOfMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Indicates the number of times this alert has re-entered the &#39;trigger&#39; state after being suppressed. It starts at 1 and increments whenever a real-time ASW ends and the alert conditions remain active. | [optional] 

## Example

```python
from alerts.models.base_alert_all_of_meta import BaseAlertAllOfMeta

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAlertAllOfMeta from a JSON string
base_alert_all_of_meta_instance = BaseAlertAllOfMeta.from_json(json)
# print the JSON string representation of the object
print(BaseAlertAllOfMeta.to_json())

# convert the object into a dict
base_alert_all_of_meta_dict = base_alert_all_of_meta_instance.to_dict()
# create an instance of BaseAlertAllOfMeta from a dict
base_alert_all_of_meta_from_dict = BaseAlertAllOfMeta.from_dict(base_alert_all_of_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


