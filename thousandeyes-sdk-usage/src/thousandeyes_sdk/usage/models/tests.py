# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Tests(BaseModel):
    """
    Tests
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="Unique identifier of the account group which owns the test.")
    account_group_name: Optional[StrictStr] = Field(default=None, description="Name of the account group which owns the test.", alias="accountGroupName")
    test_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the test generating usage.", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="Name of the test generating usage.", alias="testName")
    test_type: Optional[StrictStr] = Field(default=None, description="The type of test that generated the usage data. Note that this parameter provides a user-friendly description of the test type and should not be parsed to determine the endpoint for querying configuration details.", alias="testType")
    cloud_units_used: Optional[StrictInt] = Field(default=None, description="Number of cloud units that the test has consumed in the usage period.", alias="cloudUnitsUsed")
    cloud_units_projected: Optional[StrictInt] = Field(default=None, description="The estimated number of cloud units that the test is expected to consume during the usage period. This estimate is determined by considering the units consumed up to the current time and the test's configuration. It's important to note that this value is updated every hour. For new tests, the `cloudUnitsProjected` parameter is absent until the projection is calculated.", alias="cloudUnitsProjected")
    __properties: ClassVar[List[str]] = ["aid", "accountGroupName", "testId", "testName", "testType", "cloudUnitsUsed", "cloudUnitsProjected"]

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
        """Create an instance of Tests from a JSON string"""
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
        """Create an instance of Tests from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "accountGroupName": obj.get("accountGroupName"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "testType": obj.get("testType"),
            "cloudUnitsUsed": obj.get("cloudUnitsUsed"),
            "cloudUnitsProjected": obj.get("cloudUnitsProjected")
        })
        return _obj


