# thousandeyes_sdk.streaming.StreamingApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stream**](StreamingApi.md#create_stream) | **POST** /stream | Create data stream
[**delete_stream**](StreamingApi.md#delete_stream) | **DELETE** /stream/{id} | Delete a data stream
[**get_stream**](StreamingApi.md#get_stream) | **GET** /stream/{id} | Retrieve data stream
[**get_streams**](StreamingApi.md#get_streams) | **GET** /stream | List data streams
[**update_stream**](StreamingApi.md#update_stream) | **PUT** /stream/{id} | Update data stream


# **create_stream**
> CreateStreamResponse create_stream(aid=aid, stream=stream)

Create data stream

Creates a new data stream.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.streaming
from thousandeyes_sdk.streaming.models.create_stream_response import CreateStreamResponse
from thousandeyes_sdk.streaming.models.stream import Stream
from thousandeyes_sdk.streaming.rest import ApiException
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
    api_instance = thousandeyes_sdk.streaming.StreamingApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    stream = thousandeyes_sdk.streaming.Stream() # Stream | Stream to configure (optional)

    try:
        # Create data stream
        api_response = api_instance.create_stream(aid=aid, stream=stream)
        print("The response of StreamingApi->create_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingApi->create_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **stream** | [**Stream**](Stream.md)| Stream to configure | [optional] 

### Return type

[**CreateStreamResponse**](CreateStreamResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | item created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**409** | An existing item already exists |  -  |
**412** | Reached limit on number of streams (maximum 5 data streams per account group) |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stream**
> delete_stream(id, aid=aid)

Delete a data stream

Deletes a configured data stream using its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.streaming
from thousandeyes_sdk.streaming.rest import ApiException
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
    api_instance = thousandeyes_sdk.streaming.StreamingApi(api_client)
    id = 'id_example' # str | ID of stream to query
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete a data stream
        api_instance.delete_stream(id, aid=aid)
    except Exception as e:
        print("Exception when calling StreamingApi->delete_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of stream to query | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream**
> GetStreamResponse get_stream(id, aid=aid, type=type)

Retrieve data stream

Retrieves a configured data stream using its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.streaming
from thousandeyes_sdk.streaming.models.get_stream_response import GetStreamResponse
from thousandeyes_sdk.streaming.models.stream_type import StreamType
from thousandeyes_sdk.streaming.rest import ApiException
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
    api_instance = thousandeyes_sdk.streaming.StreamingApi(api_client)
    id = 'id_example' # str | ID of stream to query
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    type = thousandeyes_sdk.streaming.StreamType() # StreamType | Optional filter on type of Stream; should match one of Stream `type` enum (optional)

    try:
        # Retrieve data stream
        api_response = api_instance.get_stream(id, aid=aid, type=type)
        print("The response of StreamingApi->get_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingApi->get_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of stream to query | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **type** | [**StreamType**](.md)| Optional filter on type of Stream; should match one of Stream &#x60;type&#x60; enum | [optional] 

### Return type

[**GetStreamResponse**](GetStreamResponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streams**
> List[GetStreamResponse] get_streams(aid=aid, type=type)

List data streams

Retrieves a list of configured data streams.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.streaming
from thousandeyes_sdk.streaming.models.get_stream_response import GetStreamResponse
from thousandeyes_sdk.streaming.models.stream_type import StreamType
from thousandeyes_sdk.streaming.rest import ApiException
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
    api_instance = thousandeyes_sdk.streaming.StreamingApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    type = thousandeyes_sdk.streaming.StreamType() # StreamType | Optional filter on type of Stream; should match one of Stream `type` enum (optional)

    try:
        # List data streams
        api_response = api_instance.get_streams(aid=aid, type=type)
        print("The response of StreamingApi->get_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingApi->get_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **type** | [**StreamType**](.md)| Optional filter on type of Stream; should match one of Stream &#x60;type&#x60; enum | [optional] 

### Return type

[**List[GetStreamResponse]**](GetStreamResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream**
> GetStreamResponse update_stream(id, aid=aid, put_stream=put_stream)

Update data stream

Updates a configured data stream using its ID. The fields are overwritten, not appended.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.streaming
from thousandeyes_sdk.streaming.models.get_stream_response import GetStreamResponse
from thousandeyes_sdk.streaming.models.put_stream import PutStream
from thousandeyes_sdk.streaming.rest import ApiException
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
    api_instance = thousandeyes_sdk.streaming.StreamingApi(api_client)
    id = 'id_example' # str | ID of stream to query
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    put_stream = thousandeyes_sdk.streaming.PutStream() # PutStream |  (optional)

    try:
        # Update data stream
        api_response = api_instance.update_stream(id, aid=aid, put_stream=put_stream)
        print("The response of StreamingApi->update_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingApi->update_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of stream to query | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **put_stream** | [**PutStream**](PutStream.md)|  | [optional] 

### Return type

[**GetStreamResponse**](GetStreamResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream updated |  -  |
**204** | No content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

