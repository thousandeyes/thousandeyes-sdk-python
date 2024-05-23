# ApiApplicationOutageAffectedLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The affected location. | [optional] 
**affected_servers** | [**List[ApiApplicationOutageAffectedServer]**](ApiApplicationOutageAffectedServer.md) | The number of affected servers in this location. | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_application_outage_affected_location import ApiApplicationOutageAffectedLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationOutageAffectedLocation from a JSON string
api_application_outage_affected_location_instance = ApiApplicationOutageAffectedLocation.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationOutageAffectedLocation.to_json())

# convert the object into a dict
api_application_outage_affected_location_dict = api_application_outage_affected_location_instance.to_dict()
# create an instance of ApiApplicationOutageAffectedLocation from a dict
api_application_outage_affected_location_from_dict = ApiApplicationOutageAffectedLocation.from_dict(api_application_outage_affected_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


