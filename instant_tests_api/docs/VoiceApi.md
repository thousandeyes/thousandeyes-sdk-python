# instant_tests_api.VoiceApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_instant_voice**](VoiceApi.md#post_instant_voice) | **POST** /v7/tests/voice/instant | Create voice instant test


# **post_instant_voice**
> VoiceInstantTest post_instant_voice(voice_instant_test_request, aid=aid, expand=expand)

Create voice instant test

Creates and runs a voice instant test.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import instant_tests_api
from instant_tests_api.models.expand import Expand
from instant_tests_api.models.voice_instant_test import VoiceInstantTest
from instant_tests_api.models.voice_instant_test_request import VoiceInstantTestRequest
from instant_tests_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = instant_tests_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = instant_tests_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with instant_tests_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instant_tests_api.VoiceApi(api_client)
    voice_instant_test_request = instant_tests_api.VoiceInstantTestRequest() # VoiceInstantTestRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [instant_tests_api.Expand()] # List[Expand] | (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the `agents` sub-resource, use the query `?expand=agent`. (optional)

    try:
        # Create voice instant test
        api_response = api_instance.post_instant_voice(voice_instant_test_request, aid=aid, expand=expand)
        print("The response of VoiceApi->post_instant_voice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoiceApi->post_instant_voice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_instant_test_request** | [**VoiceInstantTestRequest**](VoiceInstantTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the &#x60;agents&#x60; sub-resource, use the query &#x60;?expand&#x3D;agent&#x60;. | [optional] 

### Return type

[**VoiceInstantTest**](VoiceInstantTest.md)

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

