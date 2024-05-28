# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_agents.models.agent_search_filters import AgentSearchFilters
from thousandeyes_sdk.endpoint_agents.models.agent_search_sort import AgentSearchSort
from thousandeyes_sdk.endpoint_agents.models.agent_threshold_filters import AgentThresholdFilters
from typing import Optional, Set
from typing_extensions import Self

class AgentSearchRequest(BaseModel):
    """
    Parameters for filtering a list of agents.
    """ # noqa: E501
    search_filters: Optional[AgentSearchFilters] = Field(default=None, alias="searchFilters")
    threshold_filter: Optional[AgentThresholdFilters] = Field(default=None, alias="thresholdFilter")
    search_sort: Optional[List[AgentSearchSort]] = Field(default=None, alias="searchSort")
    __properties: ClassVar[List[str]] = ["searchFilters", "thresholdFilter", "searchSort"]

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
        """Create an instance of AgentSearchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of search_filters
        if self.search_filters:
            _dict['searchFilters'] = self.search_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of threshold_filter
        if self.threshold_filter:
            _dict['thresholdFilter'] = self.threshold_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in search_sort (list)
        _items = []
        if self.search_sort:
            for _item in self.search_sort:
                if _item:
                    _items.append(_item.to_dict())
            _dict['searchSort'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "searchFilters": AgentSearchFilters.from_dict(obj["searchFilters"]) if obj.get("searchFilters") is not None else None,
            "thresholdFilter": AgentThresholdFilters.from_dict(obj["thresholdFilter"]) if obj.get("thresholdFilter") is not None else None,
            "searchSort": [AgentSearchSort.from_dict(_item) for _item in obj["searchSort"]] if obj.get("searchSort") is not None else None
        })
        return _obj

