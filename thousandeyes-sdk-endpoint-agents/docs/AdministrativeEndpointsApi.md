# thousandeyes_sdk.endpoint_agents.AdministrativeEndpointsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoint_agents_connection_string**](AdministrativeEndpointsApi.md#get_endpoint_agents_connection_string) | **GET** /endpoint/agents/connection-string | Get agent connection string


# **get_endpoint_agents_connection_string**
> ConnectionString get_endpoint_agents_connection_string(aid=aid)

Get agent connection string

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.connection_string import ConnectionString
from thousandeyes_sdk.endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.endpoint_agents.AdministrativeEndpointsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get agent connection string
        api_response = api_instance.get_endpoint_agents_connection_string(aid=aid)
        print("The response of AdministrativeEndpointsApi->get_endpoint_agents_connection_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrativeEndpointsApi->get_endpoint_agents_connection_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ConnectionString**](ConnectionString.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

