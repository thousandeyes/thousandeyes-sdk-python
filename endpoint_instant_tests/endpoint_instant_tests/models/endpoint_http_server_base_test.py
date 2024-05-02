# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from endpoint_instant_tests.models.endpoint_test_auth_type import EndpointTestAuthType
from endpoint_instant_tests.models.endpoint_test_protocol import EndpointTestProtocol
from endpoint_instant_tests.models.test_probe_mode_response import TestProbeModeResponse
from endpoint_instant_tests.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class EndpointHttpServerBaseTest(BaseModel):
    """
    EndpointHttpServerBaseTest
    """ # noqa: E501
    auth_type: Optional[EndpointTestAuthType] = Field(default=None, alias="authType")
    has_path_trace_in_session: Optional[StrictBool] = Field(default=None, description="Enables \"in session\" path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session.", alias="hasPathTraceInSession")
    http_time_limit: Optional[StrictInt] = Field(default=None, description="Maximum amount of time in milliseconds the agents wait before a request times out.", alias="httpTimeLimit")
    protocol: Optional[EndpointTestProtocol] = None
    url: Optional[StrictStr] = Field(default=None, description="Test target URL. Optionally, you can specify a protocol (http or https). If no protocol is provided, the default `https` protocol is used.")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    verify_certificate: Optional[StrictBool] = Field(default=None, description="Flag indicating if a certificate should be verified.", alias="verifyCertificate")
    __properties: ClassVar[List[str]] = ["authType", "hasPathTraceInSession", "httpTimeLimit", "protocol", "url", "username", "sslVersionId", "tcpProbeMode", "verifyCertificate"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EndpointHttpServerBaseTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointHttpServerBaseTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authType": obj.get("authType"),
            "hasPathTraceInSession": obj.get("hasPathTraceInSession"),
            "httpTimeLimit": obj.get("httpTimeLimit"),
            "protocol": obj.get("protocol"),
            "url": obj.get("url"),
            "username": obj.get("username"),
            "sslVersionId": obj.get("sslVersionId"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "verifyCertificate": obj.get("verifyCertificate")
        })
        return _obj


