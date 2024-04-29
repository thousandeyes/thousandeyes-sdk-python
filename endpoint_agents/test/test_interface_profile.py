# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_agents.models.interface_profile import InterfaceProfile

class TestInterfaceProfile(unittest.TestCase):
    """InterfaceProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceProfile:
        """Test InterfaceProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceProfile`
        """
        model = InterfaceProfile()
        if include_optional:
            return InterfaceProfile(
                interface_name = 'en0',
                address_profiles = [
                    endpoint_agents.models.address_profile.AddressProfile(
                        address_type = 'unique-local', 
                        ip_address = '2001:db8:3333:4444:5555:6666:7777:8888', 
                        prefix_length = 24, 
                        gateway = '192.168.0.254', 
                        router_hardware_address = '5c:b1:3e:46:1c:84', )
                    ],
                hardware_type = 'wireless',
                ethernet_profile = endpoint_agents.models.ethernet_profile.EthernetProfile(
                    link_speed = 56, ),
                wireless_profile = endpoint_agents.models.wireless_profile.WirelessProfile(
                    bssid = '00:11:22:aa:bb:cc', 
                    ssid = 'GuestWiFi', 
                    rssi = -36, 
                    channel = 48, 
                    phy_mode = '802.11ac', )
            )
        else:
            return InterfaceProfile(
        )
        """

    def testInterfaceProfile(self):
        """Test InterfaceProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()