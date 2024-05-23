# ApiApplicationOutageAffectedServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_application_outage_affected_server import ApiApplicationOutageAffectedServer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationOutageAffectedServer from a JSON string
api_application_outage_affected_server_instance = ApiApplicationOutageAffectedServer.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationOutageAffectedServer.to_json())

# convert the object into a dict
api_application_outage_affected_server_dict = api_application_outage_affected_server_instance.to_dict()
# create an instance of ApiApplicationOutageAffectedServer from a dict
api_application_outage_affected_server_from_dict = ApiApplicationOutageAffectedServer.from_dict(api_application_outage_affected_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


