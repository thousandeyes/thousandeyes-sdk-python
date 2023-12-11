# EndpointTestAid


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 

## Example

```python
from test_results_api.models.endpoint_test_aid import EndpointTestAid

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestAid from a JSON string
endpoint_test_aid_instance = EndpointTestAid.from_json(json)
# print the JSON string representation of the object
print EndpointTestAid.to_json()

# convert the object into a dict
endpoint_test_aid_dict = endpoint_test_aid_instance.to_dict()
# create an instance of EndpointTestAid from a dict
endpoint_test_aid_form_dict = endpoint_test_aid.from_dict(endpoint_test_aid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


