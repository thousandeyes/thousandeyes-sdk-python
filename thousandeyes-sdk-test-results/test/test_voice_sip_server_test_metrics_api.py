# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.test_results.api.voice_sip_server_test_metrics_api import VoiceSIPServerTestMetricsApi


class TestVoiceSIPServerTestMetricsApi(unittest.TestCase):
    """VoiceSIPServerTestMetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VoiceSIPServerTestMetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_test_sip_server_results_models_validation(self) -> None:
        """Test case for get_test_sip_server_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "endDate" : "2022-07-18T22:00:54Z",
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "numRedirects" : 0,
                    "registerTime" : 21,
                    "optionsTime" : 17,
                    "optionsRequest" : "OPTIONS sip:6054@voice.sfo2.notarealco.com SIP/2.0\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;branch=z9hG4bKRTzPzMoVh0;rport\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nCSeq: 3 OPTIONS\\r\\nContact: <sip:6054@38.140.61.68:55431;transport=tcp>\\r\\nUser-Agent: ThousandEyes Test Call\\r\\nAllow: INVITE, ACK, CANCEL, BYE\\r\\nSupported: outbound, path\\r\\nMax-Forwards: 70\\r\\nExpires: 60\\r\\nContent-Length: 0\\r\\n\\r\\n\\nOPTIONS sip:6054@voice.sfo2.notarealco.com SIP/2.0\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;branch=z9hG4bKRTzPzMoVh0;rport\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nCSeq: 4 OPTIONS\\r\\nContact: <sip:6054@38.140.61.68:55431;transport=tcp>\\r\\nAuthorization: Digest username=\\"al6054\\", realm=\\"asterisk\\", nonce=\\"1598728080/4e3bef2c789bdfa45ce9123221e08c8f\\", uri=\\"sip:6054@voice.sfo2.notarealco.com\\", response=\\"83c538a39ff766cf75ffd1d62317b442\\", algorithm=MD5, cnonce=\\"0a4f113b\\", opaque=\\"748ffa241d840721\\", qop=auth, nc=00000001\\r\\nUser-Agent: ThousandEyes Test Call\\r\\nAllow: INVITE, ACK, CANCEL, BYE\\r\\nSupported: outbound, path\\r\\nMax-Forwards: 70\\r\\nExpires: 60\\r\\nContent-Length: 0\\r\\n\\r\\n",
                    "responseTime" : 12,
                    "totalTime" : 40,
                    "errorType" : "none",
                    "availability" : 100.0,
                    "responseCode" : 200,
                    "optionsResponse" : "SIP/2.0 401 Unauthorized\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;rport=55431;received=38.140.61.68;branch=z9hG4bKRTzPzMoVh0\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>;tag=z9hG4bKRTzPzMoVh0\\r\\nCSeq: 3 OPTIONS\\r\\nWWW-Authenticate: Digest  realm=\\"asterisk\\",nonce=\\"1598728080/4e3bef2c789bdfa45ce9123221e08c8f\\",opaque=\\"748ffa241d840721\\",algorithm=md5,qop=\\"auth\\"\\r\\nServer: Asterisk PBX 16.4.0\\r\\nContent-Length:  0\\r\\n\\r\\n\\nSIP/2.0 200 OK\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;rport=55431;received=38.140.61.68;branch=z9hG4bKRTzPzMoVh0\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>;tag=z9hG4bKRTzPzMoVh0\\r\\nCSeq: 4 OPTIONS\\r\\nAccept: application/xpidf+xml, application/cpim-pidf+xml, application/simple-message-summary, application/pidf+xml, application/dialog-info+xml, application/simple-message-summary, application/pidf+xml, application/dialog-info+xml, application/sdp, message/sipfrag;version=2.0\\r\\nAllow: OPTIONS, REGISTER, SUBSCRIBE, NOTIFY, PUBLISH, INVITE, ACK, BYE, CANCEL, UPDATE, PRACK, MESSAGE, REFER\\r\\nSupported: 100rel, timer, replaces, norefersub\\r\\nAccept-Encoding: text/plain\\r\\nAccept-Language: en\\r\\nServer: Asterisk PBX 16.4.0\\r\\nContent-Length:  0\\r\\n\\r\\n",
                    "problemDetail" : "problemDetail",
                    "connectTime" : 5,
                    "dnsTime" : 2,
                    "serverIp" : "193.2.1.88",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "waitTime" : 5,
                    "inviteTime" : 10
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "numRedirects" : 0,
                    "registerTime" : 21,
                    "optionsTime" : 17,
                    "optionsRequest" : "OPTIONS sip:6054@voice.sfo2.notarealco.com SIP/2.0\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;branch=z9hG4bKRTzPzMoVh0;rport\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nCSeq: 3 OPTIONS\\r\\nContact: <sip:6054@38.140.61.68:55431;transport=tcp>\\r\\nUser-Agent: ThousandEyes Test Call\\r\\nAllow: INVITE, ACK, CANCEL, BYE\\r\\nSupported: outbound, path\\r\\nMax-Forwards: 70\\r\\nExpires: 60\\r\\nContent-Length: 0\\r\\n\\r\\n\\nOPTIONS sip:6054@voice.sfo2.notarealco.com SIP/2.0\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;branch=z9hG4bKRTzPzMoVh0;rport\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nCSeq: 4 OPTIONS\\r\\nContact: <sip:6054@38.140.61.68:55431;transport=tcp>\\r\\nAuthorization: Digest username=\\"al6054\\", realm=\\"asterisk\\", nonce=\\"1598728080/4e3bef2c789bdfa45ce9123221e08c8f\\", uri=\\"sip:6054@voice.sfo2.notarealco.com\\", response=\\"83c538a39ff766cf75ffd1d62317b442\\", algorithm=MD5, cnonce=\\"0a4f113b\\", opaque=\\"748ffa241d840721\\", qop=auth, nc=00000001\\r\\nUser-Agent: ThousandEyes Test Call\\r\\nAllow: INVITE, ACK, CANCEL, BYE\\r\\nSupported: outbound, path\\r\\nMax-Forwards: 70\\r\\nExpires: 60\\r\\nContent-Length: 0\\r\\n\\r\\n",
                    "responseTime" : 12,
                    "totalTime" : 40,
                    "errorType" : "none",
                    "availability" : 100.0,
                    "responseCode" : 200,
                    "optionsResponse" : "SIP/2.0 401 Unauthorized\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;rport=55431;received=38.140.61.68;branch=z9hG4bKRTzPzMoVh0\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>;tag=z9hG4bKRTzPzMoVh0\\r\\nCSeq: 3 OPTIONS\\r\\nWWW-Authenticate: Digest  realm=\\"asterisk\\",nonce=\\"1598728080/4e3bef2c789bdfa45ce9123221e08c8f\\",opaque=\\"748ffa241d840721\\",algorithm=md5,qop=\\"auth\\"\\r\\nServer: Asterisk PBX 16.4.0\\r\\nContent-Length:  0\\r\\n\\r\\n\\nSIP/2.0 200 OK\\r\\nVia: SIP/2.0/TCP 38.140.61.68:55431;rport=55431;received=38.140.61.68;branch=z9hG4bKRTzPzMoVh0\\r\\nCall-ID: oO9WaL3av8@38.140.61.68\\r\\nFrom: <sip:6054@voice.sfo2.notarealco.com>;tag=cGaJDNKQFE\\r\\nTo: <sip:6054@voice.sfo2.notarealco.com>;tag=z9hG4bKRTzPzMoVh0\\r\\nCSeq: 4 OPTIONS\\r\\nAccept: application/xpidf+xml, application/cpim-pidf+xml, application/simple-message-summary, application/pidf+xml, application/dialog-info+xml, application/simple-message-summary, application/pidf+xml, application/dialog-info+xml, application/sdp, message/sipfrag;version=2.0\\r\\nAllow: OPTIONS, REGISTER, SUBSCRIBE, NOTIFY, PUBLISH, INVITE, ACK, BYE, CANCEL, UPDATE, PRACK, MESSAGE, REFER\\r\\nSupported: 100rel, timer, replaces, norefersub\\r\\nAccept-Encoding: text/plain\\r\\nAccept-Language: en\\r\\nServer: Asterisk PBX 16.4.0\\r\\nContent-Length:  0\\r\\n\\r\\n",
                    "problemDetail" : "problemDetail",
                    "connectTime" : 5,
                    "dnsTime" : 2,
                    "serverIp" : "193.2.1.88",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "waitTime" : 5,
                    "inviteTime" : 10
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.SipServerTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
