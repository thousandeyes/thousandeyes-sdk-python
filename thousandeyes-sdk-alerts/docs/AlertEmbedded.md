# AlertEmbedded

Container for embedded resources in alert responses (HATEOAS).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | [**Asn**](Asn.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_embedded import AlertEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of AlertEmbedded from a JSON string
alert_embedded_instance = AlertEmbedded.from_json(json)
# print the JSON string representation of the object
print(AlertEmbedded.to_json())

# convert the object into a dict
alert_embedded_dict = alert_embedded_instance.to_dict()
# create an instance of AlertEmbedded from a dict
alert_embedded_from_dict = AlertEmbedded.from_dict(alert_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


