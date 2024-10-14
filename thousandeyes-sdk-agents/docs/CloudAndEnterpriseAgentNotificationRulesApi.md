# thousandeyes_sdk.agents.CloudAndEnterpriseAgentNotificationRulesApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agents_notification_rule**](CloudAndEnterpriseAgentNotificationRulesApi.md#get_agents_notification_rule) | **GET** /agents/notification-rules/{notificationRuleId} | Retrieve agent notification rule
[**get_agents_notification_rules**](CloudAndEnterpriseAgentNotificationRulesApi.md#get_agents_notification_rules) | **GET** /agents/notification-rules | List agent notification rules


# **get_agents_notification_rule**
> NotificationRuleDetail get_agents_notification_rule(notification_rule_id, aid=aid)

Retrieve agent notification rule

Returns details of an agent notification rule, including agents it is assigned to. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.notification_rule_detail import NotificationRuleDetail
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
    api_instance = thousandeyes_sdk.agents.CloudAndEnterpriseAgentNotificationRulesApi(api_client)
    notification_rule_id = '281474976710706' # str | Unique ID for the agent notification rule.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve agent notification rule
        api_response = api_instance.get_agents_notification_rule(notification_rule_id, aid=aid)
        print("The response of CloudAndEnterpriseAgentNotificationRulesApi->get_agents_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAndEnterpriseAgentNotificationRulesApi->get_agents_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_rule_id** | **str**| Unique ID for the agent notification rule. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**NotificationRuleDetail**](NotificationRuleDetail.md)

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
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_notification_rules**
> ListNotificationRulesResponse get_agents_notification_rules(aid=aid)

List agent notification rules

Returns a list of all agent notification rules configured under the account.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.list_notification_rules_response import ListNotificationRulesResponse
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
    api_instance = thousandeyes_sdk.agents.CloudAndEnterpriseAgentNotificationRulesApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List agent notification rules
        api_response = api_instance.get_agents_notification_rules(aid=aid)
        print("The response of CloudAndEnterpriseAgentNotificationRulesApi->get_agents_notification_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAndEnterpriseAgentNotificationRulesApi->get_agents_notification_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ListNotificationRulesResponse**](ListNotificationRulesResponse.md)

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
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

