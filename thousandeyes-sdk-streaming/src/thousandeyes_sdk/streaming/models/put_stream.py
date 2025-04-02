# coding: utf-8

"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.streaming.models.exporter_config import ExporterConfig
from thousandeyes_sdk.streaming.models.filters import Filters
from thousandeyes_sdk.streaming.models.tag_match import TagMatch
from thousandeyes_sdk.streaming.models.test_match import TestMatch
from typing import Optional, Set
from typing_extensions import Self

class PutStream(BaseModel):
    """
    PutStream
    """ # noqa: E501
    custom_headers: Optional[Dict[str, StrictStr]] = Field(default=None, description="Custom headers.", alias="customHeaders")
    stream_endpoint_url: Optional[StrictStr] = Field(default=None, description="The URL ThousandEyes sends data stream to. For a URL to be valid, it needs to: - Be syntactically correct. - Be reachable. - Use the HTTPS protocol. - When using the `grpc` endpointType, streamEndpointUrl cannot contain paths:     - Valid . `grpc` - `https://example.com`     - Invalid . `grpc` - `https://example.com/collector`.     - Valid . `http` - `https://example.com/collector`.  - When using the `http` endpointType, the operation must match the exact final full URL (including the path if there is one) to which the data will be sent. Examples below:     - `https://api.honeycomb.io:443/v1/metrics`     - `https://ingest.eu0.signalfx.com/v2/datapoint/otlp`", alias="streamEndpointUrl")
    tag_match: Optional[List[TagMatch]] = Field(default=None, description="A collection of tags that determine what tests are included in the data stream. These tag values are also included as attributes in the data stream metrics.", alias="tagMatch")
    test_match: Optional[List[TestMatch]] = Field(default=None, description="A collection of tests to be included in the data stream.", alias="testMatch")
    enabled: Optional[StrictBool] = Field(default=None, description="Flag to enable or disable the stream integration.")
    filters: Optional[Filters] = None
    exporter_config: Optional[ExporterConfig] = Field(default=None, alias="exporterConfig")
    __properties: ClassVar[List[str]] = ["customHeaders", "streamEndpointUrl", "tagMatch", "testMatch", "enabled", "filters", "exporterConfig"]

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
        """Create an instance of PutStream from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exporter_config
        if self.exporter_config:
            _dict['exporterConfig'] = self.exporter_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PutStream from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customHeaders": obj.get("customHeaders"),
            "streamEndpointUrl": obj.get("streamEndpointUrl"),
            "tagMatch": [TagMatch.from_dict(_item) for _item in obj["tagMatch"]] if obj.get("tagMatch") is not None else None,
            "testMatch": [TestMatch.from_dict(_item) for _item in obj["testMatch"]] if obj.get("testMatch") is not None else None,
            "enabled": obj.get("enabled"),
            "filters": Filters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "exporterConfig": ExporterConfig.from_dict(obj["exporterConfig"]) if obj.get("exporterConfig") is not None else None
        })
        return _obj


