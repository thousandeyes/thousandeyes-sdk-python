# OAuth

Use this only if you want to use OAuth as the authentication mechanism.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | The ID of the OAuth configuration. | [optional] 
**test_url** | **str** | Target for the test. | [optional] 
**request_method** | [**RequestMethod**](RequestMethod.md) |  | [optional] 
**post_body** | **str** | Enter the OAuth body for the HTTP POST request in this field when using OAuth as the authentication mechanism. No special escaping is required. If content is provided in the post body, the &#x60;requestMethod&#x60; is automatically set to POST. | [optional] 
**headers** | **str** | Request headers used for OAuth. | [optional] 
**auth_type** | [**TestAuthType**](TestAuthType.md) |  | [optional] 
**username** | **str** | OAuth username | [optional] 
**password** | **str** | OAuth password | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.o_auth import OAuth

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth from a JSON string
o_auth_instance = OAuth.from_json(json)
# print the JSON string representation of the object
print(OAuth.to_json())

# convert the object into a dict
o_auth_dict = o_auth_instance.to_dict()
# create an instance of OAuth from a dict
o_auth_from_dict = OAuth.from_dict(o_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


