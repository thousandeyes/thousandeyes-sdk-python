# instant_tests.AgentToServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_instant_agent_to_server**](AgentToServerApi.md#post_instant_agent_to_server) | **POST** /v7/tests/agent-to-server/instant | Create agent-to-server instant test


# **post_instant_agent_to_server**
> AgentToServerInstantTest post_instant_agent_to_server(agent_to_server_instant_test_request, aid=aid, expand=expand)

Create agent-to-server instant test

Creates and runs a new agent-to-server instant test.

### Example

* Bearer Authentication (BearerAuth):

```python
import instant_tests
from instant_tests.models.agent_to_server_instant_test import AgentToServerInstantTest
from instant_tests.models.agent_to_server_instant_test_request import AgentToServerInstantTestRequest
from instant_tests.models.expand import Expand
from instant_tests.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = instant_tests.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = instant_tests.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with instant_tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instant_tests.AgentToServerApi(api_client)
    agent_to_server_instant_test_request = instant_tests.AgentToServerInstantTestRequest() # AgentToServerInstantTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [instant_tests.Expand()] # List[Expand] | (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the `agents` sub-resource, use the query `?expand=agent`. (optional)

    try:
        # Create agent-to-server instant test
        api_response = api_instance.post_instant_agent_to_server(agent_to_server_instant_test_request, aid=aid, expand=expand)
        print("The response of AgentToServerApi->post_instant_agent_to_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentToServerApi->post_instant_agent_to_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_to_server_instant_test_request** | [**AgentToServerInstantTestRequest**](AgentToServerInstantTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the &#x60;agents&#x60; sub-resource, use the query &#x60;?expand&#x3D;agent&#x60;. | [optional] 

### Return type

[**AgentToServerInstantTest**](AgentToServerInstantTest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

