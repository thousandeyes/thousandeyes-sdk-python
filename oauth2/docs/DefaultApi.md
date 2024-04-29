# oauth2.DefaultApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v7_oauth2_token_post**](DefaultApi.md#v7_oauth2_token_post) | **POST** /v7/oauth2/token | Create and return access token.


# **v7_oauth2_token_post**
> AccessToken v7_oauth2_token_post(x_tenant_id=x_tenant_id, client_id=client_id, client_secret=client_secret, grant_type=grant_type, scope=scope, thousandeyes_bearer_token=thousandeyes_bearer_token)

Create and return access token.

This endpoint uses the client credentials passed alongside the request to create a new access token and return it to the client.

### Example

* OAuth Authentication (application):

```python
import oauth2
from oauth2.models.access_token import AccessToken
from oauth2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = oauth2.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with oauth2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth2.DefaultApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | Tenant ID, only applicable if using the WanInsights Tenant flow (optional)
    client_id = 'client_id_example' # str | The Application ID. (optional)
    client_secret = 'client_secret_example' # str | The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported. (optional)
    grant_type = 'grant_type_example' # str | Must be set to `client_credentials`. (optional)
    scope = 'scope_example' # str | Requested scope values for the new access token. (optional)
    thousandeyes_bearer_token = 'thousandeyes_bearer_token_example' # str | The user's bearer token, only applicable for special cases where the client wants to make requests on behalf of a user. (optional)

    try:
        # Create and return access token.
        api_response = api_instance.v7_oauth2_token_post(x_tenant_id=x_tenant_id, client_id=client_id, client_secret=client_secret, grant_type=grant_type, scope=scope, thousandeyes_bearer_token=thousandeyes_bearer_token)
        print("The response of DefaultApi->v7_oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v7_oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant ID, only applicable if using the WanInsights Tenant flow | [optional] 
 **client_id** | **str**| The Application ID. | [optional] 
 **client_secret** | **str**| The application secret that was generated for you during the app registration. The Basic auth pattern of instead providing credentials in the Authorization header, per RFC 6749 is also supported. | [optional] 
 **grant_type** | **str**| Must be set to &#x60;client_credentials&#x60;. | [optional] 
 **scope** | **str**| Requested scope values for the new access token. | [optional] 
 **thousandeyes_bearer_token** | **str**| The user&#39;s bearer token, only applicable for special cases where the client wants to make requests on behalf of a user. | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

