# thousandeyes_sdk.agents.TestsAssignmentOnAgentsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_tests**](TestsAssignmentOnAgentsApi.md#assign_tests) | **POST** /agents/{agentId}/tests/assign | Assign tests to an agent
[**overwrite_tests**](TestsAssignmentOnAgentsApi.md#overwrite_tests) | **POST** /agents/{agentId}/tests/override | Overwrite tests assigned to an agent
[**unassign_tests**](TestsAssignmentOnAgentsApi.md#unassign_tests) | **POST** /agents/{agentId}/tests/unassign | Unassign tests from an agent


# **assign_tests**
> AgentDetails assign_tests(agent_id, agent_tests_assign_request, aid=aid)

Assign tests to an agent

Assign tests to a specific Agent. Existing assigned tests are not removed.  **Important notes:**    * The operation fails if the specified agent does not exist.    * If any provided test ID is invalid, the entire operation is canceled.    * Already assigned tests are ignored; other valid tests will be assigned.    * This operation does not overwrite existing assignments.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_details import AgentDetails
from thousandeyes_sdk.agents.models.agent_tests_assign_request import AgentTestsAssignRequest
from thousandeyes_sdk.agents.rest import ApiException
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
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.agents.TestsAssignmentOnAgentsApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the Enterprise Agent cluster to add new agents to.
    agent_tests_assign_request = thousandeyes_sdk.agents.AgentTestsAssignRequest() # AgentTestsAssignRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Assign tests to an agent
        api_response = api_instance.assign_tests(agent_id, agent_tests_assign_request, aid=aid)
        print("The response of TestsAssignmentOnAgentsApi->assign_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsAssignmentOnAgentsApi->assign_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the Enterprise Agent cluster to add new agents to. | 
 **agent_tests_assign_request** | [**AgentTestsAssignRequest**](AgentTestsAssignRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AgentDetails**](AgentDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_tests**
> AgentDetails overwrite_tests(agent_id, agent_tests_assign_request, aid=aid)

Overwrite tests assigned to an agent

Replaces all tests assigned to a specific agent with the new set of test IDs provided.  **Important notes:**    * The operation fails if the specified agent does not exist.    * If any test ID is invalid, the operation is canceled and no changes are made.    * Already assigned tests that are also in the request are ignored.    * Previously assigned tests not included in the request will be removed.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_details import AgentDetails
from thousandeyes_sdk.agents.models.agent_tests_assign_request import AgentTestsAssignRequest
from thousandeyes_sdk.agents.rest import ApiException
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
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.agents.TestsAssignmentOnAgentsApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the Enterprise Agent cluster to add new agents to.
    agent_tests_assign_request = thousandeyes_sdk.agents.AgentTestsAssignRequest() # AgentTestsAssignRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Overwrite tests assigned to an agent
        api_response = api_instance.overwrite_tests(agent_id, agent_tests_assign_request, aid=aid)
        print("The response of TestsAssignmentOnAgentsApi->overwrite_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsAssignmentOnAgentsApi->overwrite_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the Enterprise Agent cluster to add new agents to. | 
 **agent_tests_assign_request** | [**AgentTestsAssignRequest**](AgentTestsAssignRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AgentDetails**](AgentDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_tests**
> AgentDetails unassign_tests(agent_id, agent_tests_assign_request, aid=aid)

Unassign tests from an agent

Unassigns the specified tests from a specific agent.  **Important notes:**    * The operation fails if the specified agent does not exist.    * If any test ID is invalid, the operation is canceled and no changes are made.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_details import AgentDetails
from thousandeyes_sdk.agents.models.agent_tests_assign_request import AgentTestsAssignRequest
from thousandeyes_sdk.agents.rest import ApiException
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
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.agents.TestsAssignmentOnAgentsApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the Enterprise Agent cluster to add new agents to.
    agent_tests_assign_request = thousandeyes_sdk.agents.AgentTestsAssignRequest() # AgentTestsAssignRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Unassign tests from an agent
        api_response = api_instance.unassign_tests(agent_id, agent_tests_assign_request, aid=aid)
        print("The response of TestsAssignmentOnAgentsApi->unassign_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestsAssignmentOnAgentsApi->unassign_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the Enterprise Agent cluster to add new agents to. | 
 **agent_tests_assign_request** | [**AgentTestsAssignRequest**](AgentTestsAssignRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AgentDetails**](AgentDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

