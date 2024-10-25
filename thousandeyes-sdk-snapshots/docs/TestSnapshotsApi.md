# thousandeyes_sdk.snapshots.TestSnapshotsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_snapshot**](TestSnapshotsApi.md#create_test_snapshot) | **POST** /tests/{testId}/snapshot | Create test snapshot


# **create_test_snapshot**
> SnapshotResponse create_test_snapshot(test_id, snapshot_request, aid=aid)

Create test snapshot

This operation creates a test snapshot based on the properties provided in the POST data.  * To use this endpoint, you need the `Create snapshot shares` permission. * You can create a maximum of 5 snapshots per organization within a 5-minute interval. * Snapshots generated through this operation have a 30-day expiration period. * The time range specified with the `from` and `to` parameters must adhere to one of the following intervals: 1, 2, 4, 6, 12, 24, or 48 hours. * The `endDate` field of the snapshot must be set to the present or a past date. * Certain regions may not have public snapshots enabled for compliance reasons. In that case you will get a 403 Forbidden as a response.  **Note**: This operation does not support the creation of operation Agent snapshots. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.snapshots
from thousandeyes_sdk.snapshots.models.snapshot_request import SnapshotRequest
from thousandeyes_sdk.snapshots.models.snapshot_response import SnapshotResponse
from thousandeyes_sdk.snapshots.rest import ApiException
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
    api_instance = thousandeyes_sdk.snapshots.TestSnapshotsApi(api_client)
    test_id = '202701' # str | Test ID
    snapshot_request = thousandeyes_sdk.snapshots.SnapshotRequest() # SnapshotRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create test snapshot
        api_response = api_instance.create_test_snapshot(test_id, snapshot_request, aid=aid)
        print("The response of TestSnapshotsApi->create_test_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSnapshotsApi->create_test_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **snapshot_request** | [**SnapshotRequest**](SnapshotRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

