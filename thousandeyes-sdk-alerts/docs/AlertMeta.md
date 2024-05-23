# AlertMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Indicates the number of times this alert has re-entered the &#39;trigger&#39; state after being suppressed. It starts at 1 and increments whenever a real-time ASW ends and the alert conditions remain active. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_meta import AlertMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AlertMeta from a JSON string
alert_meta_instance = AlertMeta.from_json(json)
# print the JSON string representation of the object
print(AlertMeta.to_json())

# convert the object into a dict
alert_meta_dict = alert_meta_instance.to_dict()
# create an instance of AlertMeta from a dict
alert_meta_from_dict = AlertMeta.from_dict(alert_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


