# ApiOutageFilter

Advanced filter query used to filter the response. Can filter on: - outageScope (all, affected tests (e.g. my tests only)). - providerName - interfaceNetwork - applicationName - startDate, endDate - window

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Start of the time range. Must be paired with &#x60;endDate&#x60;. | [optional] 
**end_date** | **str** | End of the time range. Must be paired with &#x60;startDate&#x60;. | [optional] 
**window** | **str** | Specify a time period in the past for which to retrieve data. Alternative to specifying &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
**outage_scope** | [**OutageScope**](OutageScope.md) |  | [optional] 
**provider_name** | **List[str]** | The name used to identify the provider. | [optional] 
**application_name** | **List[str]** | The name to identify the application. | [optional] 
**interface_network** | **List[str]** | The name of the ASN (Interface Network). | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_outage_filter import ApiOutageFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOutageFilter from a JSON string
api_outage_filter_instance = ApiOutageFilter.from_json(json)
# print the JSON string representation of the object
print(ApiOutageFilter.to_json())

# convert the object into a dict
api_outage_filter_dict = api_outage_filter_instance.to_dict()
# create an instance of ApiOutageFilter from a dict
api_outage_filter_from_dict = ApiOutageFilter.from_dict(api_outage_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


