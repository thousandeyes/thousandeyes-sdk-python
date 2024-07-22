# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from thousandeyes_sdk.endpoint_test_results.models.endpoint_browser import EndpointBrowser
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_coordinates import RealUserTestCoordinates
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_network import RealUserTestNetwork
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page import RealUserTestPage
from typing import Optional, Set
from typing_extensions import Self

class EndpointRealUserTestDetail(BaseModel):
    """
    EndpointRealUserTestDetail
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint agent, from `/endpoint/agents` endpoint.", alias="agentId")
    committed: Optional[datetime] = Field(default=None, description="UTC date when endpoint real user test was committed to the controller (ISO date-time format).")
    var_date: Optional[datetime] = Field(default=None, description="UTC date when endpoint real user test took place (ISO date-time format).", alias="date")
    experience_score: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="Score rating a user’s experience when loading a particular page, from 0 (the worst) to 1 (the best). [More details](https://docs.thousandeyes.com/product-documentation/end-user-monitoring/viewing-data/endpoint-agent-views-reference#user-experience-score).", alias="experienceScore")
    number_of_pages: Optional[StrictInt] = Field(default=None, description="Number of web pages visited on target website.", alias="numberOfPages")
    organization_name: Optional[StrictStr] = Field(default=None, description="Name of the AS organization `sourceAddress` belongs to.", alias="organizationName")
    port: Optional[StrictInt] = Field(default=None, description="Port used to visit target website.")
    protocol: Optional[StrictStr] = Field(default=None, description="Protocol used to visit target website.")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round.", alias="roundId")
    source_address: Optional[StrictStr] = Field(default=None, description="Public IP address of the endpoint agent during the session.", alias="sourceAddress")
    id: Optional[StrictStr] = Field(default=None, description="Endpoint real user test ID. Each endpoint real user test occurrence has a unique ID.")
    visited_site: Optional[StrictStr] = Field(default=None, description="Domain used to visit target website.", alias="visitedSite")
    browser: Optional[EndpointBrowser] = None
    coordinates: Optional[RealUserTestCoordinates] = None
    pages: Optional[List[RealUserTestPage]] = Field(default=None, description="Web site base domain visited during the session.")
    network: Optional[RealUserTestNetwork] = None
    __properties: ClassVar[List[str]] = ["agentId", "committed", "date", "experienceScore", "numberOfPages", "organizationName", "port", "protocol", "roundId", "sourceAddress", "id", "visitedSite", "browser", "coordinates", "pages", "network"]

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
        """Create an instance of EndpointRealUserTestDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "agent_id",
            "committed",
            "var_date",
            "experience_score",
            "number_of_pages",
            "organization_name",
            "port",
            "protocol",
            "round_id",
            "source_address",
            "id",
            "visited_site",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of browser
        if self.browser:
            _dict['browser'] = self.browser.to_dict()
        # override the default output from pydantic by calling `to_dict()` of coordinates
        if self.coordinates:
            _dict['coordinates'] = self.coordinates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pages (list)
        _items = []
        if self.pages:
            for _item in self.pages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pages'] = _items
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointRealUserTestDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentId": obj.get("agentId"),
            "committed": obj.get("committed"),
            "date": obj.get("date"),
            "experienceScore": obj.get("experienceScore"),
            "numberOfPages": obj.get("numberOfPages"),
            "organizationName": obj.get("organizationName"),
            "port": obj.get("port"),
            "protocol": obj.get("protocol"),
            "roundId": obj.get("roundId"),
            "sourceAddress": obj.get("sourceAddress"),
            "id": obj.get("id"),
            "visitedSite": obj.get("visitedSite"),
            "browser": EndpointBrowser.from_dict(obj["browser"]) if obj.get("browser") is not None else None,
            "coordinates": RealUserTestCoordinates.from_dict(obj["coordinates"]) if obj.get("coordinates") is not None else None,
            "pages": [RealUserTestPage.from_dict(_item) for _item in obj["pages"]] if obj.get("pages") is not None else None,
            "network": RealUserTestNetwork.from_dict(obj["network"]) if obj.get("network") is not None else None
        })
        return _obj


