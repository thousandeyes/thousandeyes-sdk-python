# thousandeyes-sdk-endpoint-test-results
Retrieve results for scheduled and dynamic tests on endpoint agents.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 7.0.4
- Package version: 1.0.0
- Generator version: 7.6.0
- Build package: com.thousandeyes.api.codegen.ThousandeyesPythonGenerator

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import thousandeyes_sdk.endpoint_test_results
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thousandeyes_sdk.endpoint_test_results
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import thousandeyes_sdk.client
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.client.exceptions import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.client.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.endpoint_test_results.LocalNetworkTestsResultsApi(api_client)
    network_topology_id = '00160:39c518560de9:1491651900:236e6f18' # str | The network topology ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve endpoint local network topology
        api_response = api_instance.get_endpoint_local_network_topology_details(network_topology_id, aid=aid)
        print("The response of LocalNetworkTestsResultsApi->get_endpoint_local_network_topology_details:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalNetworkTestsResultsApi->get_endpoint_local_network_topology_details: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thousandeyes.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LocalNetworkTestsResultsApi* | [**get_endpoint_local_network_topology_details**](docs/LocalNetworkTestsResultsApi.md#get_endpoint_local_network_topology_details) | **GET** /v7/endpoint/test-results/local-networks/topologies/{networkTopologyId} | Retrieve endpoint local network topology
*LocalNetworkTestsResultsApi* | [**get_endpoint_local_networks**](docs/LocalNetworkTestsResultsApi.md#get_endpoint_local_networks) | **GET** /v7/endpoint/test-results/local-networks | List local networks
*LocalNetworkTestsResultsApi* | [**get_endpoint_local_networks_topologies**](docs/LocalNetworkTestsResultsApi.md#get_endpoint_local_networks_topologies) | **POST** /v7/endpoint/test-results/local-networks/topologies/filter | List endpoint network topologies probes
*NetworkDynamicTestsResultsApi* | [**get_dynamic_test_result_network_pathvis**](docs/NetworkDynamicTestsResultsApi.md#get_dynamic_test_result_network_pathvis) | **GET** /v7/endpoint/test-results/dynamic-tests/{testId}/path-vis | Retrieve path visualization network dynamic test results
*NetworkDynamicTestsResultsApi* | [**get_dynamic_test_result_pathvis_agent_round**](docs/NetworkDynamicTestsResultsApi.md#get_dynamic_test_result_pathvis_agent_round) | **GET** /v7/endpoint/test-results/dynamic-tests/{testId}/path-vis/agent/{agentId}/round/{roundId} | Retrieve path visualization network dynamic test results details
*NetworkDynamicTestsResultsApi* | [**post_fetch_dynamic_test_result_metrics**](docs/NetworkDynamicTestsResultsApi.md#post_fetch_dynamic_test_result_metrics) | **POST** /v7/endpoint/test-results/dynamic-tests/{testId}/network/filter | Retrieve network dynamic test results
*NetworkScheduledTestsResultsApi* | [**get_test_result_network_pathvis**](docs/NetworkScheduledTestsResultsApi.md#get_test_result_network_pathvis) | **GET** /v7/endpoint/test-results/scheduled-tests/{testId}/path-vis | Retrieve path visualization network scheduled test results
*NetworkScheduledTestsResultsApi* | [**get_test_result_pathvis_agent_round**](docs/NetworkScheduledTestsResultsApi.md#get_test_result_pathvis_agent_round) | **GET** /v7/endpoint/test-results/scheduled-tests/{testId}/path-vis/agent/{agentId}/round/{roundId} | Retrieve path visualization network scheduled test results details
*NetworkScheduledTestsResultsApi* | [**post_fetch_test_result_metrics**](docs/NetworkScheduledTestsResultsApi.md#post_fetch_test_result_metrics) | **POST** /v7/endpoint/test-results/scheduled-tests/{testId}/network/filter | Retrieve network scheduled test results
*NetworkScheduledTestsResultsApi* | [**post_fetch_test_result_metrics_multi_test**](docs/NetworkScheduledTestsResultsApi.md#post_fetch_test_result_metrics_multi_test) | **POST** /v7/endpoint/test-results/scheduled-tests/network/filter | Retrieve network scheduled test results from multiple tests
*RealUserTestsResultsApi* | [**get_endpoint_real_user_test_details**](docs/RealUserTestsResultsApi.md#get_endpoint_real_user_test_details) | **GET** /v7/endpoint/test-results/real-user-tests/{id} | Retrieve endpoint real user test
*RealUserTestsResultsApi* | [**get_endpoint_real_user_test_pages_details**](docs/RealUserTestsResultsApi.md#get_endpoint_real_user_test_pages_details) | **GET** /v7/endpoint/test-results/real-user-tests/{id}/pages/{pageId} | Retrieve endpoint real user test page
*RealUserTestsResultsApi* | [**get_endpoint_real_user_tests**](docs/RealUserTestsResultsApi.md#get_endpoint_real_user_tests) | **POST** /v7/endpoint/test-results/real-user-tests/filter | List endpoint real user tests
*RealUserTestsResultsApi* | [**get_endpoint_real_user_tests_network**](docs/RealUserTestsResultsApi.md#get_endpoint_real_user_tests_network) | **POST** /v7/endpoint/test-results/real-user-tests/networks/filter | List endpoint real user tests
*RealUserTestsResultsApi* | [**get_endpoint_real_user_tests_pages**](docs/RealUserTestsResultsApi.md#get_endpoint_real_user_tests_pages) | **POST** /v7/endpoint/test-results/real-user-tests/pages/filter | List endpoint real user tests visited pages
*WebHTTPServerScheduledTestResultsApi* | [**get_test_result_http_server**](docs/WebHTTPServerScheduledTestResultsApi.md#get_test_result_http_server) | **GET** /v7/endpoint/test-results/scheduled-tests/{testId}/http-server | Retrieve HTTP server scheduled test results


## Documentation For Models

 - [AlertDirection](docs/AlertDirection.md)
 - [AlertRoundsViolationMode](docs/AlertRoundsViolationMode.md)
 - [AlertRule](docs/AlertRule.md)
 - [AlertType](docs/AlertType.md)
 - [ApplicationScoreQuality](docs/ApplicationScoreQuality.md)
 - [AsnDetails](docs/AsnDetails.md)
 - [ConditionalOperator](docs/ConditionalOperator.md)
 - [CpuUtilization](docs/CpuUtilization.md)
 - [DynamicBaseTestResult](docs/DynamicBaseTestResult.md)
 - [DynamicTest](docs/DynamicTest.md)
 - [DynamicTestLinks](docs/DynamicTestLinks.md)
 - [DynamicTestSelfLink](docs/DynamicTestSelfLink.md)
 - [DynamicTestWebex](docs/DynamicTestWebex.md)
 - [DynamicTestsDataRoundSearch](docs/DynamicTestsDataRoundSearch.md)
 - [DynamicTestsDataSearchFilter](docs/DynamicTestsDataSearchFilter.md)
 - [EndpointAgentLabelsSelectorConfig](docs/EndpointAgentLabelsSelectorConfig.md)
 - [EndpointAgentSelectorConfig](docs/EndpointAgentSelectorConfig.md)
 - [EndpointAgentToServerTest](docs/EndpointAgentToServerTest.md)
 - [EndpointAllAgentsSelectorConfig](docs/EndpointAllAgentsSelectorConfig.md)
 - [EndpointBrowser](docs/EndpointBrowser.md)
 - [EndpointHttpDataPointScore](docs/EndpointHttpDataPointScore.md)
 - [EndpointHttpServerBaseTest](docs/EndpointHttpServerBaseTest.md)
 - [EndpointHttpServerTest](docs/EndpointHttpServerTest.md)
 - [EndpointNetworkTopologyResultRequest](docs/EndpointNetworkTopologyResultRequest.md)
 - [EndpointNetworkTopologyResultRequestFilter](docs/EndpointNetworkTopologyResultRequestFilter.md)
 - [EndpointPingDataPointScore](docs/EndpointPingDataPointScore.md)
 - [EndpointRealUserTest](docs/EndpointRealUserTest.md)
 - [EndpointRealUserTestBase](docs/EndpointRealUserTestBase.md)
 - [EndpointRealUserTestDetail](docs/EndpointRealUserTestDetail.md)
 - [EndpointRealUserTestDetailResults](docs/EndpointRealUserTestDetailResults.md)
 - [EndpointRealUserTestResultRequestFilter](docs/EndpointRealUserTestResultRequestFilter.md)
 - [EndpointRealUserTestResults](docs/EndpointRealUserTestResults.md)
 - [EndpointRealUserTestResultsRequest](docs/EndpointRealUserTestResultsRequest.md)
 - [EndpointResultRequestFilter](docs/EndpointResultRequestFilter.md)
 - [EndpointScheduledTest](docs/EndpointScheduledTest.md)
 - [EndpointScheduledTestType](docs/EndpointScheduledTestType.md)
 - [EndpointSpecificAgentsSelectorConfig](docs/EndpointSpecificAgentsSelectorConfig.md)
 - [EndpointTest](docs/EndpointTest.md)
 - [EndpointTestAuthType](docs/EndpointTestAuthType.md)
 - [EndpointTestLinks](docs/EndpointTestLinks.md)
 - [EndpointTestProtocol](docs/EndpointTestProtocol.md)
 - [EndpointTestSelfLink](docs/EndpointTestSelfLink.md)
 - [Error](docs/Error.md)
 - [EthernetProfile](docs/EthernetProfile.md)
 - [Expand](docs/Expand.md)
 - [GatewayNetworkPing](docs/GatewayNetworkPing.md)
 - [Hop](docs/Hop.md)
 - [HttpErrorType](docs/HttpErrorType.md)
 - [HttpTestResult](docs/HttpTestResult.md)
 - [HttpTestResultHeaders](docs/HttpTestResultHeaders.md)
 - [HttpTestResults](docs/HttpTestResults.md)
 - [InterfaceHardwareType](docs/InterfaceHardwareType.md)
 - [Link](docs/Link.md)
 - [LocalNetworkResult](docs/LocalNetworkResult.md)
 - [LocalNetworkResults](docs/LocalNetworkResults.md)
 - [LocalNetworkTopologyDetailResults](docs/LocalNetworkTopologyDetailResults.md)
 - [LocalNetworkTopologyResult](docs/LocalNetworkTopologyResult.md)
 - [LocalNetworkTopologyResultBase](docs/LocalNetworkTopologyResultBase.md)
 - [LocalNetworkTopologyResults](docs/LocalNetworkTopologyResults.md)
 - [MultiTestIdNetworkTestResults](docs/MultiTestIdNetworkTestResults.md)
 - [MultiTestIdTestsDataRoundsSearch](docs/MultiTestIdTestsDataRoundsSearch.md)
 - [MultiTestIdTestsDataSearchFilter](docs/MultiTestIdTestsDataSearchFilter.md)
 - [NetworkDynamicTestResult](docs/NetworkDynamicTestResult.md)
 - [NetworkDynamicTestResults](docs/NetworkDynamicTestResults.md)
 - [NetworkInterface](docs/NetworkInterface.md)
 - [NetworkMetrics](docs/NetworkMetrics.md)
 - [NetworkPing](docs/NetworkPing.md)
 - [NetworkProfile](docs/NetworkProfile.md)
 - [NetworkProxy](docs/NetworkProxy.md)
 - [NetworkProxyProfile](docs/NetworkProxyProfile.md)
 - [NetworkTestResult](docs/NetworkTestResult.md)
 - [NetworkTestResults](docs/NetworkTestResults.md)
 - [NetworkTopologyType](docs/NetworkTopologyType.md)
 - [NetworkWirelessProfile](docs/NetworkWirelessProfile.md)
 - [PaginationNextAndSelfLink](docs/PaginationNextAndSelfLink.md)
 - [PaginationNextLink](docs/PaginationNextLink.md)
 - [PathVisBaseTestResult](docs/PathVisBaseTestResult.md)
 - [PathVisDetailDynamicTestResult](docs/PathVisDetailDynamicTestResult.md)
 - [PathVisDetailDynamicTestResults](docs/PathVisDetailDynamicTestResults.md)
 - [PathVisDetailTestResult](docs/PathVisDetailTestResult.md)
 - [PathVisDetailTestResults](docs/PathVisDetailTestResults.md)
 - [PathVisDynamicTestResult](docs/PathVisDynamicTestResult.md)
 - [PathVisDynamicTestResults](docs/PathVisDynamicTestResults.md)
 - [PathVisEndpoint](docs/PathVisEndpoint.md)
 - [PathVisHop](docs/PathVisHop.md)
 - [PathVisRoute](docs/PathVisRoute.md)
 - [PathVisTestResult](docs/PathVisTestResult.md)
 - [PathVisTestResults](docs/PathVisTestResults.md)
 - [PhysicalMemoryUsedBytes](docs/PhysicalMemoryUsedBytes.md)
 - [Platform](docs/Platform.md)
 - [RealUserTestCoordinates](docs/RealUserTestCoordinates.md)
 - [RealUserTestNetwork](docs/RealUserTestNetwork.md)
 - [RealUserTestNetworkResult](docs/RealUserTestNetworkResult.md)
 - [RealUserTestNetworkResults](docs/RealUserTestNetworkResults.md)
 - [RealUserTestPage](docs/RealUserTestPage.md)
 - [RealUserTestPageDetailResult](docs/RealUserTestPageDetailResult.md)
 - [RealUserTestPageResult](docs/RealUserTestPageResult.md)
 - [RealUserTestPageResults](docs/RealUserTestPageResults.md)
 - [RealUserTestPageTimings](docs/RealUserTestPageTimings.md)
 - [SelfLinks](docs/SelfLinks.md)
 - [Severity](docs/Severity.md)
 - [SortOrder](docs/SortOrder.md)
 - [SystemMetrics](docs/SystemMetrics.md)
 - [TargetNetworkPing](docs/TargetNetworkPing.md)
 - [TargetProfile](docs/TargetProfile.md)
 - [TargetTraceroute](docs/TargetTraceroute.md)
 - [TcpConnect](docs/TcpConnect.md)
 - [TestInterval](docs/TestInterval.md)
 - [TestLabel](docs/TestLabel.md)
 - [TestProbeModeResponse](docs/TestProbeModeResponse.md)
 - [TestProtocol](docs/TestProtocol.md)
 - [TestResult](docs/TestResult.md)
 - [TestSslVersionId](docs/TestSslVersionId.md)
 - [TestsDataRoundsSearch](docs/TestsDataRoundsSearch.md)
 - [TestsDataSearchFilter](docs/TestsDataSearchFilter.md)
 - [TestsDataSearchSort](docs/TestsDataSearchSort.md)
 - [TestsDataSearchSortKey](docs/TestsDataSearchSortKey.md)
 - [TestsDataThresholdFilter](docs/TestsDataThresholdFilter.md)
 - [TestsDataThresholdFilters](docs/TestsDataThresholdFilters.md)
 - [ThresholdFilterName](docs/ThresholdFilterName.md)
 - [ThresholdFilterOperator](docs/ThresholdFilterOperator.md)
 - [Traceroute](docs/Traceroute.md)
 - [TracerouteHop](docs/TracerouteHop.md)
 - [Trigger](docs/Trigger.md)
 - [UnauthorizedError](docs/UnauthorizedError.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorItem](docs/ValidationErrorItem.md)
 - [VpnNetworkPing](docs/VpnNetworkPing.md)
 - [VpnProfile](docs/VpnProfile.md)
 - [VpnTraceroute](docs/VpnTraceroute.md)
 - [VpnType](docs/VpnType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author



