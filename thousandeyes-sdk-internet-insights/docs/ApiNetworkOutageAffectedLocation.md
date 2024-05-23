# ApiNetworkOutageAffectedLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The affected location. | [optional] 
**affected_interfaces** | **List[str]** | The affected interfaces in this location. | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_network_outage_affected_location import ApiNetworkOutageAffectedLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNetworkOutageAffectedLocation from a JSON string
api_network_outage_affected_location_instance = ApiNetworkOutageAffectedLocation.from_json(json)
# print the JSON string representation of the object
print(ApiNetworkOutageAffectedLocation.to_json())

# convert the object into a dict
api_network_outage_affected_location_dict = api_network_outage_affected_location_instance.to_dict()
# create an instance of ApiNetworkOutageAffectedLocation from a dict
api_network_outage_affected_location_from_dict = ApiNetworkOutageAffectedLocation.from_dict(api_network_outage_affected_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


