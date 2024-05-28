# thousandeyes-sdk-tests
This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests.


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
import thousandeyes_sdk.tests
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thousandeyes_sdk.tests
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import thousandeyes_sdk.client
import thousandeyes_sdk.tests
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
    api_instance = thousandeyes_sdk.tests.APIApi(api_client)
    update_api_test = thousandeyes_sdk.tests.UpdateApiTest() # UpdateApiTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Create API test
        api_response = api_instance.create_api_test(update_api_test, aid=aid, expand=expand)
        print("The response of APIApi->create_api_test:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIApi->create_api_test: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thousandeyes.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIApi* | [**create_api_test**](docs/APIApi.md#create_api_test) | **POST** /v7/tests/api | Create API test
*APIApi* | [**delete_api_test**](docs/APIApi.md#delete_api_test) | **DELETE** /v7/tests/api/{testId} | Delete API test
*APIApi* | [**get_api_test**](docs/APIApi.md#get_api_test) | **GET** /v7/tests/api/{testId} | Get API test
*APIApi* | [**get_api_tests**](docs/APIApi.md#get_api_tests) | **GET** /v7/tests/api | List API tests
*APIApi* | [**update_api_test**](docs/APIApi.md#update_api_test) | **PUT** /v7/tests/api/{testId} | Update API test
*AgentToAgentApi* | [**create_agent_to_agent_test**](docs/AgentToAgentApi.md#create_agent_to_agent_test) | **POST** /v7/tests/agent-to-agent | Create Agent to Agent test
*AgentToAgentApi* | [**delete_agent_to_agent_test**](docs/AgentToAgentApi.md#delete_agent_to_agent_test) | **DELETE** /v7/tests/agent-to-agent/{testId} | Delete Agent to Agent test
*AgentToAgentApi* | [**get_agent_to_agent_test**](docs/AgentToAgentApi.md#get_agent_to_agent_test) | **GET** /v7/tests/agent-to-agent/{testId} | Get Agent to Agent test
*AgentToAgentApi* | [**get_agent_to_agent_tests**](docs/AgentToAgentApi.md#get_agent_to_agent_tests) | **GET** /v7/tests/agent-to-agent | List Agent to Agent tests
*AgentToAgentApi* | [**update_agent_to_agent_test**](docs/AgentToAgentApi.md#update_agent_to_agent_test) | **PUT** /v7/tests/agent-to-agent/{testId} | Update Agent to Agent test
*AgentToServerApi* | [**create_agent_to_server_test**](docs/AgentToServerApi.md#create_agent_to_server_test) | **POST** /v7/tests/agent-to-server | Create Agent to Server test
*AgentToServerApi* | [**delete_agent_to_server_test**](docs/AgentToServerApi.md#delete_agent_to_server_test) | **DELETE** /v7/tests/agent-to-server/{testId} | Delete Agent to Server test
*AgentToServerApi* | [**get_agent_to_server_test**](docs/AgentToServerApi.md#get_agent_to_server_test) | **GET** /v7/tests/agent-to-server/{testId} | Get Agent to Server test
*AgentToServerApi* | [**get_agent_to_server_tests**](docs/AgentToServerApi.md#get_agent_to_server_tests) | **GET** /v7/tests/agent-to-server | List Agent to Server tests
*AgentToServerApi* | [**update_agent_to_server_test**](docs/AgentToServerApi.md#update_agent_to_server_test) | **PUT** /v7/tests/agent-to-server/{testId} | Update Agent to Server test
*AllTestTypesApi* | [**get_tests**](docs/AllTestTypesApi.md#get_tests) | **GET** /v7/tests | List configured tests
*BGPApi* | [**create_bgp_test**](docs/BGPApi.md#create_bgp_test) | **POST** /v7/tests/bgp | Create BGP test
*BGPApi* | [**delete_bgp_test**](docs/BGPApi.md#delete_bgp_test) | **DELETE** /v7/tests/bgp/{testId} | Delete BGP test
*BGPApi* | [**get_bgp_test**](docs/BGPApi.md#get_bgp_test) | **GET** /v7/tests/bgp/{testId} | Get BGP test
*BGPApi* | [**get_bgp_tests**](docs/BGPApi.md#get_bgp_tests) | **GET** /v7/tests/bgp | List BGP tests
*BGPApi* | [**update_bgp_test**](docs/BGPApi.md#update_bgp_test) | **PUT** /v7/tests/bgp/{testId} | Update BGP test
*DNSSECApi* | [**create_dns_sec_test**](docs/DNSSECApi.md#create_dns_sec_test) | **POST** /v7/tests/dnssec | Create DNSSEC test
*DNSSECApi* | [**delete_dns_sec_test**](docs/DNSSECApi.md#delete_dns_sec_test) | **DELETE** /v7/tests/dnssec/{testId} | Delete DNSSEC test
*DNSSECApi* | [**get_dns_sec_test**](docs/DNSSECApi.md#get_dns_sec_test) | **GET** /v7/tests/dnssec/{testId} | Get DNSSEC test
*DNSSECApi* | [**get_dns_sec_tests**](docs/DNSSECApi.md#get_dns_sec_tests) | **GET** /v7/tests/dnssec | List DNSSEC tests
*DNSSECApi* | [**update_dns_sec_test**](docs/DNSSECApi.md#update_dns_sec_test) | **PUT** /v7/tests/dnssec/{testId} | Update DNSSEC test
*DNSServerApi* | [**create_dns_server_test**](docs/DNSServerApi.md#create_dns_server_test) | **POST** /v7/tests/dns-server | Create DNS Server test
*DNSServerApi* | [**delete_dns_server_test**](docs/DNSServerApi.md#delete_dns_server_test) | **DELETE** /v7/tests/dns-server/{testId} | Delete DNS Server test
*DNSServerApi* | [**get_dns_server_test**](docs/DNSServerApi.md#get_dns_server_test) | **GET** /v7/tests/dns-server/{testId} | Get DNS Server test
*DNSServerApi* | [**get_dns_server_tests**](docs/DNSServerApi.md#get_dns_server_tests) | **GET** /v7/tests/dns-server | List DNS Server tests
*DNSServerApi* | [**update_dns_server_test**](docs/DNSServerApi.md#update_dns_server_test) | **PUT** /v7/tests/dns-server/{testId} | Update DNS Server test
*DNSTraceApi* | [**create_dns_trace_test**](docs/DNSTraceApi.md#create_dns_trace_test) | **POST** /v7/tests/dns-trace | Create DNS Trace test
*DNSTraceApi* | [**delete_dns_trace_test**](docs/DNSTraceApi.md#delete_dns_trace_test) | **DELETE** /v7/tests/dns-trace/{testId} | Delete DNS Trace test
*DNSTraceApi* | [**get_dns_trace_test**](docs/DNSTraceApi.md#get_dns_trace_test) | **GET** /v7/tests/dns-trace/{testId} | Get DNS Trace test
*DNSTraceApi* | [**get_dns_trace_tests**](docs/DNSTraceApi.md#get_dns_trace_tests) | **GET** /v7/tests/dns-trace | List DNS Trace tests
*DNSTraceApi* | [**update_dns_trace_test**](docs/DNSTraceApi.md#update_dns_trace_test) | **PUT** /v7/tests/dns-trace/{testId} | Update DNS Trace test
*FTPServerApi* | [**create_ftp_server_test**](docs/FTPServerApi.md#create_ftp_server_test) | **POST** /v7/tests/ftp-server | Create FTP Server test
*FTPServerApi* | [**delete_ftp_server_test**](docs/FTPServerApi.md#delete_ftp_server_test) | **DELETE** /v7/tests/ftp-server/{testId} | Delete FTP Server test
*FTPServerApi* | [**get_ftp_server_test**](docs/FTPServerApi.md#get_ftp_server_test) | **GET** /v7/tests/ftp-server/{testId} | Get FTP Server test
*FTPServerApi* | [**get_ftp_server_tests**](docs/FTPServerApi.md#get_ftp_server_tests) | **GET** /v7/tests/ftp-server | List FTP Server tests
*FTPServerApi* | [**update_ftp_server_test**](docs/FTPServerApi.md#update_ftp_server_test) | **PUT** /v7/tests/ftp-server/{testId} | Update FTP Server test
*HTTPServerApi* | [**create_http_server_test**](docs/HTTPServerApi.md#create_http_server_test) | **POST** /v7/tests/http-server | Create HTTP Server test
*HTTPServerApi* | [**delete_http_server_test**](docs/HTTPServerApi.md#delete_http_server_test) | **DELETE** /v7/tests/http-server/{testId} | Delete HTTP Server test
*HTTPServerApi* | [**get_http_server_test**](docs/HTTPServerApi.md#get_http_server_test) | **GET** /v7/tests/http-server/{testId} | Get HTTP Server test
*HTTPServerApi* | [**get_http_server_tests**](docs/HTTPServerApi.md#get_http_server_tests) | **GET** /v7/tests/http-server | List HTTP Server tests
*HTTPServerApi* | [**update_http_server_test**](docs/HTTPServerApi.md#update_http_server_test) | **PUT** /v7/tests/http-server/{testId} | Update HTTP Server test
*PageLoadApi* | [**create_page_load_test**](docs/PageLoadApi.md#create_page_load_test) | **POST** /v7/tests/page-load | Create Page Load test
*PageLoadApi* | [**delete_page_load_test**](docs/PageLoadApi.md#delete_page_load_test) | **DELETE** /v7/tests/page-load/{testId} | Delete Page Load test
*PageLoadApi* | [**get_page_load_test**](docs/PageLoadApi.md#get_page_load_test) | **GET** /v7/tests/page-load/{testId} | Get Page Load test
*PageLoadApi* | [**get_page_load_tests**](docs/PageLoadApi.md#get_page_load_tests) | **GET** /v7/tests/page-load | List Page Load tests
*PageLoadApi* | [**update_page_load_test**](docs/PageLoadApi.md#update_page_load_test) | **PUT** /v7/tests/page-load/{testId} | Update Page Load test
*PathVisualizationInterfaceGroupsApi* | [**create_path_vis_interface_groups**](docs/PathVisualizationInterfaceGroupsApi.md#create_path_vis_interface_groups) | **POST** /v7/network/path-vis/interface-groups | Create interface group for path visualization
*PathVisualizationInterfaceGroupsApi* | [**delete_path_vis_interface_group**](docs/PathVisualizationInterfaceGroupsApi.md#delete_path_vis_interface_group) | **DELETE** /v7/network/path-vis/interface-groups/{interfaceGroupId} | Delete interface group
*PathVisualizationInterfaceGroupsApi* | [**get_path_vis_interface_groups**](docs/PathVisualizationInterfaceGroupsApi.md#get_path_vis_interface_groups) | **GET** /v7/network/path-vis/interface-groups | List interface groups for path visualization
*PathVisualizationInterfaceGroupsApi* | [**update_path_vis_interface_group**](docs/PathVisualizationInterfaceGroupsApi.md#update_path_vis_interface_group) | **PUT** /v7/network/path-vis/interface-groups/{interfaceGroupId} | Update interface group
*SIPServerApi* | [**create_sip_server_test**](docs/SIPServerApi.md#create_sip_server_test) | **POST** /v7/tests/sip-server | Create SIP Server test
*SIPServerApi* | [**delete_sip_server_test**](docs/SIPServerApi.md#delete_sip_server_test) | **DELETE** /v7/tests/sip-server/{testId} | Delete SIP Server test
*SIPServerApi* | [**get_sip_server_test**](docs/SIPServerApi.md#get_sip_server_test) | **GET** /v7/tests/sip-server/{testId} | Get SIP Server test
*SIPServerApi* | [**get_sip_server_tests**](docs/SIPServerApi.md#get_sip_server_tests) | **GET** /v7/tests/sip-server | List SIP Server tests
*SIPServerApi* | [**update_sip_server_test**](docs/SIPServerApi.md#update_sip_server_test) | **PUT** /v7/tests/sip-server/{testId} | Update SIP Server test
*VoiceApi* | [**create_voice_test**](docs/VoiceApi.md#create_voice_test) | **POST** /v7/tests/voice | Create Voice test
*VoiceApi* | [**delete_voice_test**](docs/VoiceApi.md#delete_voice_test) | **DELETE** /v7/tests/voice/{testId} | Delete Voice test
*VoiceApi* | [**get_voice_test**](docs/VoiceApi.md#get_voice_test) | **GET** /v7/tests/voice/{testId} | Get Voice test
*VoiceApi* | [**get_voice_tests**](docs/VoiceApi.md#get_voice_tests) | **GET** /v7/tests/voice | List Voice tests
*VoiceApi* | [**update_voice_test**](docs/VoiceApi.md#update_voice_test) | **PUT** /v7/tests/voice/{testId} | Update Voice test
*WebTransactionApi* | [**create_web_transactions_test**](docs/WebTransactionApi.md#create_web_transactions_test) | **POST** /v7/tests/web-transactions | Create Web Transactions test
*WebTransactionApi* | [**delete_web_transactions_test**](docs/WebTransactionApi.md#delete_web_transactions_test) | **DELETE** /v7/tests/web-transactions/{testId} | Delete Web Transactions test
*WebTransactionApi* | [**get_web_transactions_test**](docs/WebTransactionApi.md#get_web_transactions_test) | **GET** /v7/tests/web-transactions/{testId} | Get Web Transactions test
*WebTransactionApi* | [**get_web_transactions_tests**](docs/WebTransactionApi.md#get_web_transactions_tests) | **GET** /v7/tests/web-transactions | List Web Transactions tests
*WebTransactionApi* | [**update_web_transactions_test**](docs/WebTransactionApi.md#update_web_transactions_test) | **PUT** /v7/tests/web-transactions/{testId} | Update Web Transactions test


## Documentation For Models

 - [Agent](docs/Agent.md)
 - [AgentBase](docs/AgentBase.md)
 - [AgentRequest](docs/AgentRequest.md)
 - [AgentToAgentInstantTest](docs/AgentToAgentInstantTest.md)
 - [AgentToAgentProperties](docs/AgentToAgentProperties.md)
 - [AgentToAgentTest](docs/AgentToAgentTest.md)
 - [AgentToAgentTestProtocol](docs/AgentToAgentTestProtocol.md)
 - [AgentToAgentTests](docs/AgentToAgentTests.md)
 - [AgentToServerInstantTest](docs/AgentToServerInstantTest.md)
 - [AgentToServerProperties](docs/AgentToServerProperties.md)
 - [AgentToServerTest](docs/AgentToServerTest.md)
 - [AgentToServerTests](docs/AgentToServerTests.md)
 - [AlertDirection](docs/AlertDirection.md)
 - [AlertRoundsViolationMode](docs/AlertRoundsViolationMode.md)
 - [AlertRule](docs/AlertRule.md)
 - [AlertType](docs/AlertType.md)
 - [ApiInstantTest](docs/ApiInstantTest.md)
 - [ApiPredefinedVariable](docs/ApiPredefinedVariable.md)
 - [ApiProperties](docs/ApiProperties.md)
 - [ApiRequest](docs/ApiRequest.md)
 - [ApiRequestAssertion](docs/ApiRequestAssertion.md)
 - [ApiRequestAssertionName](docs/ApiRequestAssertionName.md)
 - [ApiRequestAssertionOperator](docs/ApiRequestAssertionOperator.md)
 - [ApiRequestAuthType](docs/ApiRequestAuthType.md)
 - [ApiRequestHeader](docs/ApiRequestHeader.md)
 - [ApiRequestMethod](docs/ApiRequestMethod.md)
 - [ApiRequestVariable](docs/ApiRequestVariable.md)
 - [ApiTest](docs/ApiTest.md)
 - [ApiTests](docs/ApiTests.md)
 - [BaseBgpTest](docs/BaseBgpTest.md)
 - [BaseRequest](docs/BaseRequest.md)
 - [BaseTest](docs/BaseTest.md)
 - [BgpTest](docs/BgpTest.md)
 - [BgpTests](docs/BgpTests.md)
 - [CloudEnterpriseAgentType](docs/CloudEnterpriseAgentType.md)
 - [DnsQueryClass](docs/DnsQueryClass.md)
 - [DnsSecInstantTest](docs/DnsSecInstantTest.md)
 - [DnsSecProperties](docs/DnsSecProperties.md)
 - [DnsSecTest](docs/DnsSecTest.md)
 - [DnsSecTests](docs/DnsSecTests.md)
 - [DnsServerInstantTest](docs/DnsServerInstantTest.md)
 - [DnsServerProperties](docs/DnsServerProperties.md)
 - [DnsServerTest](docs/DnsServerTest.md)
 - [DnsServerTests](docs/DnsServerTests.md)
 - [DnsServersRequest](docs/DnsServersRequest.md)
 - [DnsTraceInstantTest](docs/DnsTraceInstantTest.md)
 - [DnsTraceProperties](docs/DnsTraceProperties.md)
 - [DnsTraceTest](docs/DnsTraceTest.md)
 - [DnsTraceTests](docs/DnsTraceTests.md)
 - [Error](docs/Error.md)
 - [Expand](docs/Expand.md)
 - [FtpServerInstantTest](docs/FtpServerInstantTest.md)
 - [FtpServerProperties](docs/FtpServerProperties.md)
 - [FtpServerRequestType](docs/FtpServerRequestType.md)
 - [FtpServerTest](docs/FtpServerTest.md)
 - [FtpServerTests](docs/FtpServerTests.md)
 - [HttpServerInstantTest](docs/HttpServerInstantTest.md)
 - [HttpServerProperties](docs/HttpServerProperties.md)
 - [HttpServerTest](docs/HttpServerTest.md)
 - [HttpServerTests](docs/HttpServerTests.md)
 - [InstantTest](docs/InstantTest.md)
 - [InterfaceGroup](docs/InterfaceGroup.md)
 - [InterfaceGroups](docs/InterfaceGroups.md)
 - [Link](docs/Link.md)
 - [Monitor](docs/Monitor.md)
 - [MonitorType](docs/MonitorType.md)
 - [MonitorsRequest](docs/MonitorsRequest.md)
 - [PageLoadInstantTest](docs/PageLoadInstantTest.md)
 - [PageLoadProperties](docs/PageLoadProperties.md)
 - [PageLoadTest](docs/PageLoadTest.md)
 - [PageLoadTests](docs/PageLoadTests.md)
 - [SelfLinks](docs/SelfLinks.md)
 - [Severity](docs/Severity.md)
 - [SharedWithAccount](docs/SharedWithAccount.md)
 - [SimpleAgent](docs/SimpleAgent.md)
 - [SimpleTest](docs/SimpleTest.md)
 - [SipServerInstantTest](docs/SipServerInstantTest.md)
 - [SipServerInstantTestRequest](docs/SipServerInstantTestRequest.md)
 - [SipServerInstantTestResponse](docs/SipServerInstantTestResponse.md)
 - [SipServerProperties](docs/SipServerProperties.md)
 - [SipServerTest](docs/SipServerTest.md)
 - [SipServerTests](docs/SipServerTests.md)
 - [SipTestProtocol](docs/SipTestProtocol.md)
 - [TestAuthType](docs/TestAuthType.md)
 - [TestCustomHeaders](docs/TestCustomHeaders.md)
 - [TestDirection](docs/TestDirection.md)
 - [TestDnsServer](docs/TestDnsServer.md)
 - [TestDnsTransportProtocol](docs/TestDnsTransportProtocol.md)
 - [TestDscpId](docs/TestDscpId.md)
 - [TestHttpInterval](docs/TestHttpInterval.md)
 - [TestInterval](docs/TestInterval.md)
 - [TestIpv6Policy](docs/TestIpv6Policy.md)
 - [TestLabel](docs/TestLabel.md)
 - [TestLinks](docs/TestLinks.md)
 - [TestMonitorsProperties](docs/TestMonitorsProperties.md)
 - [TestPageLoadingStrategy](docs/TestPageLoadingStrategy.md)
 - [TestPathTraceMode](docs/TestPathTraceMode.md)
 - [TestProbeMode](docs/TestProbeMode.md)
 - [TestProtocol](docs/TestProtocol.md)
 - [TestRequest](docs/TestRequest.md)
 - [TestSelfLink](docs/TestSelfLink.md)
 - [TestSipCredentials](docs/TestSipCredentials.md)
 - [TestSslVersionId](docs/TestSslVersionId.md)
 - [TestSubInterval](docs/TestSubInterval.md)
 - [TestType](docs/TestType.md)
 - [Tests](docs/Tests.md)
 - [UnauthorizedError](docs/UnauthorizedError.md)
 - [UnexpandedAgentToAgentTest](docs/UnexpandedAgentToAgentTest.md)
 - [UnexpandedAgentToServerTest](docs/UnexpandedAgentToServerTest.md)
 - [UnexpandedApiTest](docs/UnexpandedApiTest.md)
 - [UnexpandedBgpTest](docs/UnexpandedBgpTest.md)
 - [UnexpandedDnsSecTest](docs/UnexpandedDnsSecTest.md)
 - [UnexpandedDnsServerTest](docs/UnexpandedDnsServerTest.md)
 - [UnexpandedDnsTraceTest](docs/UnexpandedDnsTraceTest.md)
 - [UnexpandedFtpServerTest](docs/UnexpandedFtpServerTest.md)
 - [UnexpandedHttpServerTest](docs/UnexpandedHttpServerTest.md)
 - [UnexpandedInstantTest](docs/UnexpandedInstantTest.md)
 - [UnexpandedPageLoadTest](docs/UnexpandedPageLoadTest.md)
 - [UnexpandedSipServerTest](docs/UnexpandedSipServerTest.md)
 - [UnexpandedTest](docs/UnexpandedTest.md)
 - [UnexpandedVoiceTest](docs/UnexpandedVoiceTest.md)
 - [UnexpandedWebTransactionTest](docs/UnexpandedWebTransactionTest.md)
 - [UpdateAgentToAgentTest](docs/UpdateAgentToAgentTest.md)
 - [UpdateAgentToServerTest](docs/UpdateAgentToServerTest.md)
 - [UpdateApiTest](docs/UpdateApiTest.md)
 - [UpdateBgpTest](docs/UpdateBgpTest.md)
 - [UpdateBgpTestRequest](docs/UpdateBgpTestRequest.md)
 - [UpdateDnsSecTest](docs/UpdateDnsSecTest.md)
 - [UpdateDnsServerTest](docs/UpdateDnsServerTest.md)
 - [UpdateDnsTraceTest](docs/UpdateDnsTraceTest.md)
 - [UpdateFtpServerTest](docs/UpdateFtpServerTest.md)
 - [UpdateHttpServerTest](docs/UpdateHttpServerTest.md)
 - [UpdatePageLoadTest](docs/UpdatePageLoadTest.md)
 - [UpdateSipServerTest](docs/UpdateSipServerTest.md)
 - [UpdateSipServerTest1](docs/UpdateSipServerTest1.md)
 - [UpdateVoiceTest](docs/UpdateVoiceTest.md)
 - [UpdateWebTransactionTest](docs/UpdateWebTransactionTest.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorItem](docs/ValidationErrorItem.md)
 - [VoiceInstantTest](docs/VoiceInstantTest.md)
 - [VoiceProperties](docs/VoiceProperties.md)
 - [VoiceTest](docs/VoiceTest.md)
 - [VoiceTests](docs/VoiceTests.md)
 - [WebTransactionInstantTest](docs/WebTransactionInstantTest.md)
 - [WebTransactionProperties](docs/WebTransactionProperties.md)
 - [WebTransactionTest](docs/WebTransactionTest.md)
 - [WebTransactionTests](docs/WebTransactionTests.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author



