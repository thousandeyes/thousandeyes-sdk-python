# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EndpointTestAgentSelectorType(str, Enum):
    """
    Retrieve either all available agents, a specific list of agents, or a list of agent labels.
    """

    """
    allowed enum values
    """
    ALL_MINUS_AGENTS = 'all-agents'
    SPECIFIC_MINUS_AGENTS = 'specific-agents'
    AGENT_MINUS_LABELS = 'agent-labels'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EndpointTestAgentSelectorType from a JSON string"""
        return cls(json.loads(json_str))


