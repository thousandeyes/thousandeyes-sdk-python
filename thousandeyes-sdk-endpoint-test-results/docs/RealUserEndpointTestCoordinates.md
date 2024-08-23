# RealUserEndpointTestCoordinates

Contains approximate GPS location of the endpoint agent, based on endpoint agent’s public IP address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Numeric representations of GPS coordinates. | [optional] [readonly] 
**location** | **str** | Represents named geographical location. | [optional] [readonly] 
**longitude** | **float** | Numeric representations of GPS coordinates. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_coordinates import RealUserEndpointTestCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestCoordinates from a JSON string
real_user_endpoint_test_coordinates_instance = RealUserEndpointTestCoordinates.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestCoordinates.to_json())

# convert the object into a dict
real_user_endpoint_test_coordinates_dict = real_user_endpoint_test_coordinates_instance.to_dict()
# create an instance of RealUserEndpointTestCoordinates from a dict
real_user_endpoint_test_coordinates_from_dict = RealUserEndpointTestCoordinates.from_dict(real_user_endpoint_test_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


