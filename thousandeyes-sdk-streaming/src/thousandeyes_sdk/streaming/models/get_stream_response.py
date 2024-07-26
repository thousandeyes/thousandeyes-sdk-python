# coding: utf-8

"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.streaming.models.audit_operation_with_update import AuditOperationWithUpdate
from thousandeyes_sdk.streaming.models.endpoint_type import EndpointType
from thousandeyes_sdk.streaming.models.stream_links import StreamLinks
from thousandeyes_sdk.streaming.models.stream_type import StreamType
from thousandeyes_sdk.streaming.models.tag_match import TagMatch
from thousandeyes_sdk.streaming.models.test_match import TestMatch
from typing import Optional, Set
from typing_extensions import Self

class GetStreamResponse(BaseModel):
    """
    GetStreamResponse
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The data stream ID")
    enabled: Optional[StrictBool] = Field(default=None, description="Flag to enable or disable the stream integration.")
    links: Optional[StreamLinks] = Field(default=None, alias="_links")
    type: Optional[StreamType] = None
    endpoint_type: Optional[EndpointType] = Field(default=None, alias="endpointType")
    stream_endpoint_url: Optional[StrictStr] = Field(default=None, description="The URL ThousandEyes sends data stream to. For a URL to be valid, it needs to: - Be syntactically correct. - Be reachable. - Use the HTTPS protocol. - When using the `grpc` endpointType, streamEndpointUrl cannot contain paths:     - Valid . `grpc` - `https://example.com`     - Invalid . `grpc` - `https://example.com/collector`.     - Valid . `http` - `https://example.com/collector`.      - When using the `http` endpointType, the endpoint must match the exact final full URL (including the path if there is one) to which the metrics will be sent. Examples below:     - `https://api.honeycomb.io:443/v1/metrics`     - `https://ingest.eu0.signalfx.com/v2/datapoint/otlp`", alias="streamEndpointUrl")
    custom_headers: Optional[Dict[str, StrictStr]] = Field(default=None, description="Custom headers. **Note**: When using the `splunk-hec` `type`, the `customHeaders` must contain just one element with the key `token` and the value of the *Splunk HEC Token*.", alias="customHeaders")
    tag_match: Optional[List[TagMatch]] = Field(default=None, description="A collection of tags that determine what tests are included in the data stream. These tag values are also included as attributes in the data stream metrics.", alias="tagMatch")
    test_match: Optional[List[TestMatch]] = Field(default=None, description="A collection of tests to be included in the data stream.", alias="testMatch")
    audit_operation: Optional[AuditOperationWithUpdate] = Field(default=None, alias="auditOperation")
    __properties: ClassVar[List[str]] = ["id", "enabled", "_links", "type", "endpointType", "streamEndpointUrl", "customHeaders", "tagMatch", "testMatch", "auditOperation"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return self.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetStreamResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tag_match (list)
        _items = []
        if self.tag_match:
            for _item in self.tag_match:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tagMatch'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in test_match (list)
        _items = []
        if self.test_match:
            for _item in self.test_match:
                if _item:
                    _items.append(_item.to_dict())
            _dict['testMatch'] = _items
        # override the default output from pydantic by calling `to_dict()` of audit_operation
        if self.audit_operation:
            _dict['auditOperation'] = self.audit_operation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetStreamResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "enabled": obj.get("enabled"),
            "_links": StreamLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "type": obj.get("type"),
            "endpointType": obj.get("endpointType"),
            "streamEndpointUrl": obj.get("streamEndpointUrl"),
            "customHeaders": obj.get("customHeaders"),
            "tagMatch": [TagMatch.from_dict(_item) for _item in obj["tagMatch"]] if obj.get("tagMatch") is not None else None,
            "testMatch": [TestMatch.from_dict(_item) for _item in obj["testMatch"]] if obj.get("testMatch") is not None else None,
            "auditOperation": AuditOperationWithUpdate.from_dict(obj["auditOperation"]) if obj.get("auditOperation") is not None else None
        })
        return _obj


