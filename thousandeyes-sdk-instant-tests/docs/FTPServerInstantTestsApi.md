# thousandeyes_sdk.instant_tests.FTPServerInstantTestsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ftp_server_instant_test**](FTPServerInstantTestsApi.md#create_ftp_server_instant_test) | **POST** /tests/ftp-server/instant | Create FTP server instant test


# **create_ftp_server_instant_test**
> FtpServerInstantTestResponse create_ftp_server_instant_test(ftp_server_instant_test_request, aid=aid, expand=expand)

Create FTP server instant test

Creates and runs a new FTP server instant test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.instant_tests
from thousandeyes_sdk.instant_tests.models.expand_instant_test_options import ExpandInstantTestOptions
from thousandeyes_sdk.instant_tests.models.ftp_server_instant_test_request import FtpServerInstantTestRequest
from thousandeyes_sdk.instant_tests.models.ftp_server_instant_test_response import FtpServerInstantTestResponse
from thousandeyes_sdk.instant_tests.rest import ApiException
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
with thousandeyes_sdk.instant_tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.instant_tests.FTPServerInstantTestsApi(api_client)
    ftp_server_instant_test_request = thousandeyes_sdk.instant_tests.FtpServerInstantTestRequest() # FtpServerInstantTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.instant_tests.ExpandInstantTestOptions()] # List[ExpandInstantTestOptions] | (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the `agents` sub-resource, use the query `?expand=agent`. (optional)

    try:
        # Create FTP server instant test
        api_response = api_instance.create_ftp_server_instant_test(ftp_server_instant_test_request, aid=aid, expand=expand)
        print("The response of FTPServerInstantTestsApi->create_ftp_server_instant_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerInstantTestsApi->create_ftp_server_instant_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ftp_server_instant_test_request** | [**FtpServerInstantTestRequest**](FtpServerInstantTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandInstantTestOptions]**](ExpandInstantTestOptions.md)| (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the &#x60;agents&#x60; sub-resource, use the query &#x60;?expand&#x3D;agent&#x60;. | [optional] 

### Return type

[**FtpServerInstantTestResponse**](FtpServerInstantTestResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

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

