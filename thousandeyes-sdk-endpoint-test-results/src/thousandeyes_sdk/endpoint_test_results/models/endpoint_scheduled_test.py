# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_server_test import EndpointHttpServerTest
from pydantic import StrictStr, Field, model_serializer
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ENDPOINTSCHEDULEDTEST_ONE_OF_SCHEMAS = ["EndpointAgentToServerTest", "EndpointHttpServerTest"]

class EndpointScheduledTest(BaseModel):
    """
    EndpointScheduledTest
    """
    # data type: EndpointAgentToServerTest
    oneof_schema_1_validator: Optional[EndpointAgentToServerTest] = None
    # data type: EndpointHttpServerTest
    oneof_schema_2_validator: Optional[EndpointHttpServerTest] = None
    actual_instance: Optional[Union[EndpointAgentToServerTest, EndpointHttpServerTest]] = None
    one_of_schemas: Set[str] = { "EndpointAgentToServerTest", "EndpointHttpServerTest" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = EndpointScheduledTest.model_construct()
        error_messages = []
        match = 0
        # validate data type: EndpointAgentToServerTest
        if not isinstance(v, EndpointAgentToServerTest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EndpointAgentToServerTest`")
        else:
            match += 1
        # validate data type: EndpointHttpServerTest
        if not isinstance(v, EndpointHttpServerTest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EndpointHttpServerTest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EndpointScheduledTest with oneOf schemas: EndpointAgentToServerTest, EndpointHttpServerTest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EndpointScheduledTest with oneOf schemas: EndpointAgentToServerTest, EndpointHttpServerTest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into EndpointAgentToServerTest
        try:
            instance.actual_instance = EndpointAgentToServerTest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EndpointHttpServerTest
        try:
            instance.actual_instance = EndpointHttpServerTest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EndpointScheduledTest with oneOf schemas: EndpointAgentToServerTest, EndpointHttpServerTest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EndpointScheduledTest with oneOf schemas: EndpointAgentToServerTest, EndpointHttpServerTest. Details: " + ", ".join(error_messages))
        else:
            return instance

    @model_serializer(when_used="json")
    def serialize_model(self):
        return json.loads(self.to_json())

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], EndpointAgentToServerTest, EndpointHttpServerTest]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


