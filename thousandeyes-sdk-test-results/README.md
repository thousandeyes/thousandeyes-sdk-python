# thousandeyes-sdk-test-results
Get test result metrics for Network and Application Synthetics tests.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 7.0.54
- Generator version: 7.6.0
- Build package: com.thousandeyes.api.codegen.ThousandeyesPythonGenerator

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

Install directly via PyPi:

```sh
pip install thousandeyes-sdk-test-results
```
(you may need to run `pip` with root permission: `sudo pip install thousandeyes-sdk-test-results`)

Then import the package:
```python
import thousandeyes_sdk.test_results
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thousandeyes_sdk.test_results
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the installation procedure and then run the following:

```python

import thousandeyes_sdk.core
import thousandeyes_sdk.test_results
from thousandeyes_sdk.core.exceptions import ApiException
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
    api_instance = thousandeyes_sdk.test_results.APITestResultsApi(api_client)
    test_id = '202701' # str | Test ID
    agent_id = '11' # str | Agent ID
    round_id = '1384309800' # str | Round ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get API test results by agent and round
        api_response = api_instance.get_test_api_agent_round_results(test_id, agent_id, round_id, aid=aid)
        print("The response of APITestResultsApi->get_test_api_agent_round_results:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APITestResultsApi->get_test_api_agent_round_results: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thousandeyes.com/v7*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APITestResultsApi* | [**get_test_api_agent_round_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/APITestResultsApi.md#get_test_api_agent_round_results) | **GET** /test-results/{testId}/api/agent/{agentId}/round/{roundId} | Get API test results by agent and round
*APITestResultsApi* | [**get_test_api_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/APITestResultsApi.md#get_test_api_results) | **GET** /test-results/{testId}/api | Get API test results
*DNSSECTestResultsApi* | [**get_test_dns_sec_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DNSSECTestResultsApi.md#get_test_dns_sec_results) | **GET** /test-results/{testId}/dnssec | Get DNSSEC test results
*DNSServerTestResultsApi* | [**get_test_dns_server_result**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DNSServerTestResultsApi.md#get_test_dns_server_result) | **GET** /test-results/{testId}/dns-server/{serverId} | Get DNS server test results by server
*DNSServerTestResultsApi* | [**get_test_dns_servers_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DNSServerTestResultsApi.md#get_test_dns_servers_results) | **GET** /test-results/{testId}/dns-server | Get DNS server test results
*DNSTraceTestResultsApi* | [**get_test_dns_trace_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DNSTraceTestResultsApi.md#get_test_dns_trace_results) | **GET** /test-results/{testId}/dns-trace | Get DNS trace test results
*NetworkBGPTestResultsApi* | [**get_test_bgp_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkBGPTestResultsApi.md#get_test_bgp_results) | **GET** /test-results/{testId}/bgp | Get BGP test results
*NetworkBGPTestResultsApi* | [**get_test_bgp_routes_prefix_round_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkBGPTestResultsApi.md#get_test_bgp_routes_prefix_round_results) | **GET** /test-results/{testId}/bgp/routes/prefix/{prefixId}/round/{roundId} | Get BGP route test results by prefix
*NetworkTestResultsApi* | [**get_test_network_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkTestResultsApi.md#get_test_network_results) | **GET** /test-results/{testId}/network | Get network test results
*NetworkTestResultsApi* | [**get_test_path_vis_agent_round_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkTestResultsApi.md#get_test_path_vis_agent_round_results) | **GET** /test-results/{testId}/path-vis/agent/{agentId}/round/{roundId} | Get path visualization test results by agent and round
*NetworkTestResultsApi* | [**get_test_path_vis_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkTestResultsApi.md#get_test_path_vis_results) | **GET** /test-results/{testId}/path-vis | Get path visualization network test results
*VoiceRTPServerTestResultsApi* | [**get_test_rtp_server_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/VoiceRTPServerTestResultsApi.md#get_test_rtp_server_results) | **GET** /test-results/{testId}/rtp-server | Retrieve RTP server test metrics
*VoiceSIPServerTestResultsApi* | [**get_test_sip_server_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/VoiceSIPServerTestResultsApi.md#get_test_sip_server_results) | **GET** /test-results/{testId}/sip-server | Get SIP server test results
*WebFTPServerTestResultsApi* | [**get_test_ftp_server_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebFTPServerTestResultsApi.md#get_test_ftp_server_results) | **GET** /test-results/{testId}/ftp-server | Get FTP server test results
*WebHTTPServerTestResultsApi* | [**get_test_http_server_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebHTTPServerTestResultsApi.md#get_test_http_server_results) | **GET** /test-results/{testId}/http-server | Get HTTP server test results
*WebPageLoadTestResultsApi* | [**get_test_page_load_agent_round_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebPageLoadTestResultsApi.md#get_test_page_load_agent_round_results) | **GET** /test-results/{testId}/page-load/agent/{agentId}/round/{roundId} | Get page load server test results by agent and round
*WebPageLoadTestResultsApi* | [**get_test_page_load_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebPageLoadTestResultsApi.md#get_test_page_load_results) | **GET** /test-results/{testId}/page-load | Get page load server test results
*WebTransactionsTestResultsApi* | [**get_test_web_transaction_agent_round_page_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionsTestResultsApi.md#get_test_web_transaction_agent_round_page_results) | **GET** /test-results/{testId}/web-transactions/agent/{agentId}/round/{roundId}/page/{pageId} | Get detailed web transactions test result by agent, round, and page
*WebTransactionsTestResultsApi* | [**get_test_web_transaction_agent_round_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionsTestResultsApi.md#get_test_web_transaction_agent_round_results) | **GET** /test-results/{testId}/web-transactions/agent/{agentId}/round/{roundId} | Get web transactions test results by agent and round
*WebTransactionsTestResultsApi* | [**get_test_web_transaction_results**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionsTestResultsApi.md#get_test_web_transaction_results) | **GET** /test-results/{testId}/web-transactions | Get web transactions test results


## Documentation For Models

 - [ApiDetailTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiDetailTestResult.md)
 - [ApiDetailTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiDetailTestResults.md)
 - [ApiRequestDetail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiRequestDetail.md)
 - [ApiRequestDetailAssertion](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiRequestDetailAssertion.md)
 - [ApiRequestStepType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiRequestStepType.md)
 - [ApiTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiTestResult.md)
 - [ApiTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ApiTestResults.md)
 - [AppLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/AppLinks.md)
 - [BgpBasicTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/BgpBasicTestResult.md)
 - [BgpHop](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/BgpHop.md)
 - [BgpTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/BgpTestResult.md)
 - [BgpTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/BgpTestResults.md)
 - [BgpTestRouteInformationResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/BgpTestRouteInformationResult.md)
 - [BgpTestRouteInformationResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/BgpTestRouteInformationResults.md)
 - [DnsServerTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DnsServerTestResult.md)
 - [DnsServerTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DnsServerTestResults.md)
 - [DnsTraceTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DnsTraceTestResult.md)
 - [DnsTraceTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DnsTraceTestResults.md)
 - [DnssecTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DnssecTestResult.md)
 - [DnssecTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/DnssecTestResults.md)
 - [EpochTimeWindow](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/EpochTimeWindow.md)
 - [Error](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/Error.md)
 - [Expand](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/Expand.md)
 - [FtpServerTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/FtpServerTestResult.md)
 - [FtpServerTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/FtpServerTestResults.md)
 - [HttpTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/HttpTestResult.md)
 - [HttpTestResultHeaders](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/HttpTestResultHeaders.md)
 - [HttpTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/HttpTestResults.md)
 - [Link](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/Link.md)
 - [Marker](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/Marker.md)
 - [NetworkTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkTestResult.md)
 - [NetworkTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/NetworkTestResults.md)
 - [Page](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/Page.md)
 - [PageLoadDetailTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PageLoadDetailTestResult.md)
 - [PageLoadDetailTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PageLoadDetailTestResults.md)
 - [PageLoadTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PageLoadTestResult.md)
 - [PageLoadTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PageLoadTestResults.md)
 - [PaginationLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PaginationLinks.md)
 - [PathTrace](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathTrace.md)
 - [PathVisBaseTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisBaseTestResult.md)
 - [PathVisDetailTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisDetailTestResult.md)
 - [PathVisDetailTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisDetailTestResults.md)
 - [PathVisDirection](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisDirection.md)
 - [PathVisHop](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisHop.md)
 - [PathVisRoute](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisRoute.md)
 - [PathVisTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisTestResult.md)
 - [PathVisTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/PathVisTestResults.md)
 - [RtpStreamTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/RtpStreamTestResult.md)
 - [RtpStreamTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/RtpStreamTestResults.md)
 - [SelfLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/SelfLinks.md)
 - [SimpleTest](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/SimpleTest.md)
 - [SipServerErrorType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/SipServerErrorType.md)
 - [SipServerTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/SipServerTestResult.md)
 - [SipServerTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/SipServerTestResults.md)
 - [SslCert](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/SslCert.md)
 - [TestDirection](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestDirection.md)
 - [TestInterval](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestInterval.md)
 - [TestLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestLinks.md)
 - [TestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestResult.md)
 - [TestResultAgent](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestResultAgent.md)
 - [TestResultAppLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestResultAppLinks.md)
 - [TestResultMonitor](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestResultMonitor.md)
 - [TestSelfLink](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestSelfLink.md)
 - [TestType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/TestType.md)
 - [UnauthorizedError](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/UnauthorizedError.md)
 - [ValidationError](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ValidationError.md)
 - [ValidationErrorItem](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/ValidationErrorItem.md)
 - [WebTransactionDetailTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionDetailTestResult.md)
 - [WebTransactionDetailTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionDetailTestResults.md)
 - [WebTransactionPageDetailTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionPageDetailTestResult.md)
 - [WebTransactionPageDetailTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionPageDetailTestResults.md)
 - [WebTransactionTestResult](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionTestResult.md)
 - [WebTransactionTestResults](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-test-results/docs/WebTransactionTestResults.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author

<a href="mailto:api-team@thousandeyes.com">ThousandEyes API Team </a>


