# AlertEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message used for email notification. | [optional] 
**recipients** | **List[str]** | List of recipients emails that will be notified. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.alert_email import AlertEmail

# TODO update the JSON string below
json = "{}"
# create an instance of AlertEmail from a JSON string
alert_email_instance = AlertEmail.from_json(json)
# print the JSON string representation of the object
print(AlertEmail.to_json())

# convert the object into a dict
alert_email_dict = alert_email_instance.to_dict()
# create an instance of AlertEmail from a dict
alert_email_from_dict = AlertEmail.from_dict(alert_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


