# coding: utf-8

"""
    Administrative API

    Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.administrative.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.administrative.api.account_groups_api import AccountGroupsApi


class TestAccountGroupsApi(unittest.TestCase):
    """AccountGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_create_account_group_models_validation(self) -> None:
        """Test case for create_account_group request and response models"""
        request_body_json = """
                {
                  "accountGroupName" : "My testing account group",
                  "agents" : [ "105", "719" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.administrative.models.AccountGroupRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "isCurrentAccountGroup" : true,
                  "organizationName" : "organizationName",
                  "_links" : {
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
                  "accountGroupName" : "Account A",
                  "isDefaultAccountGroup" : true,
                  "aid" : "1234",
                  "users" : [ {
                    "uid" : "235",
                    "lastLogin" : "2022-07-17T22:00:54Z",
                    "roles" : [ {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    }, {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    } ],
                    "name" : "User X",
                    "email" : "userx@thousandeyes.com",
                    "dateRegistered" : "2022-07-17T22:00:54Z"
                  }, {
                    "uid" : "235",
                    "lastLogin" : "2022-07-17T22:00:54Z",
                    "roles" : [ {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    }, {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    } ],
                    "name" : "User X",
                    "email" : "userx@thousandeyes.com",
                    "dateRegistered" : "2022-07-17T22:00:54Z"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.CreatedAccountGroup.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_account_group_models_validation(self) -> None:
        """Test case for delete_account_group request and response models"""


    def test_get_account_group_models_validation(self) -> None:
        """Test case for get_account_group request and response models"""

        response_body_json = """
                {
                  "isCurrentAccountGroup" : true,
                  "organizationName" : "organizationName",
                  "_links" : {
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
                  "accountGroupName" : "Account A",
                  "isDefaultAccountGroup" : true,
                  "aid" : "1234",
                  "users" : [ {
                    "uid" : "235",
                    "lastLogin" : "2022-07-17T22:00:54Z",
                    "roles" : [ {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    }, {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    } ],
                    "name" : "User X",
                    "email" : "userx@thousandeyes.com",
                    "dateRegistered" : "2022-07-17T22:00:54Z"
                  }, {
                    "uid" : "235",
                    "lastLogin" : "2022-07-17T22:00:54Z",
                    "roles" : [ {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    }, {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    } ],
                    "name" : "User X",
                    "email" : "userx@thousandeyes.com",
                    "dateRegistered" : "2022-07-17T22:00:54Z"
                  } ],
                  "agents" : [ {
                    "localResolutionPrefixes" : [ "10.2.3.3/24", "10.2.3.3/24" ],
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "ipv6Policy" : "force-ipv4",
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "utilization" : 25,
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "clusterMembers" : [ {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    }, {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    } ],
                    "hostname" : "thousandeyes.com",
                    "lastSeen" : "2022-07-17T22:00:54Z",
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "keepBrowserCache" : true,
                    "interfaceIpMappings" : [ {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    }, {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    } ],
                    "agentState" : "online",
                    "targetForTests" : "1.1.1.1",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "accountGroups" : [ {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    }, {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    } ],
                    "verifySslCertificates" : true,
                    "errorDetails" : [ {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    }, {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    } ]
                  }, {
                    "localResolutionPrefixes" : [ "10.2.3.3/24", "10.2.3.3/24" ],
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "ipv6Policy" : "force-ipv4",
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "utilization" : 25,
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "clusterMembers" : [ {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    }, {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    } ],
                    "hostname" : "thousandeyes.com",
                    "lastSeen" : "2022-07-17T22:00:54Z",
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "keepBrowserCache" : true,
                    "interfaceIpMappings" : [ {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    }, {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    } ],
                    "agentState" : "online",
                    "targetForTests" : "1.1.1.1",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "accountGroups" : [ {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    }, {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    } ],
                    "verifySslCertificates" : true,
                    "errorDetails" : [ {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    }, {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    } ]
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.AccountGroupDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_account_groups_models_validation(self) -> None:
        """Test case for get_account_groups request and response models"""

        response_body_json = """
                {
                  "_links" : {
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
                  "accountGroups" : [ {
                    "isCurrentAccountGroup" : true,
                    "organizationName" : "organizationName",
                    "accountGroupName" : "Account A",
                    "isDefaultAccountGroup" : true,
                    "aid" : "1234"
                  }, {
                    "isCurrentAccountGroup" : true,
                    "organizationName" : "organizationName",
                    "accountGroupName" : "Account A",
                    "isDefaultAccountGroup" : true,
                    "aid" : "1234"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.AccountGroups.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_account_group_models_validation(self) -> None:
        """Test case for update_account_group request and response models"""
        request_body_json = """
                {
                  "accountGroupName" : "My testing account group",
                  "agents" : [ "105", "719" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.administrative.models.AccountGroupRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "isCurrentAccountGroup" : true,
                  "organizationName" : "organizationName",
                  "_links" : {
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
                  "accountGroupName" : "Account A",
                  "isDefaultAccountGroup" : true,
                  "aid" : "1234",
                  "users" : [ {
                    "uid" : "235",
                    "lastLogin" : "2022-07-17T22:00:54Z",
                    "roles" : [ {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    }, {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    } ],
                    "name" : "User X",
                    "email" : "userx@thousandeyes.com",
                    "dateRegistered" : "2022-07-17T22:00:54Z"
                  }, {
                    "uid" : "235",
                    "lastLogin" : "2022-07-17T22:00:54Z",
                    "roles" : [ {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    }, {
                      "roleId" : "35",
                      "name" : "Organization Admin",
                      "isBuiltin" : true,
                      "hasManagementPermissions" : true
                    } ],
                    "name" : "User X",
                    "email" : "userx@thousandeyes.com",
                    "dateRegistered" : "2022-07-17T22:00:54Z"
                  } ],
                  "agents" : [ {
                    "localResolutionPrefixes" : [ "10.2.3.3/24", "10.2.3.3/24" ],
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "ipv6Policy" : "force-ipv4",
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "utilization" : 25,
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "clusterMembers" : [ {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    }, {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    } ],
                    "hostname" : "thousandeyes.com",
                    "lastSeen" : "2022-07-17T22:00:54Z",
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "keepBrowserCache" : true,
                    "interfaceIpMappings" : [ {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    }, {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    } ],
                    "agentState" : "online",
                    "targetForTests" : "1.1.1.1",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "accountGroups" : [ {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    }, {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    } ],
                    "verifySslCertificates" : true,
                    "errorDetails" : [ {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    }, {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    } ]
                  }, {
                    "localResolutionPrefixes" : [ "10.2.3.3/24", "10.2.3.3/24" ],
                    "agentId" : "281474976710706",
                    "agentType" : "enterprise-cluster",
                    "ipv6Policy" : "force-ipv4",
                    "prefix" : "99.128.0.0/11",
                    "agentName" : "thousandeyes-stg-va-254",
                    "utilization" : 25,
                    "countryId" : "US",
                    "enabled" : true,
                    "network" : "AT&T Services, Inc. (AS 7018)",
                    "clusterMembers" : [ {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    }, {
                      "lastSeen" : "2022-07-17T22:00:54Z",
                      "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                      "agentState" : "online",
                      "targetForTests" : "1.1.1.1",
                      "name" : "Cluster member name",
                      "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                      "utilization" : 25,
                      "network" : "AT&T Services, Inc. (AS 7018)",
                      "memberId" : "10",
                      "errorDetails" : [ {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      }, {
                        "code" : "agent-version-outdated",
                        "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                      } ]
                    } ],
                    "hostname" : "thousandeyes.com",
                    "lastSeen" : "2022-07-17T22:00:54Z",
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "publicIpAddresses" : [ "192.168.1.78", "f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c" ],
                    "keepBrowserCache" : true,
                    "interfaceIpMappings" : [ {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    }, {
                      "ipAddresses" : [ "73.252.207.219", "2601:646:300:3ae0::b977" ],
                      "interfaceName" : "wlp4s0"
                    } ],
                    "agentState" : "online",
                    "targetForTests" : "1.1.1.1",
                    "ipAddresses" : [ "99.139.65.220", "9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce" ],
                    "location" : "San Francisco Bay Area",
                    "accountGroups" : [ {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    }, {
                      "accountGroupName" : "Account A",
                      "aid" : "1234"
                    } ],
                    "verifySslCertificates" : true,
                    "errorDetails" : [ {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    }, {
                      "code" : "agent-version-outdated",
                      "description" : "Agent Version 0.1.1 (latest: 1.0.0)"
                    } ]
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.AccountGroupDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
